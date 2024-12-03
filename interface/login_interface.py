from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox,QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from utils.utils import *
from dataset.dataset import *
from .main_interface import MainInterface

from .dashbord import Dashbord

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuration principale
        self.setWindowTitle("Bureau de Suivi des Adhérents - Royal Fitness")
        self.setGeometry(100, 100, 1500, 800)
        self.showFullScreen()
        self.create_login_interface()
        self.setStyleSheet(set_styles())
        
        

    def create_login_interface(self):
        self.central_widget = QWidget()
        self.central_widget.setObjectName("main") 
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QVBoxLayout(self.central_widget) 

        

        # Layout principal
        top_widget = QWidget()
        top_layout = QHBoxLayout(top_widget)
        top_widget.setObjectName("top_widget")

        
        # Add the layout to your main layout
        self.main_layout.addWidget(top_widget) 
       # Ajouter le logo à gauche
        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/images/logos/Logo.png").scaled(240, 240, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo_label.setObjectName("logotop")
        self.logo_label.setAlignment(Qt.AlignLeft)
        top_layout.addWidget(self.logo_label)
        
        # Ajouter le titre à droite
        self.title_label = QLabel("Bureau de Suivi des Adhérents")
        self.title_label.setObjectName("titleLabel")
        self.title_label.setAlignment(Qt.AlignRight)
        top_layout.addWidget(self.title_label, alignment=Qt.AlignRight)

        
        # Page de connexion
        self.login_frame = QFrame()
        self.login_frame.setFixedSize(400, 400)  # Frame carrée avec taille fixe 
        self.main_layout.addWidget(self.login_frame, alignment=Qt.AlignCenter)
        self.login_frame.setObjectName("loginframe")

        # Layout de la frame de connexion
        self.login_layout = QVBoxLayout(self.login_frame)

        self.connexion = QLabel("Connexion")
        self.connexion.setObjectName('connexionlab')
        self.login_layout.addWidget(self.connexion )

        self.user_label = QLabel("Utilisateur :")
        self.login_layout.addWidget(self.user_label)

        self.user_entry = QLineEdit()
        self.user_entry.setPlaceholderText("Entrez votre nom d'utilisateur")
        self.login_layout.addWidget(self.user_entry)

        self.password_label = QLabel("Mot de passe :")
        self.login_layout.addWidget(self.password_label)

        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setPlaceholderText("Entrez votre mot de passe")
        self.login_layout.addWidget(self.password_entry)

        self.login_button = QPushButton("Se connecter")
        self.login_button.clicked.connect(self.login)
        self.login_button.setObjectName("buttconexion")
        self.login_layout.addWidget(self.login_button)
        

    def login(self):
        username = self.user_entry.text()
        password = self.password_entry.text()

        # Vérification des identifiants
        if username == "user1" and password == "123":
            self.show_main_interface()
        else:
            QMessageBox.critical(self, "Erreur", "Nom d'utilisateur ou mot de passe incorrect")


    def show_main_interface(self): 
        self.main_interface = Dashbord()
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
        from .gestion_adherents import Gestion_adherents 
        self.main_interface = Gestion_adherents()
        self.main_interface.show()
        self.close()
    def ajouter_adh(self):
        from .ajouter_adherent import AjouterAfh
        self.main_interface = AjouterAfh()
        self.main_interface.show()
        self.close()
        
    
