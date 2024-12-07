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
        self.table_widget.setObjectName("dashbord_widget") 

        layout = QVBoxLayout(self.table_widget)

        titre_table = QLabel('Liste des adhérents : ')
        titre_table.setObjectName("titre_table")
        layout.addWidget(titre_table)


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

        self.modification = QPushButton("Télécharger la base de données")
        self.modification.clicked.connect(self.telecharger_dataset)
        layout.addWidget(self.modification)
        self.modification.setObjectName('button_vert')
        

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
         
        adherents = fetch_data_with_last()

        # Effacer les anciennes lignes dans le tableau
        self.tableWidget.setRowCount(0)

        # Ajouter les adhérents dans le tableau
        for row_index, adherent in adherents.iterrows():
            self.tableWidget.insertRow(row_index)

            # Ajouter les données dans les colonnes respectives
            for col_index, data in enumerate(adherent[1:-2]):  # Exclure 'id' pour l'affichage
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_index, col_index, item)
                

                # Ajouter une couleur verte à la cellule de la colonne Email
                if col_index == 4 :  # 3e colonne (Email)
                    date_to_compare = adherent[7] 
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
            action_item.setForeground(QColor('white'))
            action_item.setTextAlignment(Qt.AlignCenter)
            action_item.setData(Qt.UserRole, adherent[0])  # Stocker l'ID de l'adhérent pour le traitement
            action_item.setBackground(QColor(0, 0, 255))  # Vert
            self.tableWidget.setItem(row_index, 5, action_item)
        # Connecter l'événement de clic pour traiter un adhérent
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)



    



 
    def telecharger_dataset(self):
        # Simuler un téléchargement ou choisir un emplacement
        options = QFileDialog.Options()
        save_path, _ = QFileDialog.getSaveFileName(
            self.main_inter,
            "Enregistrer sous",
            os.path.expanduser("~/Téléchargements/output.xlsx"),
            "Tous les fichiers (*.*)",
            options=options,
        )
        if save_path: 
            write_to_excel(save_path) 
            QMessageBox.information(self.main_inter, f"Fichier enregistré à : {save_path}",f"Fichier enregistré à : {save_path}")

    def on_cell_clicked(self, row, column): 
        # Si la colonne 12 (Action) est cliquée
        if column == 5:
            self.main_inter.clear_content_frame()
            adherent_id = self.tableWidget.item(row, column).data(Qt.UserRole)
            from .profile_interface import Profile
            self.main_interface = Profile(adherent_id, self.main_inter)
            
 