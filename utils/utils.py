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
from openpyxl import Workbook
import os
import shutil


from dataset.dataset import *

path_logo = "/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/images/logos/logoa.png"


def set_styles():
    try:
        with open("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/style/style.qss", "r") as file:
            style = file.read()
            return style
    except FileNotFoundError:
        print("Style file not found. Using default styles.")


def increment_month(year: int, month: int) -> tuple:
    """
    Incrémente un mois et ajuste l'année si nécessaire.

    Args:
        year (int): L'année actuelle.
        month (int): Le mois actuel (1 à 12).

    Returns:
        tuple: Une paire (année mise à jour, mois mis à jour).
    """
    if not (1 <= month <= 12):
        raise ValueError("Le mois doit être entre 1 et 12 inclus.")

    # Incrémenter le mois
    month += 1
    if month > 12:  # Si on dépasse décembre
        month = 1  # Revenir à janvier
        year += 1  # Incrémenter l'année

    return year, month


def decrement_month(year: int, month: int) -> tuple:
    """
    Décrémente un mois et ajuste l'année si nécessaire.

    Args:
        year (int): L'année actuelle.
        month (int): Le mois actuel (1 à 12).

    Returns:
        tuple: Une paire (année mise à jour, mois mis à jour).
    """
    if not (1 <= month <= 12):
        raise ValueError("Le mois doit être entre 1 et 12 inclus.")

    # Décrémenter le mois
    month -= 1
    if month < 1:  # Si on descend en dessous de janvier
        month = 12  # Revenir à décembre
        year -= 1  # Décrémenter l'année

    return year, month

def deplacer_et_renommer_image(source_path, destination_folder, nouveau_nom):
    """
    Déplace une image vers un dossier spécifique et la renomme.

    Args:
        source_path (str): Le chemin complet de l'image source.
        destination_folder (str): Le dossier de destination.
        nouveau_nom (str): Le nouveau nom du fichier (sans extension).
    
    Returns:
        str: Le nouveau chemin complet de l'image déplacée et renommée.
    """
    # Vérifier si le fichier source existe
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Le fichier source n'existe pas : {source_path}")
    
    # Créer le dossier de destination s'il n'existe pas
    os.makedirs(destination_folder, exist_ok=True)
    
    # Obtenir l'extension de l'image source
    extension = os.path.splitext(source_path)[1]
    
    # Construire le chemin complet du nouveau fichier
    nouveau_chemin = os.path.join(destination_folder, f"{nouveau_nom}{extension}")
    
    # Déplacer et renommer le fichier
    shutil.move(source_path, nouveau_chemin)
    
    return nouveau_chemin





def write_to_excel(file_name="output.xlsx"):
     
    workbook = Workbook()
    adherents = fetch_data()
    paiments = recuperer_all_paiements()
    # Feuille 1
    sheet1 = workbook.active
    sheet1.title = "adherents"
    for row in adherents:
        sheet1.append(row)

    # Feuille 2
    sheet2 = workbook.create_sheet(title="paiments")
    for row in paiments:
        sheet2.append(row)

    # Sauvegarde du fichier Excel
    workbook.save(file_name) 

 