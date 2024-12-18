from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import * 
from .main_interface import MainInterface

import numpy as np


from matplotlib.ticker import FuncFormatter
 

class Compta(MainInterface):
    def __init__(self,main_inter): 
        self.main_inter = main_inter 
        self.show_dashboard_inter()
        
        
    def show_dashboard_inter(self):
        self.main_inter.clear_content_frame()
        self.dashbord_widget = QWidget()
        self.dashbord_widget.setObjectName("dashbord_widget")

        # Layout principal
        layout = QVBoxLayout(self.dashbord_widget)
        
        # Layouts horizontaux pour les graphiques
        graphs_layout = QHBoxLayout()
        
        # Graphique 1 : Pourcentage des situations pour ce mois
        self.situation_canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.situation_canvas.setObjectName("dashbord_graphe")
        self.plot_situation_graph()
        graphs_layout.addWidget(self.situation_canvas)
        
        # Graphique 2 : Revenus mensuels pour cette année
        self.revenue_canvas = QWidget()
        self.revenue_canvas.setObjectName("dashbord_graphe_stat")

        
        self.plot_revenue_graph()



        graphs_layout.addWidget(self.revenue_canvas)
        
        # Ajout des graphiques au layout principal
        layout.addLayout(graphs_layout)
        
        # Tableau pour afficher les adhérents avec situation = NON

        graphs2_layout = QHBoxLayout() 
        # Graphique 1 : Pourcentage des situations pour ce mois
        self.situation_canvas2 = FigureCanvas(Figure(figsize=(5, 4)))
        self.situation_canvas2.setObjectName("dashbord_graphe") 
        self.plot_situation_graph2()
        graphs2_layout.addWidget(self.situation_canvas2) 

 
        

        layout.addLayout(graphs2_layout) 

        
        self.main_inter.content_layout.addWidget(self.dashbord_widget) 
 

    def actualiser(self):
        self.achats_input.setText("test")


    def filter_table(self):
        # Get the filter text from the search bar
        filter_text = self.search_bar.text().lower()

        # Loop through all rows and hide/show them based on the search
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)  # Assuming column 0 is 'Nom'
            if item is not None:
                if filter_text in item.text().lower():  # Case-insensitive comparison
                    self.tableWidget.setRowHidden(row, False)
                else:
                    self.tableWidget.setRowHidden(row, True)

    def plot_situation_graph(self):
        """Affiche le pourcentage des situations pour le mois actuel"""
        donnees = recuperer_compta_each_year()
        annees = [d['annee'] for d in donnees]
        ventes = [d['ventes'] for d in donnees]
        achats = [d['achats'] for d in donnees]
        paiements = [d['paiements'] for d in donnees]
        depenses = [d['dépenses'] for d in donnees]
        salaires = [d['salaires'] for d in donnees]

        ax = self.situation_canvas.figure.add_subplot(111) 

        self.situation_canvas.figure.set_facecolor((0, 0, 0, 0.1))
        ax.clear()
        ax.set_facecolor((0, 0, 0, 0.1))

        # Largeur des barres
        bar_width = 0.115
        x = range(len(annees))

        # Tracer les différentes catégories

        ax.bar(x, paiements, bar_width, label='Paiements', color='orange')
        ax.bar(x , ventes, bar_width, bottom=paiements,label='Ventes', color='blue')

        ax.bar([i - bar_width for i in x], achats, bar_width, label='Achats', color='green')
        ax.bar([i - bar_width for i in x], depenses, bar_width, bottom=achats, label='Dépenses', color='red')
        s=np.array(depenses)+np.array(achats)
        ax.bar([i - bar_width for i in x], salaires, bar_width, bottom=s,label='Salaires', color='purple')

        ax.set_title("Évolution des Comptes par Année",color='white', fontsize=14)
        ax.set_xlabel("Années",color='white', fontsize=12)
        ax.set_ylabel("Valeurs",color='white', fontsize=12)
        ax.set_xticks(x)
        ax.tick_params(axis='x', colors='white')  # Ticks de l'axe X en noir
        ax.tick_params(axis='y', colors='white')
        ax.set_xticklabels(annees)
        ax.legend()

        self.situation_canvas.figure.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.2)
        for label in ax.texts:
            label.set_color('white')
            label.set_fontsize(14)

        # Sauvegarder l'image
        self.situation_canvas.draw()
    


    
    
    def plot_situation_graph2(self):
        

        """Affiche le pourcentage des situations pour le mois actuel"""
        donnees = recuperer_compta_each_month()
        annees = [d['mois'] for d in donnees]
        ventes = [d['ventes'] for d in donnees]
        achats = [d['achats'] for d in donnees]
        paiements = [d['paiments'] for d in donnees]
        depenses = [d['dépenses'] for d in donnees]
        salaires = [d['salaires'] for d in donnees]

        ax = self.situation_canvas2.figure.add_subplot(111) 

        self.situation_canvas2.figure.set_facecolor((0, 0, 0, 0.1))
        ax.clear()
        ax.set_facecolor((0, 0, 0, 0.1))

        # Largeur des barres
        bar_width = 0.15
        x = range(len(annees))

        # Tracer les différentes catégories

        ax.bar(x, paiements, bar_width, label='Paiements', color='#9ACD32', alpha=0.75) 
        ax.bar(x, ventes, bar_width, bottom=paiements, label='Ventes', color='#98fb98', alpha=0.75)



        ax.bar([i - bar_width for i in x], achats, bar_width, label='Achats', color='#FF6347', alpha=0.75)
        ax.bar([i - bar_width for i in x], depenses, bar_width, bottom=achats, label='Dépenses', color='red', alpha=0.75)
        s=np.array(depenses)+np.array(achats)
        ax.bar([i -  bar_width for i in x], salaires, bar_width, bottom=s,label='Salaires', color='#FF4500', alpha=0.75)

        ax.set_title("Évolution des Comptes par mois",color='white', fontsize=14)
        ax.set_xlabel("Mois", color='white',fontsize=12 )
        ax.set_ylabel("Valeurs", color='white',fontsize=12 )
        ax.set_xticks(x)
        ax.set_xticklabels(annees, rotation=90)
        ax.tick_params(axis='x', colors='white')  # Ticks de l'axe X en noir
        ax.tick_params(axis='y', colors='white')
        ax.legend()
        self.situation_canvas2.figure.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.25)
        for label in ax.texts:
            label.set_color('white')
            label.set_fontsize(14)

        # Sauvegarder l'image
        self.situation_canvas2.draw()
        
        

   
    def plot_revenue_graph(self): 
        """Affiche le pourcentage des situations pour le mois actuel"""
        date_month = datetime.now().strftime('%Y-%m')
        month_keys = comptabilite_par_mois(date_month)
        date_year = datetime.now().strftime('%Y')
        year_keys = comptabilite_par_annee(date_year)
         
        self.info_layout = QVBoxLayout()


        


        self.revenue_canvas_month = QWidget()
        self.revenue_canvas_month.setObjectName("dashbord_graphe_stat") 
        self.info_layout_month = QVBoxLayout(self.revenue_canvas_month)


        
        # Ventes du mois
        row2_layout = QHBoxLayout()
        el_paiment = QLabel(" Mois : ")
        self.aiment_input_month = QLabel( str(date_month))
        
        
        row2_layout.addWidget(el_paiment)
        row2_layout.addWidget(self.aiment_input_month )

        label_pay_salarial = QLabel("Salaires mensuelles :")
        self.pay_salarial_input = QLabel(str(month_keys['salaires'])+ " Dhs")

        
        row2_layout.addWidget(label_pay_salarial)
        row2_layout.addWidget(self.pay_salarial_input)
        
 
        self.info_layout_month.addLayout(row2_layout)

 

        # Ventes du mois
        row3_layout = QHBoxLayout()
        label_ventes = QLabel("Ventes mensuelles :")
        self.ventes_input = QLabel(str(month_keys['ventes'])+ " Dhs")
        row3_layout.addWidget(label_ventes)
        row3_layout.addWidget(self.ventes_input)

        label_achats = QLabel("Achas mensuelles :")
        self.achats_input = QLabel(str(month_keys['achats'])+ " Dhs")
        row3_layout.addWidget(label_achats)
        row3_layout.addWidget(self.achats_input)
        self.info_layout_month.addLayout(row3_layout)
 

        # Pay salarial du mois
        row5_layout = QHBoxLayout()
        label_paiment = QLabel("Paiement mensuels :")
        self.paiment_input_month = QLabel(str(month_keys['paiments'])+ " Dhs")
        row5_layout.addWidget(label_paiment)
        row5_layout.addWidget(self.paiment_input_month) 




        

        
        label_depense = QLabel("Dépenses mensuelles :")
        self.depense_input = QLabel(str(month_keys['dépenses'])+ " Dhs")
        row5_layout.addWidget(label_depense)
        row5_layout.addWidget(self.depense_input)
        self.info_layout_month.addLayout(row5_layout)
        total_r = month_keys['ventes']+month_keys['paiments']
        total_d = month_keys['achats']+month_keys['dépenses']+month_keys['salaires']

        # Pay salarial du mois
        row6_layout = QHBoxLayout()
        label_rev_salarial = QLabel("Total des revenus monseils :")
        self.rev_salarial_input = QLabel(str(total_r)+ " Dhs")
        row6_layout.addWidget(label_rev_salarial)
        row6_layout.addWidget(self.rev_salarial_input)
        label_depensett = QLabel("Total des dépenses monseils :")
        self.depense_inputtt = QLabel(str(total_d)+ " Dhs")
        row6_layout.addWidget(label_depensett)
        row6_layout.addWidget(self.depense_inputtt)
        self.info_layout_month.addLayout(row6_layout)




        self.info_layout.addWidget(self.revenue_canvas_month )




        self.revenue_canvas_year = QWidget()
        self.revenue_canvas_year.setObjectName("dashbord_graphe_stat") 


        info_layout_year = QVBoxLayout(self.revenue_canvas_year)


         


        # Achats de l'année
        row4_layout = QHBoxLayout()

        lab_annee = QLabel("Année :")
        self.annee_input = QLabel(str(date_year))
        row4_layout.addWidget(lab_annee)
        row4_layout.addWidget(self.annee_input )
        
        label_pay_salarial_annee = QLabel("Salaires annuels :")
        self.pay_salarial_annee_input = QLabel(str(year_keys['salaires'])+ " Dhs")
        row4_layout.addWidget(label_pay_salarial_annee)
        row4_layout.addWidget(self.pay_salarial_annee_input)
        info_layout_year.addLayout(row4_layout) 
        


        # Paiment de l'année
        row2_layout = QHBoxLayout()
        label_ventes_annee = QLabel("Ventes annuels :")
        self.ventes_annee_input = QLabel(str(year_keys['paiements']) +" Dhs") 
        row2_layout.addWidget(label_ventes_annee)
        row2_layout.addWidget(self.ventes_annee_input)  

        label_achats_annee = QLabel("Achats annuels :")
        self.achats_annee_input = QLabel(str(year_keys['achats'])+ " Dhs")
        row2_layout.addWidget(label_achats_annee)
        row2_layout.addWidget(self.achats_annee_input)


        info_layout_year.addLayout(row2_layout)
 

        
        # Dépense de l'année
        row6_layout = QHBoxLayout()
        label_paiment_annee = QLabel("Paiment annuels :")
        self.paiment_annee_input = QLabel(str(year_keys['paiements'])+ " Dhs") 
        row6_layout.addWidget(label_paiment_annee)
        row6_layout.addWidget(self.paiment_annee_input)



        label_depense_annee = QLabel("Dépense annuels:")
        self.depense_annee_input = QLabel(str(year_keys['dépenses'])+ " Dhs")
        row6_layout.addWidget(label_depense_annee)
        row6_layout.addWidget(self.depense_annee_input)
        info_layout_year.addLayout(row6_layout)

        total_r_y = year_keys['ventes']+year_keys['paiements']
        total_d_y = year_keys['achats']+year_keys['dépenses']+year_keys['salaires']




         # Pay salarial du mois
        row7_layout = QHBoxLayout()
        label_rev_salarial_year = QLabel("Total des revenues annuels:")
        self.rev_salarial_input_year = QLabel(str(total_r_y)+" Dhs")
        row7_layout.addWidget(label_rev_salarial_year)
        row7_layout.addWidget(self.rev_salarial_input_year)
        label_depensett_year = QLabel("Total des dépenses annuels :")
        self.depense_inputtt_year = QLabel(str(total_d_y)+" Dhs")
        row7_layout.addWidget(label_depensett_year)
        row7_layout.addWidget(self.depense_inputtt_year)
        info_layout_year.addLayout(row7_layout)
        self.info_layout.addWidget(self.revenue_canvas_year )

        



        self.revenue_canvas.setLayout(self.info_layout) 
    


    