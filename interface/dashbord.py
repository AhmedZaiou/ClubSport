from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import *
from .main_interface import MainInterface
import matplotlib.pyplot as plt
from PyQt5.QtGui import QColor, QFont


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
        self.load_all_table()
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
            colors=["skyblue", "firebrick"]
        ) 
        date = datetime.now().strftime("%Y-%m-%d")
        ax.set_title(f"Pourcentage de la situation du mois : ({date})", color='white',  fontsize=16) 
        ax.tick_params(axis='both', labelcolor='purple')
        for label in ax.texts:
            label.set_color('white')
            label.set_fontsize(14)
        
        self.situation_canvas.draw()

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
        revenue_by_month.plot(kind="bar", ax=ax, color="#00C000", alpha=0.75)
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
        """Charge les adhérents dans le tableau avec des fonctionnalités supplémentaires"""
        # Connexion à la base de données SQLite
        
        self.adherents = fetch_data_Non() 
        
        # Effacer les anciennes lignes dans le tableau
        self.tableWidget.setColumnCount(6)  # Nombre de colonnes affichées
        self.tableWidget.setHorizontalHeaderLabels([
            'Nom', 'Prénom', 'Email', 'Téléphone', 'Situation', 'Action'
        ])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.tableWidget.setRowCount(10)

        self.rows_shown = 20  # Nombre de lignes visibles à chaque fois
        self.current_row = 0
        self.tableWidget.verticalScrollBar().valueChanged.connect(self.on_scroll)


        self.load_table() 

        # Connecter l'événement de clic pour traiter un adhérent
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)

    def load_all_table(self):

        # Ajouter les adhérents dans le tableau
        for  row_index in range(self.current_row, len(self.adherents)):
            #row_index, adherent in enumerate(self.adherents):
            self.tableWidget.insertRow(row_index)

            # Ajouter les données dans les colonnes respectives
            for col_index, data in enumerate(self.adherents[row_index][1:]):  # Exclure 'id' pour l'affichage
                
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
            action_item.setData(Qt.UserRole, self.adherents[row_index][0])  # Stocker l'ID de l'adhérent pour le traitement
            action_item.setBackground(QColor(0, 0, 255))  # Vert
            self.tableWidget.setItem(row_index, 5, action_item)
        self.current_row += len(self.adherents)
   
    def load_table(self):

        # Ajouter les adhérents dans le tableau
        for  row_index in range(self.current_row, min(self.current_row + self.rows_shown, len(self.adherents))):
            #row_index, adherent in enumerate(self.adherents):
            self.tableWidget.insertRow(row_index)

            # Ajouter les données dans les colonnes respectives
            for col_index, data in enumerate(self.adherents[row_index][1:]):  # Exclure 'id' pour l'affichage
                
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
            action_item.setData(Qt.UserRole, self.adherents[row_index][0])  # Stocker l'ID de l'adhérent pour le traitement
            action_item.setBackground(QColor(0, 0, 255))  # Vert
            self.tableWidget.setItem(row_index, 5, action_item)
        self.current_row += self.rows_shown
    def on_scroll(self, value):
        """
        Appelée à chaque fois que l'utilisateur fait défiler.
        """
        max_scroll = self.tableWidget.verticalScrollBar().maximum()

        # Si la barre de défilement est presque en bas, charger plus de données
        if value == max_scroll:
            self.load_table()
    
    def on_cell_clicked(self, row, column): 
        # Si la colonne 12 (Action) est cliquée
        if column == 5:
            self.main_inter.clear_content_frame()
            adherent_id = self.tableWidget.item(row, column).data(Qt.UserRole)
            from .profile_interface import Profile
            self.main_interface = Profile(adherent_id, self.main_inter)
            


    