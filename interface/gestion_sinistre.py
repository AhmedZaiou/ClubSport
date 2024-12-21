from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import * 
from .main_interface import MainInterface

import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from tempfile import NamedTemporaryFile

from matplotlib.ticker import FuncFormatter

 

class Sinistre( ):
    def __init__(self,main_inter, id, name): 
       self.main_inter = main_inter
       self.id_adherent = id
       self.name_adherent = name
       self.show_dashboard_inter()
    
    def show_dashboard_inter(self):
        self.main_inter.clear_content_frame()

        self.dashbord_widget = QWidget()
        self.dashbord_widget.setObjectName("dashbord_widget")

        # Layout principal
        layout = QVBoxLayout(self.dashbord_widget)
        title_layout = QHBoxLayout()
        self.title1 = QLabel(f"Ajouter un sinistre pour {self.name_adherent}")
        self.title1.setObjectName("FormulaireWidgetstock1") 
        self.title1.setAlignment(Qt.AlignCenter)
        title_layout.addWidget(self.title1 ) 
        
        
        
        # Layouts horizontaux pour les graphiques
        graphs_layout = QHBoxLayout()
 
        
        if self.id_adherent is not None:  
            self.form_widget = QWidget()
            self.form_widget.setObjectName("FormulaireWidgetstock")  
            self.add_formulaire()

            graphs_layout.addWidget(self.form_widget)



  
 
        
  
        
        # Ajout des graphiques au layout principal
        
        
        # Tableau pour afficher les adhérents avec situation = NON

        titre_table = QLabel('Liste des sinistres :')
        titre_table.setObjectName("titre_table")
        layout.addWidget(titre_table)

        # Search bar for filtering
        self.search_bar = QLineEdit(self.main_inter)
        self.search_bar.setPlaceholderText("Chercher par 'Nom adhérent'...")
        self.search_bar.textChanged.connect(self.filter_table)  # Trigger filter when text changes
        layout.addWidget(self.search_bar)

        self.tableWidget = QTableWidget()
        self.srock_table()  
        layout.addWidget(self.tableWidget)
        layout.addLayout(title_layout)
        layout.addLayout(graphs_layout)

        
 
        self.main_inter.content_layout.addWidget(self.dashbord_widget) 
    
    def add_formulaire(self):
        form_layout = QFormLayout(self.form_widget)


        # Nom du sinistré, Date de l'accident, Nature de l'accident, Gravité de l'accident
        self.nom_label = QLabel("Nom du sinistré :")
        self.nom_input = QLineEdit()
        
        self.date_label = QLabel("Date de l'accident :")
        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate()) 
        
        self.nature_label = QLabel("Nature de l'accident :")
        self.nature_input = QLineEdit()
        
        self.gravite_label = QLabel("Gravité de l'accident :")
        self.gravite_input = QComboBox()
        self.gravite_input.addItems(["Mineur", "Modéré", "Grave"])
         
        # Soins médicaux prodigués, Hospitalisation requise
        self.soins_label = QLabel("Soins médicaux prodigués :")
        self.soins_input = QLineEdit()

        self.hospitalisation_label = QLabel("Hospitalisation requise ? :")
        self.hospitalisation_input = QComboBox()
        self.hospitalisation_input.addItems(["Oui", "Non"])
         
        # Rapport médical, Date et durée d'indisponibilité
        self.rapport_label = QLabel("Rapport médical :")
        self.rapport_input = QLineEdit()

        self.indispo_label = QLabel("Date et durée d'indisponibilité :")
        self.indispo_input = QLineEdit()
         
        # Rapport de témoin(s), Mesures prises
        self.temoins_label = QLabel("Rapport de témoin(s) :")
        self.temoins_input = QLineEdit()

        self.mesures_label = QLabel("Mesures prises :")
        self.mesures_input = QLineEdit()
         
        # Boutons
        self.submit_button = QPushButton("Soumettre")
        self.submit_button.clicked.connect(self.submitForm) 
        self.submit_button.setObjectName('button_vert')




        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_button) 




        row_layout_1 = QHBoxLayout() 
        row_layout_1.addWidget(self.nom_input) 
        row_layout_1.addWidget(self.date_label)
        row_layout_1.addWidget(self.date_input)
        row_layout_1.addWidget(self.nature_label)
        row_layout_1.addWidget(self.nature_input)
        form_layout.addRow(self.nom_label, row_layout_1)

        row_layout_2 = QHBoxLayout()
        row_layout_2.addWidget(self.gravite_input)
        row_layout_2.addWidget(self.soins_label) 
        row_layout_2.addWidget(self.soins_input)
        row_layout_2.addWidget(self.hospitalisation_label)
        row_layout_2.addWidget(self.hospitalisation_input) 
        form_layout.addRow(self.gravite_label, row_layout_2)

        row_layout_3 = QHBoxLayout()
        row_layout_3.addWidget(self.rapport_input)
        row_layout_3.addWidget(self.indispo_label) 
        row_layout_3.addWidget(self.indispo_input)
        row_layout_3.addWidget(self.temoins_label)
        row_layout_3.addWidget(self.temoins_input) 
        form_layout.addRow(self.rapport_label, row_layout_3)

        row_layout_4 = QHBoxLayout()
        row_layout_4.addWidget(self.mesures_input)
        row_layout_4.addWidget(QLabel("")) 
        row_layout_4.addWidget(self.submit_button) 
        row_layout_4.addWidget(QLabel(" "))  
        form_layout.addRow(self.mesures_label, row_layout_4)

 


    def submitForm(self):
        pass
    def resetForm(self):
        pass
     
 


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

 
 
    def srock_table(self):
        """Charge les adhérents dans le tableau avec des fonctionnalités supplémentaires"""
        # Connexion à la base de données SQLite
        
        self.sinistres = recuperer_sinistre()
        
        # Effacer les anciennes lignes dans le tableau
        self.tableWidget.setColumnCount(12)  # Nombre de colonnes affichées
        self.tableWidget.setHorizontalHeaderLabels([
         "Nom adhérent","Nom sinistre", "Date", "Nature", "Gravité", "Soins", "Hospitalisation", "Rapport", "Indispo", "Témoins", "Mesures", "Action"
        ])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #self.all_data = False  # Nombre de lignes visibles à chaque fois 
        #self.tableWidget.verticalScrollBar().valueChanged.connect(self.on_scroll)

        # Ajouter les adhérents dans le tableau
        for  row_index, adherent in enumerate(self.sinistres):
            self.tableWidget.insertRow(row_index)
            # Ajouter les données dans les colonnes respectives 
            for col_index, data in enumerate(adherent[2:]):  # Exclure 'id' pour l'affichage

                
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_index, col_index, item) 



            # Ajouter un lien cliquable dans la colonne Action
            action_item = QTableWidgetItem("Profil")
            action_item.setForeground(QColor('white'))
            action_item.setTextAlignment(Qt.AlignCenter)
            action_item.setData(Qt.UserRole, adherent[0])  # Stocker l'ID de l'adhérent pour le traitement
            action_item.setBackground(QColor(0, 0, 255))  # Vert
            self.tableWidget.setItem(row_index, 11, action_item) 

        self.tableWidget.cellClicked.connect(self.on_cell_clicked_vente)
    
     

    def on_cell_clicked_vente(self, row, column):
        # Si la colonne 12 (Action) est cliquée
        if column == 11 :
            id_adherent = self.tableWidget.item(row, column).data(Qt.UserRole)  
            res = load_data(id_adherent)
            if res:
                from .profile_interface import Profile
                self.main_interface = Profile(id_adherent, self.main_inter)
            else:
                QMessageBox.information(self.main_inter, "Attenttion", "L'abonné est déjà Supprimer.")

    
 

    

    def submitForm(self):
        # Collecte des données
        data = {
            "id_adherent" : self.id_adherent,
            "name_haderent" : self.name_adherent,
            "nom": self.nom_input.text(),
            "date": self.date_input.date().toString("yyyy-MM-dd"),
            "nature": self.nature_input.text(),
            "gravite": self.gravite_input.currentText(),
            "soins": self.soins_input.text(),
            "hospitalisation": self.hospitalisation_input.currentText(),
            "rapport": self.rapport_input.text(),
            "indispo": self.indispo_input.text(),
            "temoins": self.temoins_input.text(),
            "mesures": self.mesures_input.text(),
        }

        inser_db_sinistre(data)
        self.resetForm()
        from .profile_interface import Profile
        self.main_interface = Profile(self.id_adherent, self.main_inter)

    def resetForm(self):
        # Réinitialisation du formulaire
        self.nom_input.clear()
        self.date_input.clear()
        self.nature_input.clear()
        self.gravite_input.setCurrentIndex(0)
        self.soins_input.clear()
        self.hospitalisation_input.setCurrentIndex(0)
        self.rapport_input.clear()
        self.indispo_input.clear()
        self.temoins_input.clear()
        self.mesures_input.clear()

    def closeEvent(self, event):
        # Fermeture de la base de données à la sortie
        self.conn.close()
        event.accept()