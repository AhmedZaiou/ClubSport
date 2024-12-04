from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import *
from .main_interface import MainInterface


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
        self.plot_situation_graph()
        graphs_layout.addWidget(self.situation_canvas)
        
        # Graphique 2 : Revenus mensuels pour cette année
        self.revenue_canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.plot_revenue_graph()
        graphs_layout.addWidget(self.revenue_canvas)
        
        # Ajout des graphiques au layout principal
        layout.addLayout(graphs_layout)
        
        # Tableau pour afficher les adhérents avec situation = NON
        # Search bar for filtering
        self.search_bar = QLineEdit(self.main_inter)
        self.search_bar.setPlaceholderText("Search by 'Nom'...")
        self.search_bar.textChanged.connect(self.filter_table)  # Trigger filter when text changes
        layout.addWidget(self.search_bar)

        self.tableWidget = QTableWidget()
        self.populate_table()  
        layout.addWidget(self.tableWidget)
        
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
        
         
        situation_counts = {"Paiment effectuer ": nbr_pyment, "Paiment non effectuer ": nbr_adh - nbr_pyment }
        ax = self.situation_canvas.figure.add_subplot(111)
        ax.clear()
        ax.pie(
            [nbr_pyment,nbr_adh - nbr_pyment], 
            labels=["Paiment effectuer ", "Paiment non effectuer "], 
            autopct="%1.1f%%", 
            startangle=90, 
            colors=["skyblue", "orange"]
        ) 
        date = datetime.now().strftime("%Y-%m-%d")
        ax.set_title(f"Pourcentage des Situations ({date})") 
        
        self.situation_canvas.draw()

    def plot_revenue_graph(self):
        """Affiche les revenus mensuels pour l'année en cours avec le total annuel"""
         
        
        # Filtrer les données pour l'année en cours
        current_year = datetime.now().year 
        data, total_revenue = recuperer_stat_paiment()
        revenue_by_month = pd.Series(data) 
        ax = self.revenue_canvas.figure.add_subplot(111)
        ax.clear()
        revenue_by_month.plot(kind="bar", ax=ax, color="green", alpha=0.75)
        ax.set_title(f"Revenus Mensuels ({current_year}) - Total : {total_revenue} €")
        ax.set_xlabel("Mois")
        ax.set_ylabel("Revenus (€)") 
        self.revenue_canvas.draw()

    def populate_table(self):
        """Charge les adhérents dans le tableau avec des fonctionnalités supplémentaires"""
        # Connexion à la base de données SQLite
        
        adherents = fetch_data_Non() 
        
        # Effacer les anciennes lignes dans le tableau
        self.tableWidget.setColumnCount(6)  # Nombre de colonnes affichées
        self.tableWidget.setHorizontalHeaderLabels([
            'Nom', 'Prénom', 'Email', 'Téléphone', 'Situation', 'Action'
        ])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.tableWidget.setRowCount(10)


        # Ajouter les adhérents dans le tableau
        for row_index, adherent in enumerate(adherents):
            self.tableWidget.insertRow(row_index)

            # Ajouter les données dans les colonnes respectives
            for col_index, data in enumerate(adherent[1:]):  # Exclure 'id' pour l'affichage
                
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_index, col_index, item)
                

                # Ajouter une couleur verte à la cellule de la colonne Email
                if col_index == 4 :  # 3e colonne (Email)
                    item = QTableWidgetItem(str('Paiement non effectué'))
                    self.tableWidget.setItem(row_index, col_index, item)
                    item.setBackground(QColor(255, 0, 0))  # Vert 
                else:
                    item = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row_index, col_index, item)


            # Ajouter un lien cliquable dans la colonne Action
            action_item = QTableWidgetItem("Traiter")
            action_item.setForeground(Qt.blue)
            action_item.setTextAlignment(Qt.AlignCenter)
            action_item.setData(Qt.UserRole, adherent[0])  # Stocker l'ID de l'adhérent pour le traitement
            self.tableWidget.setItem(row_index, 5, action_item)

        

        # Connecter l'événement de clic pour traiter un adhérent
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)

    def on_cell_clicked(self, row, column): 
        # Si la colonne 12 (Action) est cliquée
        if column == 5:
            self.main_inter.clear_content_frame()
            adherent_id = self.tableWidget.item(row, column).data(Qt.UserRole)
            from .profile_interface import Profile
            self.main_interface = Profile(adherent_id, self.main_inter)
            


    