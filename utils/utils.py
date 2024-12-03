import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit,QFormLayout, QPushButton, QVBoxLayout,QDateEdit,QSpinBox,QComboBox,QFileDialog,QTableWidget,QHeaderView,
    QHBoxLayout, QFrame, QMessageBox, QWidget,QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView,QGridLayout
) 
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt, QDate
import sqlite3 
from PyQt5.QtGui import QColor

import sys 
import pandas as pd
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, QTableWidget, QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import datetime



def select_photo(self):
        """Ouvrir une boîte de dialogue pour sélectionner une photo."""
        file_name, _ = QFileDialog.getOpenFileName(self, "Sélectionner une photo", "", "Images (*.png *.jpg *.bmp *.jpeg)")
        if file_name:
            self.photo_input.setText(file_name)
            self.photo_path = file_name


def set_styles():
    try:
        with open("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/style/style.qss", "r") as file:
            style = file.read()
            return style
    except FileNotFoundError:
        print("Style file not found. Using default styles.")
