from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import * 
from .main_interface import MainInterface 
from datetime import datetime


class Profile(MainInterface):
    def __init__(self, id_profile):
        super().__init__()
        self.id_profile = id_profile

        self.show_profile_content()

    def show_profile_content(self):
        self.clear_content_frame()

        self.dashbord_widget = QWidget()
        self.dashbord_widget.setObjectName("dashbord_widget")

        # Layout principal
        layout = QVBoxLayout(self.dashbord_widget)

        
        
        # Layouts horizontaux pour les graphiques
        graphs_layout = QHBoxLayout()
        
        # Graphique 1 : Pourcentage des situations pour ce mois
        self.form_widget = QWidget()
        self.form_widget.setObjectName("FormulaireWidget") 
        self.show_profile()
        graphs_layout.addWidget(self.form_widget)
        
        
        # Graphique 2 : Revenus mensuels pour cette année
        
          
        
        # Ajout des graphiques au layout principal
        layout.addLayout(graphs_layout)
        
        # Tableau pour afficher les adhérents avec situation = NON
        self.form_paiment = QWidget()
        self.form_paiment.setObjectName("FormulaireWidget") 
        self.show_payment_formule()
        layout.addWidget(self.form_paiment)
        
        self.content_layout.addWidget(self.dashbord_widget) 
    
    def show_profile(self): 
        main_layout = QVBoxLayout(self.form_widget)

        # Photo de l'adhérent
        self.photo_label = QLabel()
        self.photo_label.setPixmap(QPixmap("logo.png").scaled(240, 240, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        

        # Informations de l'adhérent
        self.info_layout = QGridLayout()
        

        # Création des labels pour chaque information
        self.nom_label = QLabel("Nom:")
        self.nom_value = QLabel()
        self.prenom_label = QLabel("Prénom:")
        self.prenom_value = QLabel()
        self.email_label = QLabel("Email:")
        self.email_value = QLabel()
        self.telephone_label = QLabel("Téléphone:")
        self.telephone_value = QLabel()
        self.cin_label = QLabel("CIN:")
        self.cin_value = QLabel()
        self.num_adh_label = QLabel("Numéro d'adhérent:")
        self.num_adh_value = QLabel()
        self.adresse_label = QLabel("Adresse:")
        self.adresse_value = QLabel()
        self.date_entree_label = QLabel("Date d'entrée:")
        self.date_entree_value = QLabel()
        self.age_label = QLabel("Âge:")
        self.age_value = QLabel()
        self.genre_label = QLabel("Genre:")
        self.genre_value = QLabel()
        self.tarif_label = QLabel("Tarif:")
        self.tarif_value = QLabel()
        self.seances_label = QLabel("Séances:")
        self.seances_value = QLabel()
        self.situation_label = QLabel("Situation:")
        self.situation_value = QLabel()

        # Ajouter deux informations par ligne 
        self.info_layout.addWidget(self.nom_label, 0, 0)
        self.info_layout.addWidget(self.nom_value, 0, 1)
        self.info_layout.addWidget(self.prenom_label, 0, 2)
        self.info_layout.addWidget(self.prenom_value, 0, 3)
        self.info_layout.addWidget(self.email_label, 1, 0)
        self.info_layout.addWidget(self.email_value, 1, 1)
        self.info_layout.addWidget(self.telephone_label, 1, 2)
        self.info_layout.addWidget(self.telephone_value, 1, 3)
        self.info_layout.addWidget(self.cin_label, 2, 0)
        self.info_layout.addWidget(self.cin_value, 2, 1)
        self.info_layout.addWidget(self.num_adh_label, 2, 2)
        self.info_layout.addWidget(self.num_adh_value, 2, 3)
        self.info_layout.addWidget(self.adresse_label, 3, 0)
        self.info_layout.addWidget(self.adresse_value, 3, 1)
        self.info_layout.addWidget(self.date_entree_label, 3, 2)
        self.info_layout.addWidget(self.date_entree_value, 3, 3)
        self.info_layout.addWidget(self.age_label, 4, 0)
        self.info_layout.addWidget(self.age_value, 4, 1)
        self.info_layout.addWidget(self.genre_label, 4, 2)
        self.info_layout.addWidget(self.genre_value, 4, 3)
        self.info_layout.addWidget(self.tarif_label, 5, 0)
        self.info_layout.addWidget(self.tarif_value, 5, 1)
        self.info_layout.addWidget(self.seances_label, 5, 2)
        self.info_layout.addWidget(self.seances_value, 5, 3)
        self.info_layout.addWidget(self.situation_label, 6, 0)
        self.info_layout.addWidget(self.situation_value, 6, 1)

        # Layout pour organiser la photo à droite
        content_layout = QHBoxLayout()
        content_layout.addLayout(self.info_layout)
        content_layout.addWidget(self.photo_label)
        self.modification = QPushButton("Modefier")
        self.modification.clicked.connect(self.medefier)
        content_layout.addWidget(self.modification)

        main_layout.addLayout(content_layout)
        

        row = load_data(self.id_profile) 
        if row:
            self.nom_value.setText(str(row[1]))
            self.prenom_value.setText(row[2])
            self.email_value.setText(row[3])
            self.telephone_value.setText(row[4])
            self.cin_value.setText(row[5])
            self.num_adh_value.setText(row[6])
            self.adresse_value.setText(row[7])
            self.date_entree_value.setText(row[8])
            self.date_entree =  row[8]
            self.age_value.setText(str(row[9]))
            self.genre_value.setText(str(row[10]))
            self.tarif_value.setText(str(row[11]))
            self.seances_value.setText(str(row[12]))
            self.situation_value.setText(str(row[13]))
            print(row[14])
            if row[14] and row[14] != 'Aucune':
                self.photo_label.setPixmap(QPixmap("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/images/logos/profile.png").scaled(150, 150))
            else:
                self.photo_label.setPixmap(QPixmap("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/images/logos/profile.png").scaled(150, 150))
        self.content_layout.addWidget(self.form_widget)
    
    def medefier(self):
        pass
    
    def show_payment_formule(self):
        self.layout = QVBoxLayout(self.form_paiment)

        # Tableau pour afficher les paiements
        self.table_paiements = QTableWidget()
        self.table_paiements.setColumnCount(3)
        self.table_paiements.setHorizontalHeaderLabels(["Mois", "État", "Action"])
        self.table_paiements.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table_paiements)

        self.charger_paiements()

    def charger_paiements(self):
        adherent_id = self.id_profile
        paiements = recuperer_paiements(adherent_id)

        # Générer la liste des mois depuis la date d'entrée jusqu'à aujourd'hui
        self.table_paiements.setRowCount(0)
        current_date = QDate.currentDate()
        current_month = current_date.month()
        current_year = current_date.year()

        # Date d'entrée
        start_date = self.date_entree.split('-')
        print(self.date_entree)
        year = int(start_date[0]) 
        month = int(start_date[1]) 

        while year < current_year or (year == current_year and month <= current_month):
            # Vérifier si le mois est payé
            month_str = f"{year}-{month:02d}"
            is_paid = any(month_str in paiement[2] for paiement in paiements)

            # Ajouter la ligne au tableau
            row_index = self.table_paiements.rowCount()
            self.table_paiements.insertRow(row_index)

            # Colonne Mois
            self.table_paiements.setItem(row_index, 0, QTableWidgetItem(month_str))

            # Colonne État
            etat_item = QTableWidgetItem("Payé" if is_paid else "Non payé")
            etat_item.setBackground(QColor(0, 255, 0) if is_paid else QColor(255, 0, 0))
            self.table_paiements.setItem(row_index, 1, etat_item)

            # Colonne Action
            if not is_paid:
                button = QPushButton("Payer")
                button.clicked.connect(lambda _, m=month_str: self.payer_mois(m))
                button.setEnabled(all(
                    f"{year}-{m:02d}" in [p[2][:7] for p in paiements]
                    for m in range(1, month)
                ))
                self.table_paiements.setCellWidget(row_index, 2, button)

            # Passer au mois suivant
            month += 1
            if month > 12:
                month = 1
                year += 1

    def payer_mois(self, mois):
        """
        Fonction pour payer un mois non payé.
        """
        adherent_id = self.id_profile
        montant = self.montant_input.value()
        mode_paiement = self.mode_paiement_input.currentText()
        commentaire = f"Paiement pour {mois}"

        ajouter_paiement(adherent_id, montant, f"{mois}-01", mode_paiement, commentaire)
        self.charger_paiements()

    def ajouter_paiement(self):
        """
        Ajoute un paiement manuel.
        """
        adherent_id = self.id_profile
        montant = self.montant_input.value()
        date_paiement = self.date_paiement_input.date().toString("yyyy-MM-dd")
        mode_paiement = self.mode_paiement_input.currentText()
        commentaire = self.commentaire_input.text()

        ajouter_paiement(adherent_id, montant, date_paiement, mode_paiement, commentaire)
        self.clear_form()
        self.charger_paiements()

    def clear_form(self):
        self.montant_input.setValue(1)
        self.date_paiement_input.setDate(QDate.currentDate())
        self.mode_paiement_input.setCurrentIndex(0)
        self.commentaire_input.clear()

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
