from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import * 
from .main_interface import MainInterface

import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from tempfile import NamedTemporaryFile

from matplotlib.ticker import FuncFormatter

 

class Salarie( ):
    def __init__(self,main_inter): 
       self.main_inter = main_inter
       self.show_dashboard_inter()
    
    def show_dashboard_inter(self):
        self.main_inter.clear_content_frame()

        self.dashbord_widget = QWidget()
        self.dashbord_widget.setObjectName("dashbord_widget")

        # Layout principal
        layout = QVBoxLayout(self.dashbord_widget)
        
        # Layouts horizontaux pour les graphiques
        graphs_layout = QHBoxLayout()
 
        # Page de connexion
        self.login_frame = QFrame() 
        self.login_frame.setObjectName("depenseframe")

        # Layout de la frame de connexion
        self.login_layout = QVBoxLayout(self.login_frame)

        self.connexion = QLabel("Ajouter un salarié")
        self.connexion.setObjectName('depenseslab')
        self.login_layout.addWidget(self.connexion )

        self.user_label = QLabel("Nom et Prénom:")
        self.login_layout.addWidget(self.user_label)

        self.user_entry = QLineEdit()
        self.user_entry.setPlaceholderText("Nom et Prénom")
        self.login_layout.addWidget(self.user_entry)

        self.password_label = QLabel("Contact :")
        self.login_layout.addWidget(self.password_label)

        self.user_contact = QLineEdit()
        self.user_contact.setPlaceholderText("Contact")
        self.login_layout.addWidget(self.user_contact)

        self.salaire_label = QLabel("Salaire en Dhs")
        self.login_layout.addWidget(self.salaire_label)

        self.salaire = QSpinBox()
        self.salaire.setRange(1, 214748364)
        self.salaire.setValue(0)
        self.login_layout.addWidget(self.salaire)



        self.salaire_admin = QLabel("C'est un admin ?")
        self.login_layout.addWidget(self.salaire_admin)

        self.salaire_admin_value = QComboBox()
        self.salaire_admin_value.addItems(["Non","Oui"])  
        self.login_layout.addWidget(self.salaire_admin_value)

        self.motdepasse = QLabel("Mot de passe :")
        self.login_layout.addWidget(self.motdepasse)

        self.motdepasse_value = QLineEdit()
        self.motdepasse_value.setPlaceholderText("Mot de passe")
        self.motdepasse_value.setEchoMode(QLineEdit.Password) 
        self.login_layout.addWidget(self.motdepasse_value)
 
 
  

        self.login_button = QPushButton("Ajouter le salarié")
        self.login_button.clicked.connect(self.ajouter_salarie)
        self.login_button.setObjectName("buttconexion")
        self.login_layout.addWidget(self.login_button)


        self.rapportSalarie = QPushButton("Télécharger le rapport des paiements")
        self.rapportSalarie.clicked.connect(self.rapport_salarie)
        self.rapportSalarie.setObjectName("buttconexion")
        self.login_layout.addWidget(self.rapportSalarie)

        graphs_layout.addWidget(self.login_frame)












        # Page de connexion
        self.login_admin = QFrame() 
        self.login_admin.setObjectName("depenseframe")

        # Layout de la frame de connexion
        self.ladmin_layout = QVBoxLayout(self.login_admin)

        self.connexion_admin = QLabel("Salarié concerné")
        self.connexion_admin.setObjectName('depenseslab')
        self.ladmin_layout.addWidget(self.connexion_admin  )

        self.user_label_admin  = QLabel("Mois concerné:")
        self.ladmin_layout.addWidget(self.user_label_admin )

        self.user_entry_admin  = QDateEdit() 
        self.user_entry_admin.setDate(QDate.currentDate())
        self.ladmin_layout.addWidget(self.user_entry_admin )

        self.password_label = QLabel("Montant du paiement :")
        self.ladmin_layout.addWidget(self.password_label)

        self.user_contact_admin = QSpinBox() 
        self.user_contact_admin.setRange(1, 214748364)
        self.user_contact_admin.setValue(0)
        self.ladmin_layout.addWidget(self.user_contact_admin)

        self.salaire_label_admin = QLabel("Commentaire :")
        self.ladmin_layout.addWidget(self.salaire_label_admin)

        self.commentaire = QLineEdit()
        self.commentaire.setPlaceholderText("Commentaire")
        self.ladmin_layout.addWidget(self.commentaire)
 
  

        self.login_button_admin= QPushButton("Payer le salarié")
        self.login_button_admin.clicked.connect(self.payer_salarie)
        self.login_button_admin.setObjectName("buttconexion")
        self.ladmin_layout.addWidget(self.login_button_admin)

        self.nvMotdepass_admin = QLabel("Nouveau mot de passe  :")
        self.ladmin_layout.addWidget(self.nvMotdepass_admin)

        self.nvMotdepass_admin_value = QLineEdit()
        self.nvMotdepass_admin_value.setPlaceholderText("Nouveau mot de passe ")
        self.nvMotdepass_admin_value.setEchoMode(QLineEdit.Password)
        self.ladmin_layout.addWidget(self.nvMotdepass_admin_value)

        self.modefier_admin= QPushButton("Modifier le mot de passe")
        self.modefier_admin.clicked.connect(self.update_motdepass)
        self.modefier_admin.setObjectName("buttconexion")
        self.ladmin_layout.addWidget(self.modefier_admin)

        self.supprimer_admin= QPushButton("Supprimer le salarié")
        self.supprimer_admin.clicked.connect(self.supprimer_salarie)
        self.supprimer_admin.setObjectName("buttconexion")
        self.ladmin_layout.addWidget(self.supprimer_admin)

        graphs_layout.addWidget(self.login_admin)





        # Ajout des graphiques au layout principal 
        # Tableau pour afficher les adhérents avec situation = NON

        titre_table = QLabel('Liste des salariés :')
        titre_table.setObjectName("titre_table")
        layout.addWidget(titre_table)

        # Search bar for filtering
        self.search_bar = QLineEdit(self.main_inter)
        self.search_bar.setPlaceholderText("Chercher par 'Nom'...")
        self.search_bar.textChanged.connect(self.filter_table)  # Trigger filter when text changes
        layout.addWidget(self.search_bar)

        self.tableWidget = QTableWidget()
        self.populate_table()  
        layout.addWidget(self.tableWidget)
        layout.addLayout(graphs_layout) 


        self.main_inter.content_layout.addWidget(self.dashbord_widget) 
    
    def update_motdepass(self):

        nvpassword = self.nvMotdepass_admin_value.text()
        try:
            if nvpassword is not None: 
                reponse = QMessageBox.question(
                    self.main_inter,
                    "Confirmer la modification du mot de passe",
                    f"Êtes-vous sûr de vouloir modifier le mot de passe de :{self.nom_prenom} ?",
                    QMessageBox.Yes | QMessageBox.No
                )
                if reponse == QMessageBox.Yes:  
                    update_salarie_password(self.salarie_id, nvpassword) 
                    QMessageBox.information(self.main_inter, "Modification validée", "La modification a été confirmé avec succès.")
                    self.main_interface = Salarie(self.main_inter)
                else:
                    QMessageBox.information(self.main_inter, "Modification annulée", "La modification a été annulée.")
            else:
                QMessageBox.warning(self.main_inter, "Champs manquants", "Veuillez remplir tous les champs obligatoires.")
        except:
            QMessageBox.warning(self.main_inter, "Champs manquants", "Veuillez sélectionner un salarié.")

    def payer_salarie(self): 
        commentaire = self.commentaire.text()
        date_c = self.user_entry_admin.date().toString("yyyy-MM-dd")
        salaire = self.user_contact_admin.value()

        try:
            if not commentaire or not date_c or not salaire or not self.nom_prenom:
                QMessageBox.warning(self.main_inter, "Champs manquants", "Veuillez remplir tous les champs obligatoires.")
                return
            

        
            reponse = QMessageBox.question(
                self.main_inter,
                "Confirmer le paiement de mois",
                f"Êtes-vous sûr de vouloir payer le mois :{date_c} pour {self.nom_prenom} ?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reponse == QMessageBox.Yes:  
                insertpaySalarie(self.nom_prenom,commentaire, salaire,date_c)
                update_salarie_lastpay(self.salarie_id, date_c)
                QMessageBox.information(self.main_inter, "Paiement confirmé", "Le Paiement a été confirmé avec succès.")
                self.main_inter = Salarie(self.main_inter)
            else:
                QMessageBox.information(self.main_inter, "Paiement annulé", "Le paiement a été annulé.")
        except:
            QMessageBox.warning(self.main_inter, "Champs manquants", "Veuillez sélectionner un salarié.")




        
        

 
    def supprimer_salarie(self):

        try:
            reponse = QMessageBox.question(
                self.main_inter,
                "Confirmer la suppression ",
                f"Êtes-vous sûr de vouloir supprimer le salarié {self.nom_prenom} ?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reponse == QMessageBox.Yes:  
                supprimer_salarie(self.salarie_id) 
                QMessageBox.information(self.main_inter, "Suppression confirmé", "La auppression a été confirmé avec succès.")
                self.main_inter = Salarie(self.main_inter)
            else:
                QMessageBox.information(self.main_inter, "Suppression annulé", "La Suppression a été annulé.")
        except:
            QMessageBox.warning(self.main_inter, "Champs manquants", "Veuillez sélectionner un salarié.")
        


    def ajouter_salarie(self): 
        nom_prenom = self.user_entry.text()
        contact = self.user_contact.text()
        salaire = self.salaire.value() 
        admin = self.salaire_admin_value.currentText()
        password =self.motdepasse_value.text() 

        if not nom_prenom or not contact or not salaire:
                QMessageBox.warning(self.main_inter, "Champs manquants", "Veuillez remplir tous les champs obligatoires.")
                return 
        if admin == "Oui" and not password:
            QMessageBox.warning(self.main_inter, "Champs manquants", "Veuillez saisir le mot de passe ou mettre admin sur non.")
            return 
        insertSalarie(nom_prenom, contact, salaire, admin, password)
        self.main_interface = Salarie( self.main_inter)


    def filter_table(self):
        #if not self.all_data:
        #    self.load_all_data()
        # Get the filter text from the search bar
        filter_text = self.search_bar.text().lower()

        # Loop through all rows and hide/show them based on the search
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 0)  # Assuming column 0 is 'Nom'
            if item is not None:
                if filter_text in item.text().lower():  # Case-insensitive comparison
                    self.tableWidget.setRowHidden(row, False)
                else:
                    self.tableWidget.setRowHidden(row, True)
                


 
    def plot_revenue_graph(self):
        """Affiche les revenus mensuels pour l'année en cours avec le total annuel"""
        
        # Filtrer les données pour l'année en cours
        current_year = datetime.now().year 
        data, total_revenue = recuperer_stat_depenses()
        revenue_by_month = pd.Series(data) 
        ax = self.revenue_canvas.figure.add_subplot(111)
        self.revenue_canvas.figure.set_facecolor((0, 0, 0, 0.1))
        ax.clear()
        ax.set_facecolor((0, 0, 0, 0.1))
        revenue_by_month.plot(kind="bar", ax=ax, color="firebrick", alpha=0.75)
        ax.set_title(f"Dépenses Mensuels ({current_year}) - Total : {total_revenue} Dhs",  color='white',  fontsize=16) 
        ax.set_ylabel("Dépenses (Dhs)",  color='white',  fontsize=16) 
        ax.tick_params(axis='x', colors='white')  # Ticks de l'axe X en noir
        ax.tick_params(axis='y', colors='white')

        self.revenue_canvas.figure.subplots_adjust(left=0.2, right=0.9, top=0.85, bottom=0.25)
        for label in ax.texts:
            label.set_color('white')
            label.set_fontsize(14)
        self.revenue_canvas.draw()

    def populate_table(self):
        """Charge les adhérents dans le tableau avec des fonctionnalités supplémentaires"""
        # Connexion à la base de données SQLite
        
        self.depenses = fetch_salaeir() 
        
        # Effacer les anciennes lignes dans le tableau
        self.tableWidget.setColumnCount(7)  # Nombre de colonnes affichées
        self.tableWidget.setHorizontalHeaderLabels([
            'Nom et Prénom', "Contact",'Salaire', "Date d'entrer","Dernier paiement", "Admin", "Action"
        ])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.tableWidget.setRowCount(10)

        #self.all_data = False  # Nombre de lignes visibles à chaque fois 
        #self.tableWidget.verticalScrollBar().valueChanged.connect(self.on_scroll)

        # Ajouter les adhérents dans le tableau
        for  row_index, adherent in enumerate(self.depenses):
            self.tableWidget.insertRow(row_index)

            # Ajouter les données dans les colonnes respectives
            for col_index, data in enumerate(adherent[1:]):  # Exclure 'id' pour l'affichage
                
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_index, col_index, item) 
            
            action_item = QTableWidgetItem("Traiter")
            action_item.setForeground(QColor('white'))
            action_item.setTextAlignment(Qt.AlignCenter)
            action_item.setData(Qt.UserRole, adherent[0])  # Stocker l'ID de l'adhérent pour le traitement
            action_item.setBackground(QColor(0, 0, 255))  # Vert
            self.tableWidget.setItem(row_index, 6, action_item)
        
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)
        
     
    def on_cell_clicked(self, row, column):
        # Si la colonne 12 (Action) est cliquée
        if column == 6 and  self.tableWidget.item(row, column) is not None:
            self.salarie_id = self.tableWidget.item(row, column).data(Qt.UserRole)  

            self.nom_prenom = self.tableWidget.item(row, 0).text()
            montant = self.tableWidget.item(row, 2).text()
            last = self.tableWidget.item(row, 4).text()
            last_date = QDate.fromString(last, "yyyy-MM-dd")
            date_to_pay = last_date.addMonths(1)
            self.connexion_admin.setText(self.nom_prenom)
            self.user_contact_admin.setValue(int(montant))
            self.user_entry_admin.setDate(date_to_pay) 


            


        
 
        


    



    def generer_graphe_evolution(self, revenue_by_month,depense_by_month): 


        # Création de la figure et de l'axe
        fig, ax = plt.subplots(figsize=(10, 6))

        # Personnalisation de la figure et de l'axe 
        if len(revenue_by_month) ==0 and len(depense_by_month) == 0:
            data = {
                    'date': ['2024-12', '2024-11'],   
                    'montant': [0, 0]  
                } 
            df = pd.DataFrame(data) 
            df.set_index('date', inplace=True) 
            result = pd.Series(data=df['montant'].values, index=df.index)  
            revenue_by_month = result
            depense_by_month = result

            # Tracer les revenus mensuels
        revenue_by_month.plot(kind="line", ax=ax, color="lightgreen", alpha=0.75, label= "Revenues")
        depense_by_month.plot(kind="line", ax=ax, color="firebrick", alpha=0.75, label= "Dépenses")
        
        # Ajouter le titre et l'étiquette de l'axe Y
        ax.set_title("Revenus et dépenses mensuels", fontsize=16)
        ax.set_ylabel("Situation en Dhs",  fontsize=16)
 

        # Formatage des valeurs sur l'axe Y
        formatter = FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", " "))
        ax.yaxis.set_major_formatter(formatter)

        # Ajustement des marges
        fig.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.25)
        ax.legend()
 

        image_stream = BytesIO()
        fig.savefig(image_stream, format='png')
        image_stream.seek(0)
        temp_image_file = NamedTemporaryFile(delete=False, suffix='.png')
        image_path = temp_image_file.name
        fig.savefig(image_path, format='png')
        temp_image_file.close()
        return image_path



    def rapport_salarie(self):
    
        
        
        options = QFileDialog.Options()
        output_pdf, _ = QFileDialog.getSaveFileName(
            self.main_inter,
            "Enregistrer le fichier",
            f"rapport-historique-salaries-{datetime.now()}.pdf",
            "Documents (*.pdf);;All Files (*)",
            options=options
        )
        if not output_pdf:
            QMessageBox.information(self.main_inter, "Le téléchargement est annulé.", "Le téléchargement est annulé.")
            return 

        # Création d'un objet Canvas pour générer le PDF
        c = canvas.Canvas(output_pdf, pagesize=letter)

        # Ajout de texte dans le PDF
        c.setFont("Helvetica", 11)  
        ventes = recuperer_all_paysalaries()
        
        page = 1
        nombre_pages = int(len(ventes)/31) if len(ventes)%31 ==0. else int(len(ventes)/31)+1 
        
        c.drawString(100, 710, f"Rapport sur les paiements des salariés : {datetime.now()}. (page {page}/{nombre_pages}).")
        c.line(100, 690, 500, 690)  
        c.setFont("Helvetica", 11)
        page_height = 680
        line_height = 15
        x = 100
        y=680

         
        
        for idx, non_payment in enumerate(ventes, start=1):
            # Vérifier si une nouvelle page est nécessaire
            if y < 50:  # Espace insuffisant, créer une nouvelle page
                c.showPage() 
                page+=1 
                c.setFont("Helvetica", 11)
                c.drawString(100, 700, f"Rapport sur les paiements des salariés : {datetime.now()}. (page {page}/{nombre_pages}).")
                c.line(100, 690, 500, 690)  
                y = page_height  
            c.drawString(100, y-15, f"Nom et Prénom      : {non_payment[1]}") 
            c.drawString(100, y-30, f"Commentaire        :  {non_payment[2]}") 
            c.drawString(100, y-45, f"Salaire            : {non_payment[3]} dhs ") 
            c.drawString(100, y-60, f"Mois payer         : {non_payment[4]}") 
            c.drawString(100, y-75,f"Date de paiement   : {non_payment[5]}")  
            c.line(100, y-90, 500, y-90)  
 
            y -= 6 *line_height  # Passer à la ligne suivante
        c.save()

    
    

             
            


    