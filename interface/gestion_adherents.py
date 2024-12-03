from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import *
from .main_interface import MainInterface


class Gestion_adherents(MainInterface):
    def __init__(self):
        super().__init__()
        self.show_table()
    

    def show_table(self):
        self.clear_content_frame()
        self.table_widget = QWidget()
        self.table_widget.setObjectName("tableWidget") 

        layout = QVBoxLayout(self.table_widget)

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

        self.content_layout.addWidget(self.table_widget)
    


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
                if col_index == 4 and data == 'Paiement non effectué':  # 3e colonne (Email)
                    item.setBackground(QColor(255, 0, 0))  # Vert

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
            self.clear_content_frame()
            adherent_id = self.tableWidget.item(row, column).data(Qt.UserRole)
            from .profile_interface import Profile
            self.main_interface = Profile(adherent_id)
            self.main_interface.show()
            self.close()

    def show_dashboard(self):
        from .dashbord import Dashbord
        self.main_interface = Dashbord()
        self.main_interface.show()
        self.close()
    def show_payments(self):
        from .payment import Payment
        self.main_interface = Payment()
        self.main_interface.show()
        self.close()
    def show_revenues(self):
        from .revenues_interface import Revenues
        self.main_interface = Revenues()
        self.main_interface.show()
        self.close()
    def show_due_dates(self):
        self.main_interface = Gestion_adherents()
        self.main_interface.show()
        self.close()
    def ajouter_adh(self):
        from .ajouter_adherent import AjouterAfh
        self.main_interface = AjouterAfh()
        self.main_interface.show()
        self.close()
        
    
    