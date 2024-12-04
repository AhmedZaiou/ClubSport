from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import *
from .main_interface import MainInterface
 

class ModefierADh():
    def __init__(self,main_inter, id_adherent): 
        self.main_inter = main_inter
        self.id_adherent = id_adherent
        self.modefier_adh_interf()



    def modefier_adh_interf(self):
        self.main_inter.clear_content_frame()

        data_adherent = load_data( self.id_adherent)
        """id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prenom TEXT,
            email TEXT,
            telephone TEXT,
            cin TEXT UNIQUE,
            num_adh TEXT UNIQUE,
            adresse TEXT,
            date_entree DATE,
            age INTEGER,
            genre TEXT,
            tarif INTEGER,
            seances INTEGER,
            situation TEXT,
            photo_path TEXT"""

        self.form_widget = QWidget()
        self.form_widget.setObjectName("FormulaireWidget") 
        
        
        form_layout = QFormLayout(self.form_widget)

        # Champs du formulaire
        self.nom_input = QLineEdit(data_adherent[1])
        self.prenom_input = QLineEdit(data_adherent[2])
        self.email_input = QLineEdit(data_adherent[3])
        self.telephone_input = QLineEdit(data_adherent[4])
        self.cin_input = QLineEdit(data_adherent[5])
        self.num_adh_input = QLineEdit(data_adherent[6])
        self.adresse_input = QLineEdit(data_adherent[7])

        self.date_entree_input = QDateEdit()
        self.date_entree_input.setDate(QDate.fromString(data_adherent[8], "yyyy-MM-dd"))

        self.nom_input.setObjectName("QLineEditstyle") 
        self.prenom_input.setObjectName("QLineEditstyle") 
        self.email_input.setObjectName("QLineEditstyle") 
        self.telephone_input.setObjectName("QLineEditstyle") 
        self.cin_input.setObjectName("QLineEditstyle") 
        self.num_adh_input.setObjectName("QLineEditstyle") 
        self.adresse_input.setObjectName("QLineEditstyle") 
        
        self.age_input = QSpinBox()
        self.age_input.setRange(1, 100)
        self.age_input.setValue(int(data_adherent[9]))
 

        self.genre_input = QComboBox()
        self.genre_input.addItems(["Homme", "Femme"])
        self.genre_input.setCurrentText(data_adherent[10])
         

        self.tarif_input = QSpinBox()
        self.tarif_input.setRange(1, 1000)
        self.tarif_input.setValue(int(data_adherent[11])) 

        self.seances_input = QSpinBox()
        self.seances_input.setRange(1, 100)
        self.seances_input.setValue(int(data_adherent[12])) 

        self.situation_input = QComboBox()
        self.situation_input.addItems(["Paiement effectué", "Paiement non effectué"])
        self.situation_input.setCurrentText(data_adherent[13])

        self.photo_input = QLabel(data_adherent[14])
        self.photo_path = data_adherent[14]

        # Ajouter les champs au formulaire
        form_layout.addRow("Nom :", self.nom_input)
        form_layout.addRow("Prénom :", self.prenom_input)
        form_layout.addRow("Email :", self.email_input)
        form_layout.addRow("Téléphone :", self.telephone_input)
        form_layout.addRow("CIN :", self.cin_input)
        form_layout.addRow("Numéro d'adhérent :", self.num_adh_input)
        form_layout.addRow("Adresse :", self.adresse_input)
        form_layout.addRow("Date d'entrée :", self.date_entree_input)
        form_layout.addRow("Âge :", self.age_input)
        form_layout.addRow("Genre :", self.genre_input)
        form_layout.addRow("Tarif mensuel :", self.tarif_input)
        form_layout.addRow("Séances incluses :", self.seances_input)
        form_layout.addRow("Situation du mois :", self.situation_input)
        form_layout.addRow("Photo :", self.photo_input)

        # Bouton de sélection de photo
        self.photo_button = QPushButton("Sélectionner une photo")
        self.photo_button.clicked.connect(self.select_photo)

        # Bouton d'enregistrement
        self.save_button = QPushButton("Enregistrer")
        self.save_button.clicked.connect(self.save_adherent)

        # Ajouter les boutons au layout 
        form_layout.addWidget(self.photo_button)
        form_layout.addWidget(self.save_button)
 
        
        self.main_inter.content_layout.addWidget(self.form_widget)

    
    def save_adherent(self):
        # Récupération des données du formulaire
        nom = self.nom_input.text()
        prenom = self.prenom_input.text()
        email = self.email_input.text()
        telephone = self.telephone_input.text()
        cin = self.cin_input.text()
        num_adh = self.num_adh_input.text()
        adresse = self.adresse_input.text()
        date_entree = self.date_entree_input.date().toString("yyyy-MM-dd")
        age = self.age_input.value()
        genre = self.genre_input.currentText()
        tarif = self.tarif_input.value()
        seances = self.seances_input.value()
        situation = self.situation_input.currentText()
        destination_path = "/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/images/profiles"
        photo_path = deplacer_et_renommer_image(self.photo_path, destination_path, f'{nom}-{prenom}-{cin}') if self.photo_path else "Aucune"

        # Vérification des champs obligatoires
        if not nom or not prenom or not cin:
            QMessageBox.warning(self, "Champs manquants", "Veuillez remplir tous les champs obligatoires.")
            return

        # Connexion à la base de données SQLite
        try:
            modifier_adh(self.id_adherent,nom, prenom, email, telephone, cin, num_adh, adresse, date_entree, age, genre, tarif, seances, situation, photo_path)
            QMessageBox.information(self.main_inter, "Succès", "Les information à été modéfier avec succès.")
            from .profile_interface import Profile
            self.main_interface = Profile(self.id_adherent, self.main_inter)
        except sqlite3.IntegrityError as e:
            QMessageBox.warning(self.main_inter, "Erreur", f"Un problème est survenu : {str(e)}")
        except Exception as e:
            QMessageBox.critical(self.main_inter, "Erreur critique", f"Une erreur inattendue est survenue : {str(e)}")
    
    def select_photo(self):
        """Ouvrir une boîte de dialogue pour sélectionner une photo."""
        file_name, _ = QFileDialog.getOpenFileName(self.main_inter, "Sélectionner une photo", "", "Images (*.png *.jpg *.bmp *.jpeg)")
        if file_name:
            self.photo_input.setText(file_name)
            self.photo_path = file_name
         
 