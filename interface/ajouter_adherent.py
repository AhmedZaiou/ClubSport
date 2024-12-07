from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import *
from .main_interface import MainInterface
 

class AjouterAfh():
    def __init__(self,main_inter): 
        self.main_inter = main_inter
        self.ajouter_adh_interf()



    def ajouter_adh_interf(self):
        self.main_inter.clear_content_frame()

        self.form_widget = QWidget()
        self.form_widget.setObjectName("FormulaireWidget") 



        
        
        form_layout = QFormLayout(self.form_widget)
        titre=QLabel('Ajouter des abonnés')
        titre.setObjectName("Titre_f")

        form_layout.addWidget(titre)
        # Champs du formulaire
        self.nom_input = QLineEdit()
        self.prenom_input = QLineEdit()
        self.email_input = QLineEdit()
        self.telephone_input = QLineEdit()
        self.cin_input = QLineEdit()
        self.num_adh_input = QLineEdit()
        self.adresse_input = QLineEdit()

        self.date_entree_input = QDateEdit()
        self.date_entree_input.setDate(QDate.currentDate())

        self.nom_input.setObjectName("QLineEditstyle") 
        self.prenom_input.setObjectName("QLineEditstyle") 
        self.email_input.setObjectName("QLineEditstyle") 
        self.telephone_input.setObjectName("QLineEditstyle") 
        self.cin_input.setObjectName("QLineEditstyle") 
        self.num_adh_input.setObjectName("QLineEditstyle") 
        self.adresse_input.setObjectName("QLineEditstyle") 
        
        self.age_input = QSpinBox()
        self.age_input.setRange(1, 100)
        self.age_input.valueChanged.connect(self.update_tarif)

        self.genre_input = QComboBox()
        self.genre_input.addItems(["Homme", "Femme"])
        self.genre_input.currentIndexChanged.connect(self.update_tarif)

        self.tarif_input = QSpinBox()
        self.tarif_input.setRange(1, 1000)
        self.tarif_input.setValue(150) 

        self.seances_input = QSpinBox()
        self.seances_input.setRange(1, 100)
        self.seances_input.setValue(4) 

        self.situation_input = QComboBox()
        self.situation_input.addItems(["Paiement effectué", "Paiement non effectué"])

        self.photo_input = QLabel("Aucune photo sélectionnée")
        self.photo_path = None

        # Ajouter les champs au formulaire
        """form_layout.addRow("Nom :", self.nom_input)
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
        form_layout.addRow("Photo :", self.photo_input) """
        # First row: Nom, Prénom
        row_layout_1 = QHBoxLayout()
        row_layout_1.addWidget(self.nom_input)
        row_layout_1.addWidget(QLabel("Prénom : "))
        row_layout_1.addWidget(self.prenom_input)

        form_layout.addRow("Nom :", row_layout_1)

        # Second row: Email, Téléphone
        row_layout_2 = QHBoxLayout()
        row_layout_2.addWidget(self.email_input)
        row_layout_2.addWidget(QLabel("Téléphone :"))
        row_layout_2.addWidget(self.telephone_input)
        form_layout.addRow("Email :", row_layout_2)

        # Third row: CIN, Numéro d'adhérent
        row_layout_3 = QHBoxLayout()
        row_layout_3.addWidget(self.cin_input)
        row_layout_3.addWidget(QLabel("Numéro d'adhérent :"))
        row_layout_3.addWidget(self.num_adh_input)
        form_layout.addRow("CIN :", row_layout_3)

        # Fourth row: Adresse, Date d'entrée
        row_layout_4 = QHBoxLayout()
        row_layout_4.addWidget(self.adresse_input)
        row_layout_4.addWidget(QLabel("Date d'entrée :"))
        row_layout_4.addWidget(self.date_entree_input)
        form_layout.addRow("Adresse :", row_layout_4)

        # If you want to add more fields, you can use the same approach:
        row_layout_5 = QHBoxLayout()
        row_layout_5.addWidget(self.age_input)
        row_layout_5.addWidget(QLabel("Genre :"))
        row_layout_5.addWidget(self.genre_input)
        form_layout.addRow("Age :", row_layout_5)

        row_layout_6 = QHBoxLayout()
        row_layout_6.addWidget(self.tarif_input)
        row_layout_6.addWidget(QLabel("Séances incluses :"))
        row_layout_6.addWidget(self.seances_input)
        form_layout.addRow("Tarif mensuel :", row_layout_6)

        row_layout_7 = QHBoxLayout()
        row_layout_7.addWidget(self.situation_input)
        row_layout_7.addWidget(QLabel("Photo :"))
        row_layout_7.addWidget(self.photo_input)
        form_layout.addRow("Assurance :", row_layout_7)

        """row_layout_8 = QHBoxLayout()
        row_layout_8.addWidget(self.situation_input)
        row_layout_8.addWidget(QLabel(" "))
        row_layout_8.addWidget(self.photo_input)
        form_layout.addRow(" ", row_layout_8)"""


 
        
 

        # Bouton de sélection de photo
        self.photo_button = QPushButton("Sélectionner une photo")
        self.photo_button.clicked.connect(self.select_photo)
        self.photo_button.setObjectName("buttonformulaire")
        

        # Bouton d'enregistrement
        self.save_button = QPushButton("Enregistrer")
        self.save_button.clicked.connect(self.save_adherent)
        self.save_button.setObjectName("buttonformulaire")

        row_layout_8 = QHBoxLayout()
        row_layout_8.addWidget(self.photo_button)
        row_layout_8.addWidget(QLabel(" "))
        row_layout_8.addWidget(self.save_button)
        form_layout.addRow(" ", row_layout_8) 
        self.main_inter.content_layout.addWidget(self.form_widget)

    def update_tarif(self):
        """Met à jour le tarif et les séances en fonction de l'âge et du genre."""
        age = self.age_input.value()
        genre = self.genre_input.currentText()

        if genre == "Homme":
            if age >= 18:
                self.tarif_input.setValue(150)  # Musculation plus de 18 ans
                self.seances_input.setValue(4)  # 4 séances
            else:
                self.tarif_input.setValue(120)  # Musculation moins de 18 ans
                self.seances_input.setValue(4)  # 4 séances
        elif genre == "Femme":
            self.tarif_input.setValue(150)  # Gymnastique et aérobie
            self.seances_input.setValue(3)  # 3 séances par semaine

        # Ajouter l'assurance annuelle obligatoire
        assurance = 100
        tarif_final = self.tarif_input.value() + assurance
        self.tarif_input.setValue(tarif_final)

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
        photo_path = deplacer_et_renommer_image(self.photo_path, path_profils_images, f'{nom}-{prenom}-{cin}') if self.photo_path else "Aucune"

        # Vérification des champs obligatoires
        if not nom or not prenom or not cin:
            QMessageBox.warning(self.main_inter, "Champs manquants", "Veuillez remplir tous les champs obligatoires.")
            return

        # Connexion à la base de données SQLite
        try:
            ajouter_adh(nom, prenom, email, telephone, cin, num_adh, adresse, date_entree, age, genre, tarif, seances, situation, photo_path)
            QMessageBox.information(self.main_inter, "Succès", "L'adhérent a été enregistré avec succès.")

            # Réinitialisation du formulaire
            self.reset_form()

        except sqlite3.IntegrityError as e:
            QMessageBox.warning(self.main_inter, "Erreur", f"Un problème est survenu : {str(e)}")
        except Exception as e:
            QMessageBox.critical(self.main_inter, "Erreur critique", f"Une erreur inattendue est survenue : {str(e)}")
         

    def reset_form(self):
        """
        Réinitialise les champs du formulaire après l'enregistrement.
        """
        self.nom_input.clear()
        self.prenom_input.clear()
        self.email_input.clear()
        self.telephone_input.clear()
        self.cin_input.clear()
        self.num_adh_input.clear()
        self.adresse_input.clear()
        self.date_entree_input.setDate(QDate.currentDate())
        self.age_input.setValue(1)
        self.genre_input.setCurrentIndex(0)
        self.tarif_input.setValue(150)
        self.seances_input.setValue(4)
        self.situation_input.setCurrentIndex(0)
        self.photo_input.setText("Aucune photo sélectionnée")
        self.photo_path = None
    def select_photo(self):
        """Ouvrir une boîte de dialogue pour sélectionner une photo."""
        file_name, _ = QFileDialog.getOpenFileName(self.main_inter, "Sélectionner une photo", "", "Images (*.png *.jpg *.bmp *.jpeg)")
        if file_name:
            self.photo_input.setText(file_name)
            self.photo_path = file_name




    
    