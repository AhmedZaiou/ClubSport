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
        self.setWindowTitle("Bureau de Royal Fitness, Taza")
        self.setGeometry(100, 100, 1500, 800)
        self.showFullScreen()
        if not path_data_set.exists():
            initialiser_dataset(path_data_set)
        if selectcode(): 
            self.create_login_interface()
        else:
            self.validateinstall()
        self.setStyleSheet(set_styles())
        
    def validateinstall(self):
        

        self.central_widget_p = QWidget()
        self.central_widget_p.setObjectName("central_widget_p")  

        self.main_layout_p = QVBoxLayout(self.central_widget_p) 
        
        self.setCentralWidget(self.central_widget_p)

        self.central_widget = QWidget()
        self.central_widget.setObjectName("main") 
        
        self.main_layout = QVBoxLayout(self.central_widget) 

        

        # Layout principal
        top_widget = QWidget()
        top_layout = QHBoxLayout(top_widget)
        top_widget.setObjectName("top_widget")
        
        # Add the layout to your main layout
        self.main_layout.addWidget(top_widget) 
       # Ajouter le logo à gauche
        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap(str(logo_path)).scaled(240, 240, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo_label.setObjectName("logotop")
        self.logo_label.setAlignment(Qt.AlignLeft)
        top_layout.addWidget(self.logo_label)
        
        # Ajouter le titre à droite
        self.title_label = QLabel("Bureau de Royal Fitness, Taza")
        self.title_label.setObjectName("titleLabel")
        self.title_label.setAlignment(Qt.AlignLeft)
        top_layout.addWidget(self.title_label, alignment=Qt.AlignLeft)

        
        # Page de connexion
        self.login_frame = QFrame()
        self.login_frame.setFixedSize(400, 400)  # Frame carrée avec taille fixe 
        self.main_layout.addWidget(self.login_frame, alignment=Qt.AlignCenter)
        self.login_frame.setObjectName("loginframe")

        # Layout de la frame de connexion
        self.login_layout = QVBoxLayout(self.login_frame)

        self.connexion = QLabel("Activer votre application")
        self.connexion.setObjectName('connexionlab')
        self.login_layout.addWidget(self.connexion )

        self.user_label = QLabel("Code unique :")
        self.login_layout.addWidget(self.user_label)

        self.user_entry = QLineEdit()
        self.user_entry.setPlaceholderText("Entrez votre code unique")
        self.login_layout.addWidget(self.user_entry)

        self.login_button = QPushButton("Activer l'application")
        self.login_button.clicked.connect(self.activer)
        self.login_button.setObjectName("buttconexion")
        self.login_layout.addWidget(self.login_button)

        self.main_layout_p.addWidget(self.central_widget)

        
    def activer(self):
        code = self.user_entry.text() 
        if code_f(code):
            insert_code(code) 
            QMessageBox.warning(self, "Activation réussie", "Activation réussie, veuillez démarrer l'application.")
            self.close()
        else:
            QMessageBox.warning(self, "Activation non réussie", "L'activation a échoué. Veuillez vérifier les informations et réessayer.")
            
    



    def create_login_interface(self): 
        

        self.central_widget_p = QWidget()
        self.central_widget_p.setObjectName("central_widget_p")  

        self.main_layout_p = QVBoxLayout(self.central_widget_p) 
        
        self.setCentralWidget(self.central_widget_p)

        self.central_widget = QWidget()
        self.central_widget.setObjectName("main") 
        
        self.main_layout = QVBoxLayout(self.central_widget) 

        

        # Layout principal
        top_widget = QWidget()
        top_layout = QHBoxLayout(top_widget)
        top_widget.setObjectName("top_widget")
        
        # Add the layout to your main layout
        self.main_layout.addWidget(top_widget) 
       # Ajouter le logo à gauche
        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap(str(logo_path)).scaled(240, 240, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo_label.setObjectName("logotop")
        self.logo_label.setAlignment(Qt.AlignLeft)
        top_layout.addWidget(self.logo_label)
        
        # Ajouter le titre à droite
        self.title_label = QLabel("Bureau de Royal Fitness, Taza")
        self.title_label.setObjectName("titleLabel")
        self.title_label.setAlignment(Qt.AlignLeft)
        top_layout.addWidget(self.title_label, alignment=Qt.AlignLeft)

        
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

        self.main_layout_p.addWidget(self.central_widget)

        
        

    def login(self):
        username = self.user_entry.text()
        password = self.password_entry.text()


        # Vérification des identifiants
        if loging_pass(username, password) or (username == "admin" and password == "123") or (username == "admin1" and password == "11221122"):
            self.show_main_interface() 
        else:
            QMessageBox.critical(self, "Erreur", "Nom d'utilisateur ou mot de passe incorrect")
            


    def show_main_interface(self): 
        
        Main = MainInterface()
        self.main_interface = Dashbord(Main)  
        self.close()
         
        
    

 