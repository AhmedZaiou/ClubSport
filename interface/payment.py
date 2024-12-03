from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import * 
from .main_interface import MainInterface
 

class Payment(MainInterface):
    def __init__(self):
        super().__init__()
    
    
    def show_dashboard(self):
        from .dashbord import Dashbord
        self.main_interface = Dashbord()
        self.main_interface.show()
        self.close()
    def show_payments(self): 
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
        
    