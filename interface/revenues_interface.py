from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import * 
from .main_interface import MainInterface
from matplotlib.ticker import FuncFormatter
 

class Revenues(MainInterface):
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
        self.revenue_canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.revenue_canvas.setObjectName("dashbord_graphe")
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
        nbr_adh,nbr_pyment = recuperer_porcentage_paiment() 

        if nbr_adh ==0 :
            nbr_adh=1
        ax = self.situation_canvas.figure.add_subplot(111)
        self.situation_canvas.figure.set_facecolor((0, 0, 0, 0.1))
        ax.clear()
        ax.set_facecolor('#ffffff')
        ax.pie(
            [nbr_pyment,nbr_adh - nbr_pyment], 
            labels=["Paiement effectué", "Paiement non effectué"], 
            autopct="%1.1f%%", 
            startangle=90, 
            colors=["lightgreen", "firebrick"]
        ) 
        date = datetime.now().strftime("%Y-%m-%d")
        ax.set_title(f"Pourcentage de la situation du mois : ({date})", color='white',  fontsize=16) 
        ax.tick_params(axis='both', labelcolor='purple')
        for label in ax.texts:
            label.set_color('white')
            label.set_fontsize(14)
        
        self.situation_canvas.draw()
    
    def plot_situation_graph2(self):
        
        
        # Filtrer les données pour l'année en cours
        
        revenue_by_month = recuperer_all_paiment()
        ax = self.situation_canvas2.figure.add_subplot(111)
        self.situation_canvas2.figure.set_facecolor((0, 0, 0, 0.1))
        ax.clear()
        ax.set_facecolor((0, 0, 0, 0.1))
        revenue_by_month.plot(kind="line", ax=ax, color="lightgreen", alpha=0.75)
        ax.set_title(f"Revenus Mensuels () - Total :  Dhs",  color='white',  fontsize=16) 
        ax.set_ylabel("Revenus (Dhs)",  color='white',  fontsize=16) 
        ax.tick_params(axis='x', colors='white')  # Ticks de l'axe X en noir
        ax.tick_params(axis='y', colors='white')
        formatter = FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", " "))
        ax.yaxis.set_major_formatter(formatter)

        self.situation_canvas2.figure.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.25)
        for label in ax.texts:
            label.set_color('white')
            label.set_fontsize(14)
        self.situation_canvas2.draw()

   


    def plot_revenue_graph(self):
        """Affiche les revenus mensuels pour l'année en cours avec le total annuel"""
         
        
        # Filtrer les données pour l'année en cours
        current_year = datetime.now().year 
        data, total_revenue = recuperer_stat_paiment()
        revenue_by_month = pd.Series(data) 
        ax = self.revenue_canvas.figure.add_subplot(111)
        self.revenue_canvas.figure.set_facecolor((0, 0, 0, 0.1))
        ax.clear()
        ax.set_facecolor((0, 0, 0, 0.1))
        revenue_by_month.plot(kind="bar", ax=ax, color="lightgreen", alpha=0.75)
        ax.set_title(f"Revenus Mensuels ({current_year}) - Total : {total_revenue} Dhs",  color='white',  fontsize=16) 
        ax.set_ylabel("Revenus (Dhs)",  color='white',  fontsize=16) 
        ax.tick_params(axis='x', colors='white')  # Ticks de l'axe X en noir
        ax.tick_params(axis='y', colors='white')

        self.revenue_canvas.figure.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.25)
        for label in ax.texts:
            label.set_color('white')
            label.set_fontsize(14)
        self.revenue_canvas.draw()

    def populate_table(self):
        pass 
