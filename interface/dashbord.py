from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import *
from .main_interface import MainInterface
import matplotlib.pyplot as plt
from PyQt5.QtGui import QColor, QFont
import numpy as np

class Dashbord():
    def __init__(self, main_inter): 
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

        titre_table = QLabel('Membres dans une situation irrégulière ')
        titre_table.setObjectName("titre_table")
        layout.addWidget(titre_table)

        # Search bar for filtering
        self.search_bar = QLineEdit(self.main_inter)
        self.search_bar.setPlaceholderText("Chercher par 'Nom'...")
        self.search_bar.textChanged.connect(self.filter_table)  # Trigger filter when text changes
        layout.addWidget(self.search_bar)

        self.tableWidget = QTableWidget()
        self.populate_table()  
        layout.addWidget(self.tableWidget)
        
        self.main_inter.content_layout.addWidget(self.dashbord_widget) 

    def filter_table(self):
        #if not self.all_data:
        #    self.load_all_data()
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
        ax.set_title(f"Pourcentage de la situation du mois : {date}", color='white',  fontsize=16) 
        ax.tick_params(axis='both', labelcolor='purple')
        for label in ax.texts:
            label.set_color('white')
            label.set_fontsize(14)
        
        self.situation_canvas.draw()

    def plot_revenue_graph(self):
        """Affiche les revenus mensuels pour l'année en cours avec le total annuel"""

        """Affiche le pourcentage des situations pour le mois actuel"""
        donnees = recuperer_compta_each_month()
        annees = [d['mois'] for d in donnees]
        ventes = [d['ventes'] for d in donnees]
        achats = [d['achats'] for d in donnees]
        paiements = [d['paiments'] for d in donnees]
        depenses = [d['dépenses'] for d in donnees]
        salaires = [d['salaires'] for d in donnees]

        ax = self.revenue_canvas.figure.add_subplot(111) 

        self.revenue_canvas.figure.set_facecolor((0, 0, 0, 0.1))
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
        ax.legend()#(facecolor='none',labelcolor='white', edgecolor='none')
        self.revenue_canvas.figure.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.25)
        for label in ax.texts:
            label.set_color('white')
            label.set_fontsize(14)

        # Sauvegarder l'image
        self.revenue_canvas.draw() 

 

    def populate_table(self):
        """Charge les adhérents dans le tableau avec des fonctionnalités supplémentaires"""
        # Connexion à la base de données SQLite
        
        self.adherents = fetch_data_Non_df() 
        
        # Effacer les anciennes lignes dans le tableau
        self.tableWidget.setColumnCount(6)  # Nombre de colonnes affichées
        self.tableWidget.setHorizontalHeaderLabels([
            'Nom', 'Prénom', 'Email', 'Téléphone', 'Situation', 'Action'
        ])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.tableWidget.setRowCount(10)

        #self.all_data = False  # Nombre de lignes visibles à chaque fois 
        #self.tableWidget.verticalScrollBar().valueChanged.connect(self.on_scroll)

        self.load_table()  
        # Connecter l'événement de clic pour traiter un adhérent
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)
    
    def load_all_data(self):

        self.adherents = fetch_data_Non_all() 
        self.load_table()

        self.all_data = True

    def load_table(self): 
        
        # Ajouter les adhérents dans le tableau
        for  row_index, adherent in self.adherents.iterrows():
            self.tableWidget.insertRow(row_index)

            # Ajouter les données dans les colonnes respectives
            for col_index, data in enumerate(adherent[1:6]):  # Exclure 'id' pour l'affichage
                
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_index, col_index, item)
                

                # Ajouter une couleur verte à la cellule de la colonne Email
                if col_index == 4 :  # 3e colonne (Email)
                    item = QTableWidgetItem(str('Paiement non effectué'))
                    self.tableWidget.setItem(row_index, col_index, item)
                    #item.setBackground(QColor(255, 0, 0))  # Vert 
                else:
                    item = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row_index, col_index, item)
            
                    
            # Ajouter un lien cliquable dans la colonne Action
            action_item = QTableWidgetItem("Gestion de l'hadérent")
            action_item.setForeground(QColor("white"))
            action_item.setTextAlignment(Qt.AlignCenter)
            action_item.setData(Qt.UserRole, adherent[0])  # Stocker l'ID de l'adhérent pour le traitement
            action_item.setBackground(QColor(0, 0, 255))  # Vert
            self.tableWidget.setItem(row_index, 5, action_item) 
        
    
  
    def on_scroll(self, value):
        """
        Appelée à chaque fois que l'utilisateur fait défiler.
        """
        max_scroll = self.tableWidget.verticalScrollBar().maximum()

        # Si la barre de défilement est presque en bas, charger plus de données
        if value == max_scroll and not self.all_data:
            self.load_all_data()
            
    
    def on_cell_clicked(self, row, column): 
        # Si la colonne 12 (Action) est cliquée
        if column == 5:
            if  self.tableWidget.item(row, column) is not None:

                self.main_inter.clear_content_frame()
                adherent_id = self.tableWidget.item(row, column).data(Qt.UserRole) 
                from .profile_interface import Profile
                self.main_interface = Profile(adherent_id, self.main_inter)
                


    