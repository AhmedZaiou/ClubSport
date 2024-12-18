from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import * 
from .main_interface import MainInterface 
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class Profile():
    def __init__(self, id_profile,main_inter): 
        self.main_inter = main_inter
        self.id_profile = id_profile 
        self.month_to_pay_value = "Paiement déjà effectué"

        self.show_profile_content()

    def show_profile_content(self):
        self.main_inter.clear_content_frame()

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

        table_layout = QHBoxLayout()


        
        # Tableau pour afficher les adhérents avec situation = NON
        self.form_paiment = QWidget()
        self.form_paiment.setObjectName("FormulaireWidget") 
        self.show_payment_formule()
        table_layout.addWidget(self.form_paiment)

        self.confirm_paiment_w = QWidget()
        self.confirm_paiment_w.setObjectName("FormulaireWidget") 
        self.confirm_payment()
        table_layout.addWidget(self.confirm_paiment_w)



        layout.addLayout(table_layout)
        
        self.main_inter.content_layout.addWidget(self.dashbord_widget) 
    
    def show_profile(self): 
        main_layout = QVBoxLayout(self.form_widget)

        # Photo de l'adhérent
        self.photo_label = QLabel()
        self.photo_label.setPixmap(QPixmap("logo.png").scaled(240, 240, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        

        # Informations de l'adhérent
        self.info_layout = QGridLayout()
        

        # Création des labels pour chaque information
        self.nom_label = QLabel("Nom :")
        self.nom_value = QLabel()
        self.prenom_label = QLabel("Prénom :")
        self.prenom_value = QLabel()
        self.email_label = QLabel("Email :")
        self.email_value = QLabel()
        self.telephone_label = QLabel("Téléphone :")
        self.telephone_value = QLabel()
        self.cin_label = QLabel("CIN :")
        self.cin_value = QLabel()
        self.num_adh_label = QLabel("Numéro d'adhérent :")
        self.num_adh_value = QLabel()
        self.adresse_label = QLabel("Adresse :")
        self.adresse_value = QLabel()
        self.date_entree_label = QLabel("Date d'entrée :")
        self.date_entree_value = QLabel()
        self.age_label = QLabel("Âge :")
        self.age_value = QLabel()
        self.genre_label = QLabel("Genre :")
        self.genre_value = QLabel()
        self.tarif_label = QLabel("Tarif :")
        self.tarif_value = QLabel()
        self.seances_label = QLabel("Séances :")
        self.seances_value = QLabel()
        self.situation_label = QLabel("Assurance :")
        self.situation_value = QLabel()

        
        self.poids = QLabel("Poids :")
        self.poids_value = QLabel()

        self.situation_sanitaire = QLabel("Situation sanitaire :")
        self.situation_sanitaire_value = QLabel()

        self.situation_sanitaire_text = QLabel("Maladie :")
        self.situation_sanitaire_text_value = QLabel()

        self.longueur = QLabel("La longueur :")
        self.longueur_value = QLabel()

        self.titre_sport = QLabel("Le titre du sport :")
        self.titre_sport_value = QLabel()


        self.nom_parent = QLabel("Nom du parent :")
        self.nom_parent_value = QLabel()

        self.contact_parent = QLabel("Contact du parent :")
        self.contact_parent_value = QLabel()

 
        self.discipline = QLabel("Discipline :")
        self.discipline_value = QLabel()

        self.numero_assurance = QLabel("Numéro d'assurance:")
        self.numero_assurance_value = QLabel()

        self.centure = QLabel("Centure :")
        self.centure_value = QLabel()

        self.dautre_information = QLabel("Autres informations :")
        self.dautre_information_value = QLabel()



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
        self.info_layout.addWidget(self.titre_sport, 6, 2)
        self.info_layout.addWidget(self.titre_sport_value, 6, 3)

        self.info_layout.addWidget(self.poids, 7, 0)
        self.info_layout.addWidget(self.poids_value, 7, 1)
        self.info_layout.addWidget(self.longueur, 7, 2)
        self.info_layout.addWidget(self.longueur_value, 7, 3)

        self.info_layout.addWidget(self.situation_sanitaire, 8, 0)
        self.info_layout.addWidget(self.situation_sanitaire_value, 8, 1)
        self.info_layout.addWidget(self.situation_sanitaire_text, 8, 2)
        self.info_layout.addWidget(self.situation_sanitaire_text_value, 8, 3)

        self.info_layout.addWidget(self.nom_parent, 9, 0)
        self.info_layout.addWidget(self.nom_parent_value, 9, 1)
        self.info_layout.addWidget(self.contact_parent, 9, 2)
        self.info_layout.addWidget(self.contact_parent_value, 9, 3)

        self.info_layout.addWidget(self.discipline, 10, 0)
        self.info_layout.addWidget(self.discipline_value, 10, 1)
        self.info_layout.addWidget(self.numero_assurance, 10, 2)
        self.info_layout.addWidget(self.numero_assurance_value, 10, 3)

        self.info_layout.addWidget(self.centure, 11, 0)
        self.info_layout.addWidget(self.centure_value, 11, 1)
        self.info_layout.addWidget(self.dautre_information, 11, 2)
        self.info_layout.addWidget(self.dautre_information_value, 11, 3)

        # Layout pour organiser la photo à droite
        content_layout = QHBoxLayout()
        content_layout.addLayout(self.info_layout)
        content_layout.addWidget(self.photo_label)


        button_layout = QVBoxLayout()
        self.modification = QPushButton("Mise à jour")
        self.modification.clicked.connect(self.medefier)
        self.modification.setObjectName('button_vert')
        button_layout.addWidget(self.modification)
        self.ajoutersanction = QPushButton("Ajouter une sanction")
        self.ajoutersanction.clicked.connect(self.ajoutersanction_fc)
        self.ajoutersanction.setObjectName('button_vert')
        button_layout.addWidget(self.ajoutersanction)

        self.ajoutersanction = QPushButton("Ajouter un sinistre")
        self.ajoutersanction.clicked.connect(self.ajoutersinistre_fc)
        self.ajoutersanction.setObjectName('button_vert')
        button_layout.addWidget(self.ajoutersanction)

        self.stopsubscription = QPushButton("Arrêter l'abonnement")
        self.stopsubscription.clicked.connect(self.stopsubscription_fnc)
        self.stopsubscription.setObjectName('button_vert')
        button_layout.addWidget(self.stopsubscription)
        content_layout.addLayout(button_layout)

        main_layout.addLayout(content_layout)
        

        row = load_data(self.id_profile) 
        print(row)
        if row:
            self.nom_value.setText(str(row[1]))
            self.prenom_value.setText(row[2])
            self.nom_value_v = row[2]
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
            self.tarif_abbonement = str(row[11])
            self.monton = int(row[11])
            self.seances_value.setText(str(row[12]))
            self.situation_value.setText(str(row[13]))  
            self.poids_value.setText(str(row[15]))
            self.longueur_value.setText(str(row[16]))
            self.titre_sport_value.setText(str(row[17]))
            self.nom_parent_value.setText(str(row[18]))
            self.contact_parent_value.setText(str(row[19]))
            self.situation_sanitaire_value.setText(str(row[20]))
            self.situation_sanitaire_text_value.setText(str(row[21]))
            self.discipline_value.setText(str(row[23]))
            self.numero_assurance_value.setText(str(row[24]))
            self.centure_value.setText(str(row[25]))
            self.dautre_information_value.setText(str(row[22]))



            if row[14] and row[14] != 'Aucune':
                self.photo_label.setPixmap(QPixmap(row[14]).scaled(150, 150))
            else:
                self.photo_label.setPixmap(QPixmap(str(path_profils_images/"profile.png")).scaled(150, 150))
        self.main_inter.content_layout.addWidget(self.form_widget)
    
    def stopsubscription_fnc(self):

        reponse = QMessageBox.question(
                self.main_inter,
                "Confirmation de la résiliation de l'abonnement.",
                f"Êtes-vous sûr de vouloir annuler l'abonnement de Mr/Mme : {self.nom_value_v } ?",
                QMessageBox.Yes | QMessageBox.No
            )
        if reponse == QMessageBox.Yes:
            dinscription(self.id_profile) 
            QMessageBox.information(self.main_inter, "Confirmation de la résiliation de l'abonnement.", "Confirmation de la résiliation de l'abonnement.")
            from .dashbord import Dashbord
            self.main_interface = Dashbord(self.main_inter)
            
        else:
            QMessageBox.information(self.main_inter, "La résiliation annulé", "La résiliation a été annulée.")
       
        

        
    def ajoutersanction_fc(self):
        from .ajouter_sanction import Sanction
        self.main_interface = Sanction(self.main_inter, self.id_profile)
    def ajoutersinistre_fc(self):
        from .gestion_sinistre import Sinistre
        self.main_interface = Sinistre(self.main_inter, self.id_profile, self.num_adh_value.text()) 
    
    def medefier(self):
        from .modefier_information import ModefierADh
        self.main_interface = ModefierADh(self.main_inter, self.id_profile) 
    
    def show_payment_formule(self):
        self.layout = QVBoxLayout(self.form_paiment)
        # Tableau pour afficher les paiements
        self.table_paiements = QTableWidget()
        self.table_paiements.setColumnCount(4)
        self.table_paiements.setHorizontalHeaderLabels(["Moi concerné","Montant","Mode de paiement","Date de paiement"])


        self.table_paiements.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table_paiements)

        self.charger_paiements()

    def charger_paiements(self):
        adherent_id = self.id_profile
        paiements = recuperer_paiements(adherent_id)
        
        if len(paiements) >0:
            print(paiements[-1])
            date_laste_paiment = paiements[-1][1].split("-")
            year_last_paiment,moi_last_paiment = int(date_laste_paiment[0]),int(date_laste_paiment[1])
        else:
            start_date = self.date_entree.split('-') 
            year_last_paiment,moi_last_paiment = int(start_date[0]),int(start_date[1])
            year_last_paiment,moi_last_paiment  = decrement_month(year_last_paiment,moi_last_paiment)
         

        # Générer la liste des mois depuis la date d'entrée jusqu'à aujourd'hui
        self.table_paiements.setRowCount(0)
        current_date = QDate.currentDate()
        current_month = current_date.month()
        current_year = current_date.year()

        year,month = year_last_paiment, moi_last_paiment
        self.year_last_paiment, self.moi_last_paiment = year_last_paiment, moi_last_paiment

        list_pa = []

        while (year <= current_year and month <= current_month) or (year == current_year and month <= current_month):
             
            list_pa.append((f'{year}-{month}-01', str(self.monton), str("Espèces")))
            year,month = increment_month(year, month)
        
        

        for ind in range(len(list_pa)-1,0,-1):
            data = list_pa[ind]
            row_index = self.table_paiements.rowCount()
            self.table_paiements.insertRow(row_index)
            self.table_paiements.setItem(row_index, 0, QTableWidgetItem(data[0]))
            self.table_paiements.setItem(row_index, 1, QTableWidgetItem(data[1]))
            self.table_paiements.setItem(row_index, 2, QTableWidgetItem(data[2]))
            
            if ind != 1:
                etat_item = QTableWidgetItem(str("En retard"))
                etat_item.setBackground(QColor(200, 200, 255))  
            else:
                etat_item = QTableWidgetItem(str("Payer"))
                etat_item.setBackground(QColor(255, 0, 0))  
                self.month_to_pay_value = data[0]

            etat_item.setForeground(Qt.blue)
            etat_item.setTextAlignment(Qt.AlignCenter)
            etat_item.setData(Qt.UserRole,str(data[0]))  
            self.table_paiements.setItem(row_index, 3, etat_item)

 
        for ind in range(len(paiements)-1,-1,-1):
            data = paiements[ind]
            # Ajouter la ligne au tableau
            row_index = self.table_paiements.rowCount()
            self.table_paiements.insertRow(row_index)

            # Colonne Mois
            self.table_paiements.setItem(row_index, 0, QTableWidgetItem(str(data[1])))
            self.table_paiements.setItem(row_index, 1, QTableWidgetItem(str(data[2])))
            self.table_paiements.setItem(row_index, 2, QTableWidgetItem(str(data[3])))
            etat_item = QTableWidgetItem(str(data[4]))
            etat_item.setBackground(QColor(0, 255, 0))
            self.table_paiements.setItem(row_index, 3, etat_item)
        #self.table_paiements.cellClicked.connect(self.payer_mois)
        
         
    
    def payer_mois(self,row, column ):
        """
        Fonction pour payer un mois non payé.
        """
        if column == 3: 
            adherent_id = self.table_paiements.item(row, column).data(Qt.UserRole)
            
            self.month_to_pay.setText(adherent_id)
            self.monton_to_pay.setText(str(self.monton))
            self.month_to_pay_value = adherent_id 
        else:
            QMessageBox.warning(self.main_inter, "Champs manquants", "Veuillez remplir tous les champs obligatoires.")
            
         

    def ajouter_paiement(self):
        """
        Ajoute un paiement manuel.
        """
        if self.month_to_pay_value != "Paiement déjà effectué":
            reponse = QMessageBox.question(
                self.main_inter,
                "Confirmation de paiement",
                f"Êtes-vous sûr de vouloir payer le mois :{self.month_to_pay_value } ?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reponse == QMessageBox.Yes:
                adherent_id = self.id_profile
                montant = self.monton
                date = QDate.currentDate().toString("yyyy-MM-dd").split('-') 
                date_paiement = str(date[0])+'-'+str(date[1])+'-'+str( date[2])
                mode_paiement = 'Espèces'
                month_to_pay = self.month_to_pay_value  

                ajouter_paiement(adherent_id, montant, date_paiement, mode_paiement, month_to_pay)
                self.telecharger_facture(adherent_id, montant, date_paiement, mode_paiement, month_to_pay)
                QMessageBox.information(self.main_inter, "Paiement validé", "Le paiement a été confirmé avec succès.")
                self.main_interface = Profile(adherent_id, self.main_inter)
            else:
                QMessageBox.information(self.main_inter, "Paiement annulé", "Le paiement a été annulée.")
        else:
            QMessageBox.information(self.main_inter, "Paiement déjà effectué", "Paiement déjà effectué.")


        
        

 
 
    def telecharger_facture(self, adherent_id, montant, date_paiement, mode_paiement, month_to_pay):
        # Nom du fichier PDF à générer
        fichier_pdf = f"Facture_Adherent_{adherent_id}.pdf"



        options = QFileDialog.Options()
        fichier_pdf, _ = QFileDialog.getSaveFileName(
            self.main_inter,
            "Enregistrer le fichier",
            f"Facture_{self.nom_value.text()}-{self.prenom_value.text()}-{month_to_pay}.pdf",
            "Documents (*.pdf);;All Files (*)",
            options=options
        )
        if not fichier_pdf:
            QMessageBox.information(self.main_inter, "Le téléchargement est annulé.", "Le téléchargement est annulé.")
            return  
        
        
        # Créer le canvas pour le PDF
        c = canvas.Canvas(fichier_pdf, pagesize=A4)
        largeur, hauteur = A4  # Dimensions de la page
        
        # Ajouter le titre
        c.setFont("Helvetica-Bold", 20)
        c.drawString(200, hauteur - 50, "FACTURE Royal Fitness")
        
        # Ajouter les informations générales
        c.setFont("Helvetica", 12)
        c.drawString(50, hauteur - 100, f"Adhérent : {self.prenom_value.text()} {self.nom_value.text()}")
        c.drawString(50, hauteur - 130, f"Montant : {montant} Dhs")
        c.drawString(50, hauteur - 160, f"Date de Paiement : {date_paiement}")
        c.drawString(50, hauteur - 190, f"Mode de Paiement : {mode_paiement}")
        c.drawString(50, hauteur - 220, f"Mois payé : {month_to_pay}")
        
        # Ajouter une ligne horizontale
        c.line(50, hauteur - 250, largeur - 50, hauteur - 250)
        
        # Ajouter un message de remerciement
        c.setFont("Helvetica-Oblique", 14)
        c.setFillColorRGB(0, 0.5, 0)  # Couleur verte
        c.drawString(50, hauteur - 300, "Merci pour votre paiement !")
        
        # Ajouter les coordonnées pour l'assistance
        c.setFont("Helvetica", 10)
        c.setFillColorRGB(0, 0, 0)  # Noir
        c.drawString(50, hauteur - 350, "Pour toute assistance, contactez-nous directement") 
        
        # Ajouter la date de génération de la facture
        c.setFont("Helvetica", 10)
        c.drawString(50, 50, f"Facture générée le : {datetime.now().strftime('%d/%m/%Y')}")

        # Enregistrer et fermer le fichier PDF
        c.save()
        print(f"Facture générée avec succès : {fichier_pdf}")



    def confirm_payment(self): 

        
        # Create the main layout for the confirmation window
        self.layout_confim = QVBoxLayout(self.confirm_paiment_w)

        # Layout for last payment info (centered message)
        self.info_layout_c1 = QGridLayout()
        last_payment_info = QLabel(f"Effectuer un paiement ") 
        last_payment_info.setAlignment(Qt.AlignCenter)  # Center the label text
        last_payment_info1 = QLabel(f" Dernier paiement : {self.moi_last_paiment if self.moi_last_paiment >10 else '0'+str(self.moi_last_paiment ) }-{self.year_last_paiment}") 
        last_payment_info1.setAlignment(Qt.AlignCenter)  # Center the label text
        self.info_layout_c1.addWidget(last_payment_info, 0, 0, Qt.AlignCenter)
        self.info_layout_c1.addWidget(last_payment_info1, 1, 0, Qt.AlignCenter)
        self.info_layout_c1.setVerticalSpacing(5)
        self.layout_confim.addLayout(self.info_layout_c1)

        # Layout for payment info
        self.info_layout_c = QGridLayout()

        # Adding labels and corresponding widgets to the payment info layout
        self.add_label_to_layout(self.info_layout_c, "Moi concerné : ", 0, 0)
        self.month_to_pay = QLabel()
        self.add_widget_to_layout(self.info_layout_c, self.month_to_pay, 0, 1)
        
        self.add_label_to_layout(self.info_layout_c, "Montant : ", 1, 0)
        self.monton_to_pay = QLabel()
        self.add_widget_to_layout(self.info_layout_c, self.monton_to_pay, 1, 1)

        self.month_to_pay.setText(self.month_to_pay_value)
        self.monton_to_pay.setText(self.tarif_abbonement)

        self.add_label_to_layout(self.info_layout_c, "Mode de paiement : ", 2, 0)
        self.add_label_to_layout(self.info_layout_c, "Espèces", 2, 1)

        # Set alignment and spacing for better visual balance
        self.info_layout_c.setHorizontalSpacing(10)
        self.info_layout_c.setVerticalSpacing(5)

        # Confirm button setup
        self.confirmation = QPushButton("Confirmer")
        self.confirmation.clicked.connect(self.ajouter_paiement)
        self.confirmation.setObjectName('button_vert')
        # Adding sub-layouts to the main layout
        self.layout_confim.addLayout(self.info_layout_c)
        self.layout_confim.addWidget(self.confirmation)

        

        # Helper method for adding labels to a layout
    def add_label_to_layout(self, layout, text, row, col):
            label = QLabel(text)
            label.setAlignment(Qt.AlignLeft)  # Align labels to the right for a cleaner look
            layout.addWidget(label, row, col)

        # Helper method for adding widgets to a layout
    def add_widget_to_layout(self, layout, widget, row, col):
            layout.addWidget(widget, row, col)


        
 