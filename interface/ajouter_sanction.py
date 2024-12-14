from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import *
from .main_interface import MainInterface
 

class Sanction():
    def __init__(self,main_inter, id_adherent): 
        self.main_inter = main_inter
        self.id_adherent = id_adherent
        self.modefier_adh_interf()



    def modefier_adh_interf(self):
        self.main_inter.clear_content_frame() 

        self.form_widget = QWidget()
        self.form_widget.setObjectName("FormulaireWidget") 

        form_layout = QFormLayout(self.form_widget)
        titre=QLabel("Ajouter une sanction")
        titre.setObjectName("Titre_f")

        form_layout.addWidget(titre)

        # Champs du formulaire
        self.cause = QLineEdit()
        self.genre = QComboBox()
        self.genre.addItems(["ARRET PROVISOIRE", "ARRET DÉFINITIF"])
        self.durre = QSpinBox()
        self.durre.setRange(1, 500)
        self.durre.setValue(15)
        self.date_start = QDateEdit()
        self.date_start.setDate(QDate.currentDate())

        self.cause.setObjectName("QLineEditstyle") 
        self.durre.setObjectName("QLineEditstyle")  

        form_layout.addRow("Cause de la sanction :", self.cause)
        form_layout.addRow("Genre de la sanction :", self.genre)
        form_layout.addRow("Durre de la sanction :", self.durre)
        form_layout.addRow("date_start de la sanction :", self.date_start)

        # Bouton d'enregistrement
        self.save_button = QPushButton("Enregistrer la sanction")
        self.save_button.clicked.connect(self.sanction_adherent)
        self.save_button.setObjectName("buttonformulaire")

        
        form_layout.addRow(" ", self.save_button) 
        self.main_inter.content_layout.addWidget(self.form_widget)

    
    def sanction_adherent(self):
        # Récupération des données du formulaire 

 

        cause = self.cause.text()
        genre = self.genre.currentText()
        duree = self.durre.value()
        date_s = self.date_start.date().toString("yyyy-MM-dd")
        date_f = self.date_start.date().addDays(duree).toString("yyyy-MM-dd")


        # Vérification des champs obligatoires
        
        # Connexion à la base de données SQLite
        try:
            ajouter_sanction(self.id_adherent, cause, genre, duree, date_s,date_f) 
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
         
 