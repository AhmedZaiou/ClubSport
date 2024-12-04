from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import *
from .main_interface import MainInterface


class Gestion_adherents():
    def __init__(self,main_inter): 
        self.main_inter = main_inter
        self.show_table()
    

    def show_table(self):
        self.main_inter.clear_content_frame()
        self.table_widget = QWidget()
        self.table_widget.setObjectName("tableWidget") 

        layout = QVBoxLayout(self.table_widget)


        # Search bar for filtering
        self.search_bar = QLineEdit(self.main_inter)
        self.search_bar.setPlaceholderText("Search by 'Nom'...")
        self.search_bar.textChanged.connect(self.filter_table)  # Trigger filter when text changes
        layout.addWidget(self.search_bar)

        # Créer le tableau pour afficher les adhérents
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(6)  # Nombre de colonnes affichées
        self.tableWidget.setHorizontalHeaderLabels([
            'Nom', 'Prénom', 'Email', 'Téléphone', 'Situation', 'Action'
        ])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Ajouter le tableau au layout
        layout.addWidget(self.tableWidget)

        # Créer un bouton pour charger les adhérents 
        self.load_adherents() 

        self.main_inter.content_layout.addWidget(self.table_widget)
    
    
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

    def load_adherents(self):
        # Connexion à la base de données SQLite
         
        adherents = fetch_data_all()

        # Effacer les anciennes lignes dans le tableau
        self.tableWidget.setRowCount(0)

        # Ajouter les adhérents dans le tableau
        for row_index, adherent in enumerate(adherents):
            self.tableWidget.insertRow(row_index)

            # Ajouter les données dans les colonnes respectives
            for col_index, data in enumerate(adherent[1:]):  # Exclure 'id' pour l'affichage
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_index, col_index, item)
                

                # Ajouter une couleur verte à la cellule de la colonne Email
                if col_index == 4 :  # 3e colonne (Email)
                    last_paiment = recuperer_last_payment(adherent[0])
                    # Define the date to compare
                    date_to_compare = datetime.strptime(last_paiment, "%Y-%m-%d") 
                    current_date = datetime.now() 
                    if date_to_compare.year == current_date.year and date_to_compare.month == current_date.month:
                        item = QTableWidgetItem(str('Paiement effectué'))
                        self.tableWidget.setItem(row_index, col_index, item)
                    else:
                        item = QTableWidgetItem(str('Paiement non effectué'))
                        self.tableWidget.setItem(row_index, col_index, item)
                        item.setBackground(QColor(255, 0, 0))
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
            
 