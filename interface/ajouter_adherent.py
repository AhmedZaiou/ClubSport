from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import *
from .main_interface import MainInterface
 

class AjouterAfh(MainInterface):
    def __init__(self):
        super().__init__()
        self.ajouter_adh_interf()



    def ajouter_adh_interf(self):
        self.clear_content_frame()

        self.form_widget = QWidget()
        self.form_widget.setObjectName("FormulaireWidget") 
        
        
        form_layout = QFormLayout(self.form_widget)

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
        self.tarif_input.setReadOnly(True)  # Calcul automatique

        self.seances_input = QSpinBox()
        self.seances_input.setRange(1, 100)
        self.seances_input.setValue(4)
        self.seances_input.setReadOnly(True)  # Calcul automatique

        self.situation_input = QComboBox()
        self.situation_input.addItems(["Paiement effectué", "Paiement non effectué"])

        self.photo_input = QLabel("Aucune photo sélectionnée")
        self.photo_path = None

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
        self.photo_button.clicked.connect(select_photo)

        # Bouton d'enregistrement
        self.save_button = QPushButton("Enregistrer")
        self.save_button.clicked.connect(self.save_adherent)

        # Ajouter les boutons au layout 
        form_layout.addWidget(self.photo_button)
        form_layout.addWidget(self.save_button)
 
        
        self.content_layout.addWidget(self.form_widget)

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
        photo_path = self.photo_path if self.photo_path else "Aucune"

        # Vérification des champs obligatoires
        if not nom or not prenom or not cin:
            QMessageBox.warning(self, "Champs manquants", "Veuillez remplir tous les champs obligatoires.")
            return

        # Connexion à la base de données SQLite
        try:
            ajouter_adh(nom, prenom, email, telephone, cin, num_adh, adresse, date_entree, age, genre, tarif, seances, situation, photo_path)
            QMessageBox.information(self, "Succès", "L'adhérent a été enregistré avec succès.")

            # Réinitialisation du formulaire
            self.reset_form()

        except sqlite3.IntegrityError as e:
            QMessageBox.warning(self, "Erreur", f"Un problème est survenu : {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Erreur critique", f"Une erreur inattendue est survenue : {str(e)}")
         

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
        from .gestion_adherents import Gestion_adherents 
        self.main_interface = Gestion_adherents()
        self.main_interface.show()
        self.close()
    def ajouter_adh(self):
        from .ajouter_adherent import AjouterAfh
        self.main_interface = AjouterAfh()
        self.main_interface.show()
        self.close()
        
    