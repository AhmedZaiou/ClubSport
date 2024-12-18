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

        self.form_widget = QWidget()
        self.form_widget.setObjectName("FormulaireWidget") 

        form_layout = QFormLayout(self.form_widget)
        titre=QLabel("Modifier les informations")
        titre.setObjectName("Titre_f")

        form_layout.addWidget(titre)

        # Champs du formulaire
        self.nom_input = QLineEdit(data_adherent[1])
        self.prenom_input = QLineEdit(data_adherent[2])
        self.email_input = QLineEdit(data_adherent[3])
        self.telephone_input = QLineEdit(data_adherent[4])
        self.cin_input = QLineEdit(data_adherent[5])
        self.num_adh_input = QLineEdit(data_adherent[6])
        self.adresse_input = QLineEdit(data_adherent[7])


        self.nom_parent = QLineEdit()
        self.contact_parent = QLineEdit()

        self.numero_assurance = QLineEdit(data_adherent[24])
        self.centure = QLineEdit(data_adherent[25])
        self.dautreinformation = QLineEdit(data_adherent[22])

        self.date_entree_input = QDateEdit()
        self.date_entree_input.setDate(QDate.fromString(data_adherent[8], "yyyy-MM-dd"))

        self.nom_input.setObjectName("QLineEditstyle") 
        self.prenom_input.setObjectName("QLineEditstyle") 
        self.email_input.setObjectName("QLineEditstyle") 
        self.telephone_input.setObjectName("QLineEditstyle") 
        self.cin_input.setObjectName("QLineEditstyle") 
        self.num_adh_input.setObjectName("QLineEditstyle") 
        self.adresse_input.setObjectName("QLineEditstyle") 
        self.centure.setObjectName("QLineEditstyle")
        self.dautreinformation.setObjectName("QLineEditstyle") 

        self.nom_parent.setObjectName("QLineEditstyle") 
        self.contact_parent.setObjectName("QLineEditstyle") 
        self.numero_assurance.setObjectName("QLineEditstyle") 
        
        
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

        self.situation_input = QSpinBox()
        self.situation_input.setRange(1, 10000)
        self.situation_input.setValue(int(data_adherent[13]))

        self.photo_input = QLabel(data_adherent[14])
        self.photo_path = data_adherent[14]
        



        self.poids = QLineEdit()
        self.longueur = QLineEdit()
        self.situation_sanitaire = QComboBox()
        self.situation_sanitaire.addItems([ 'Inapte','Apte'])


        self.poids.setObjectName("QLineEditstyle") 
        self.longueur.setObjectName("QLineEditstyle") 
         
        
        self.situation_sanitaire.currentIndexChanged.connect(self.deactiver_sanitaire)
        
        self.situation_sanitaire_text = QLineEdit()
        self.situation_sanitaire_text.setReadOnly(True)
        self.situation_sanitaire_text.setObjectName("QLineEditstyle") 

        self.titre_sport = QComboBox()
        list_sport = ["Arts martiaux", "Fitness"]
        list_sani = ['Inapte', 'Apte']
        self.titre_sport.addItems(list_sport)
        disciplines = {
            "Arts martiaux": ["Judo", "Karaté", "Aïkido", "Kendo", "Jiu-Jitsu", "Kung Fu", "Tai Chi", "Wing Chun", "Sanda", "Taekwondo", "Hapkido", "Kalaripayattu", "Gatka"],
            "Fitness": ["CrossFit", "Musculation", "Cardio", "Yoga", "Pilates"]
        }
        


        self.discipline_input = QComboBox() 

        

        self.titre_sport.currentTextChanged.connect(self.update_disciplines)
        


        self.poids.setText(str(data_adherent[15]))
        self.longueur.setText(str(data_adherent[16]))
        self.titre_sport.itemText(list_sport.index(str(data_adherent[17])))
        self.nom_parent.setText(str(data_adherent[18]))
        self.contact_parent.setText(str(data_adherent[19]))
        self.situation_sanitaire.itemText(list_sani.index(data_adherent[20]))
        self.situation_sanitaire_text.setText(str(data_adherent[21]))
        self.update_disciplines(str(data_adherent[17]))

        self.discipline_input.itemText(disciplines[str(data_adherent[17])].index(str(data_adherent[23])))
        



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


        row_layout_9 = QHBoxLayout()
        row_layout_9.addWidget(self.poids)
        row_layout_9.addWidget(QLabel("Longueur :"))
        row_layout_9.addWidget(self.longueur)
        form_layout.addRow("Poids :", row_layout_9)

        

        row_layout_11 = QHBoxLayout()
        row_layout_11.addWidget(self.situation_sanitaire)
        row_layout_11.addWidget(QLabel("Genre de maladie :"))
        row_layout_11.addWidget(self.situation_sanitaire_text)
        form_layout.addRow("Situation sanitaire :", row_layout_11)

        row_layout_12 = QHBoxLayout()
        row_layout_12.addWidget(self.titre_sport)
        row_layout_12.addWidget(QLabel('Discipline : '))
        row_layout_12.addWidget(self.discipline_input)
        form_layout.addRow("Genre de sport :", row_layout_12)

        

        """row_layout_8 = QHBoxLayout()
        row_layout_8.addWidget(self.situation_input)
        row_layout_8.addWidget(QLabel(" "))
        row_layout_8.addWidget(self.photo_input)
        form_layout.addRow(" ", row_layout_8)"""


         
        

        row_layout_17 = QHBoxLayout()
        row_layout_17.addWidget(self.numero_assurance)
        row_layout_17.addWidget(QLabel("Prix assurance :"))
        row_layout_17.addWidget(self.situation_input)
        form_layout.addRow("Numero assurance :", row_layout_17)

        row_layout_19 = QHBoxLayout()
        row_layout_19.addWidget(self.centure)
        row_layout_19.addWidget(QLabel("D'autre informations :"))
        row_layout_19.addWidget(self.dautreinformation)
        form_layout.addRow("Centure :", row_layout_19)

        row_layout_7 = QHBoxLayout()
        row_layout_7.addWidget(QLabel(" "))
        row_layout_7.addWidget(QLabel("Photo :"))
        row_layout_7.addWidget(self.photo_input)
        form_layout.addRow("", row_layout_7)


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

    def update_disciplines(self, genre):
        disciplines = {
            "Arts martiaux": ["Judo", "Karaté", "Aïkido", "Kendo", "Jiu-Jitsu", "Kung Fu", "Tai Chi", "Wing Chun", "Sanda", "Taekwondo", "Hapkido", "Kalaripayattu", "Gatka"],
            "Fitness": ["CrossFit", "Musculation", "Cardio", "Yoga", "Pilates"]
        }
        self.discipline_input.clear()
        self.discipline_input.addItems(disciplines.get(genre, []))


    def deactiver_sanitaire(self):
        if self.situation_sanitaire.currentText() == 'Apte':
            self.situation_sanitaire_text.setReadOnly(False)
        else:
            self.situation_sanitaire_text.setReadOnly(True)

    
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
        situation = self.situation_input.value() 
        photo_path = deplacer_et_renommer_image(self.photo_path, path_profils_images, f'{nom}-{prenom}-{cin}') if self.photo_path else "Aucune"

        if age < 18:
            nom_parent = self.nom_parent.text()
            contact_parent = self.contact_parent.text()
        else:
            nom_parent =  ''
            contact_parent =  ''
        poids = self.poids.text()
        situation_sanitaire = self.situation_sanitaire.currentText()
        if situation_sanitaire == "apte": 
            situation_sanitaire_text = self.situation_sanitaire_text.text()
        else:
            situation_sanitaire_text = ""
        longeur = self.longueur.text()
        titre_sport = self.titre_sport.currentText()

        discipline = self.discipline_input.currentText()
        numero_assurance = self.numero_assurance.text()
        centure =self.centure.text()
        dautre_information = self.dautreinformation.text()




        # Vérification des champs obligatoires
        if not nom or not prenom or not email or not telephone or not cin or not num_adh or not adresse or not date_entree or not age or not genre or not tarif or not seances or not situation or not photo_path or not situation_sanitaire or not poids or not longeur or not titre_sport:
            QMessageBox.warning(self.main_inter, "Champs manquants", "Veuillez remplir tous les champs obligatoires.")
            return

        # Connexion à la base de données SQLite
        try:
            modifier_adh(self.id_adherent,nom, prenom, email, telephone, cin, num_adh, adresse, date_entree, age, genre, tarif, seances, situation, photo_path, poids, longeur, titre_sport, nom_parent, contact_parent, situation_sanitaire, situation_sanitaire_text, discipline, numero_assurance, centure, dautre_information)
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
         
 