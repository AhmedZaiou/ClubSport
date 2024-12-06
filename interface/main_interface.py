from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import * 


class MainInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Bureau de Suivi des Adhérents - Royal Fitness")
        self.setGeometry(100, 100, 1500, 800)
        self.showFullScreen()
        self.setStyleSheet(set_styles())
        self.show_main_interface()
    
    def show_main_interface(self): 
        self.central_widget = QWidget()
         
        self.setCentralWidget(self.central_widget)
        self.central_widget.setObjectName("main_interface") 

        self.main_layout = QVBoxLayout(self.central_widget) 
        # Créer la nouvelle interface
        self.main_interface_frame = QFrame()
        self.main_layout.addWidget(self.main_interface_frame)
        self.main_interface_layout = QHBoxLayout(self.main_interface_frame)


        # Menu latéral
        self.menu_frame = QFrame()
        self.menu_frame.setObjectName("menuFrame")
        self.main_interface_layout.addWidget(self.menu_frame)

        self.menu_layout = QVBoxLayout(self.menu_frame)

        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap(path_logo).scaled(180, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logo_label.setObjectName("logomenu")
        self.menu_layout.addWidget(self.logo_label)
        
        # Ajouter le titre à droite
        self.title_label = QLabel("Bureau de Suivi des Adhérents") 
        self.title_label.setObjectName("titremenu")
        self.menu_layout.addWidget(self.title_label, alignment=Qt.AlignRight)
 


        self.btn_dashboard = QPushButton("Tableau de bord")
        self.btn_dashboard.clicked.connect(self.show_dashboard)
        self.menu_layout.addWidget(self.btn_dashboard)
        self.btn_dashboard.setObjectName("buttonmenu")

        self.btn_ajout_adhs = QPushButton("Ajouter des abonnés")
        self.btn_ajout_adhs.clicked.connect(self.ajouter_adh)
        self.menu_layout.addWidget(self.btn_ajout_adhs)
        self.btn_ajout_adhs.setObjectName("buttonmenu")

        self.btn_due_dates = QPushButton("Gestion des abonnés")
        self.btn_due_dates.clicked.connect(self.show_due_dates)
        self.menu_layout.addWidget(self.btn_due_dates)
        self.btn_due_dates.setObjectName("buttonmenu")

        """self.btn_payments = QPushButton("Gestion de paiement")
        self.btn_payments.clicked.connect(self.show_payments)
        self.menu_layout.addWidget(self.btn_payments)
        self.btn_payments.setObjectName("buttonmenu")"""

        self.btn_revenues = QPushButton("Suivi des revenus")
        self.btn_revenues.clicked.connect(self.show_revenues)
        self.menu_layout.addWidget(self.btn_revenues)
        self.btn_revenues.setObjectName("buttonmenu") 

        self.btn_ajout_adhs = QPushButton("Déconnecté")
        self.btn_ajout_adhs.clicked.connect(self.deconnexion)
        self.menu_layout.addWidget(self.btn_ajout_adhs)
        self.btn_ajout_adhs.setObjectName("buttonmenu")

        

        # Contenu principal
        self.content_frame = QFrame()
        self.main_interface_layout.addWidget(self.content_frame)

        self.content_layout = QVBoxLayout(self.content_frame)
        #self.show_dashboard()
    
    def show_dashboard(self):
        from .dashbord import Dashbord
        self.main_interface = Dashbord(self)  
    def show_payments(self):
        from .payment import Payment
        self.main_interface = Payment(self)  
    def show_revenues(self):
        from .revenues_interface import Revenues
        self.main_interface = Revenues(self)  
    def show_due_dates(self):
        from .gestion_adherents import Gestion_adherents 
        self.main_interface = Gestion_adherents(self)  
    def ajouter_adh(self):
        from .ajouter_adherent import AjouterAfh
        self.main_interface = AjouterAfh(self)  
    def deconnexion(self):
        from .login_interface import LoginWindow
        self.close() 
        

    def clear_content_frame(self):
        for i in reversed(range(self.content_layout.count())):
            widget = self.content_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
    
