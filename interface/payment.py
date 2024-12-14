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

 

class Payment( ):
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

        self.connexion = QLabel("Ajouter une dépense")
        self.connexion.setObjectName('depenseslab')
        self.login_layout.addWidget(self.connexion )

        self.user_label = QLabel("Commentaire de la dépense :")
        self.login_layout.addWidget(self.user_label)

        self.user_entry = QLineEdit()
        self.user_entry.setPlaceholderText("Entrez votre commentaire")
        self.login_layout.addWidget(self.user_entry)

        self.password_label = QLabel("Valeur de la dépense en Dh :")
        self.login_layout.addWidget(self.password_label)

        self.password_entry = QSpinBox()
        self.password_entry.setRange(1, 214748364)
        self.password_entry.setValue(0)
        self.login_layout.addWidget(self.password_entry)

        self.password_label = QLabel("Date de la dépense :")
        self.login_layout.addWidget(self.password_label)

        self.date_entree_input = QDateEdit()
        self.date_entree_input.setDate(QDate.currentDate())

        self.login_layout.addWidget(self.date_entree_input)

        self.login_button = QPushButton("Ajouter La dépense")
        self.login_button.clicked.connect(self.ajouter_depenses)
        self.login_button.setObjectName("buttconexion")
        self.login_layout.addWidget(self.login_button)

        graphs_layout.addWidget(self.login_frame)





 
        
        # Graphique 2 : Revenus mensuels pour cette année
        self.revenue_canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.revenue_canvas.setObjectName("dashbord_graphe")
        self.plot_revenue_graph()
        graphs_layout.addWidget(self.revenue_canvas)
        
        # Ajout des graphiques au layout principal
        layout.addLayout(graphs_layout)
        
        # Tableau pour afficher les adhérents avec situation = NON

        titre_table = QLabel('Les dépenses :')
        titre_table.setObjectName("titre_table")
        layout.addWidget(titre_table)

        # Search bar for filtering
        self.search_bar = QLineEdit(self.main_inter)
        self.search_bar.setPlaceholderText("Chercher par 'Date'...")
        self.search_bar.textChanged.connect(self.filter_table)  # Trigger filter when text changes
        layout.addWidget(self.search_bar)

        self.tableWidget = QTableWidget()
        self.populate_table()  
        layout.addWidget(self.tableWidget)



        rapport_mont = QHBoxLayout()

        # Bouton de sélection de photo
        self.rapport_month = QPushButton("Extraire le rapport du mois")
        self.rapport_month.clicked.connect(self.rapport_month_fc)
        self.rapport_month.setObjectName("buttonExtraction") 

        # Bouton de sélection de photo
        self.rapport_year = QPushButton("Extraire le rapport de l'année")
        self.rapport_year.clicked.connect(self.rapport_year_fc)
        self.rapport_year.setObjectName("buttonExtraction")         

        
        self.date_entree_input = QDateEdit()
        self.date_entree_input.setDate(QDate.currentDate())
        rapport_mont.addWidget(self.rapport_month)
        rapport_mont.addWidget(self.rapport_year)
        rapport_mont.addWidget(self.date_entree_input)   
        layout.addLayout(rapport_mont )
        
        
        self.main_inter.content_layout.addWidget(self.dashbord_widget) 
    


    def ajouter_depenses(self): 
        datae_depense = self.date_entree_input.date().toString("yyyy-MM-dd")
        commentaire = self.user_entry.text() 
        montant = self.password_entry.value()


        if not datae_depense or not commentaire or not montant :
            QMessageBox.warning(self.main_inter, "Champs manquants", "Veuillez remplir tous les champs obligatoires.")
            return
        reponse = QMessageBox.question(
                self.main_inter,
                "Confirmation de l'ajout de dépenses",
                f"Êtes-vous sûr de vouloir ajouter la dépense  :{commentaire } ?",
                QMessageBox.Yes | QMessageBox.No
            )
        if reponse == QMessageBox.Yes:
            insertion_depense(commentaire, montant, datae_depense)
            self.main_interface = Payment( self.main_inter)
        else:
            QMessageBox.information(self.main_inter, "Action annulé", "L'action a été annulée.")


    def filter_table(self):
        #if not self.all_data:
        #    self.load_all_data()
        # Get the filter text from the search bar
        filter_text = self.search_bar.text().lower()

        # Loop through all rows and hide/show them based on the search
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 2)  # Assuming column 0 is 'Nom'
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
        
        self.depenses = fetch_depenses() 
        
        # Effacer les anciennes lignes dans le tableau
        self.tableWidget.setColumnCount(3)  # Nombre de colonnes affichées
        self.tableWidget.setHorizontalHeaderLabels([
            'Commentaire', 'Montant', 'Date'
        ])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.tableWidget.setRowCount(10)

        #self.all_data = False  # Nombre de lignes visibles à chaque fois 
        #self.tableWidget.verticalScrollBar().valueChanged.connect(self.on_scroll)

        self.load_table()  
        # Connecter l'événement de clic pour traiter un adhérent 
    
    
    def load_table(self):

        # Ajouter les adhérents dans le tableau
        for  row_index, adherent in enumerate(self.depenses):
            self.tableWidget.insertRow(row_index)

            # Ajouter les données dans les colonnes respectives
            for col_index, data in enumerate(adherent[1:]):  # Exclure 'id' pour l'affichage
                
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_index, col_index, item) 
    def rapport_month_fc(self): 
        date = self.date_entree_input.date().toPyDate() 
        
        #graphe porcentage de paiment
        # Liste Dépenses et liste payment, list de non payment 
        # Chemin du fichier PDF de sortie

        nbr_adh,nbr_pyment = recuperer_porcentage_paiment_date(date) 
        if nbr_adh ==0 :
            nbr_adh=1 

        image_path = self.generer_graphe_situation(nbr_adh,nbr_pyment, date)

        
        options = QFileDialog.Options()
        output_pdf, _ = QFileDialog.getSaveFileName(
            self.main_inter,
            "Enregistrer le fichier",
            f"rapport-{date}.pdf",
            "Documents (*.pdf);;All Files (*)",
            options=options
        )
        if not output_pdf:
            QMessageBox.information(self.main_inter, "Le téléchargement est annulé.", "Le téléchargement est annulé.")
            return 

        # Création d'un objet Canvas pour générer le PDF
        c = canvas.Canvas(output_pdf, pagesize=letter)

        # Ajout de texte dans le PDF
        c.setFont("Helvetica", 16)
        c.drawString(100, 700, f"Rapport du mois {date}.")
        
        c.line(100, 680, 500, 680)
        c.setFont("Helvetica", 12) 
        introduction = f"""Ce rapport présente les statistiques des paiements pour le mois {date}. \nIl vise à fournir une vue d’ensemble des performances financières du club, \nen mettant en lumière les paiements effectués, les paiements en attente, \nainsi que des suggestions pour améliorer ces indicateurs."""
        introduction_list=introduction.split("\n") 
        for index, text in enumerate(introduction_list):
            c.drawString(100, 660-(index*20), text)


        c.drawImage(image_path, 190, 340, width=250, height=250) 

        c.setFont("Helvetica", 14) 
        # Ajouter du texte à différentes positions
        c.drawString(100, 320, f"Statistiques clés.")
        c.setFont("Helvetica", 12) 
        c.drawString(120, 280, f"Nombre total d'inscrits : {nbr_adh}.")
        c.drawString(120, 260, f"Paiements effectués : {nbr_pyment} (soit {(nbr_pyment/nbr_adh)*100}%)")
        c.drawString(120, 240, f"Paiements en attente: {nbr_adh-nbr_pyment} (soit {(1-(nbr_pyment/nbr_adh))*100}%)")
        c.drawString(100, 200, f"Liste des paiements et des non-paiements figurant dans les pages suivantes")
        c.showPage()

        non_payments = fetch_data_Non_all()
        c.setFont("Helvetica", 16)
        page = 1
        nombre_pages = int(len(non_payments)/31) if len(non_payments)%31 ==0. else int(len(non_payments)/31)+1 
        c.drawString(100, 700, f"Liste des non-paiements (page {page}/{nombre_pages}).")
        c.line(100, 680, 500, 680) 
        c.setFont("Helvetica", 12)
        page_height = 660
        line_height = 20
        x = 100
        y=660
        
        for idx, non_payment in enumerate(non_payments, start=1):
            # Vérifier si une nouvelle page est nécessaire
            if y < 50:  # Espace insuffisant, créer une nouvelle page
                c.showPage() 
                page+=1 
                c.setFont("Helvetica", 16)
                c.drawString(100, 700, f"Liste des non-paiements  (page {page}/{nombre_pages}).")
                c.line(100, 680, 500, 680)
                y = page_height  
            
            # Ajouter l'élément de la liste
            c.drawString(x, y, f"{idx}. {non_payment[1]} {non_payment[2]}")
            y -= line_height  # Passer à la ligne suivante
        

        c.showPage()

        non_payments = fetch_data_Oui_all()
        c.setFont("Helvetica", 16)
        page = 1

        nombre_pages = int(len(non_payments)/31) if len(non_payments)%31 ==0. else int(len(non_payments)/31)+1 
        c.drawString(100, 700, f"Liste des paiements (page {page}/{nombre_pages}).")
        c.line(100, 680, 500, 680) 
        c.setFont("Helvetica", 12)
        page_height = 660
        line_height = 20
        x = 100
        y=660
        
        for idx, non_payment in enumerate(non_payments, start=1):
            # Vérifier si une nouvelle page est nécessaire
            if y < 50:  # Espace insuffisant, créer une nouvelle page
                c.showPage() 
                page+=1

                c.setFont("Helvetica", 16)
                c.drawString(100, 700, f"Liste des paiements  (page {page}/{nombre_pages}).")
                c.line(100, 680, 500, 680)
                y = page_height  
            
            # Ajouter l'élément de la liste
            c.drawString(x, y, f"{idx}. {non_payment[1]} {non_payment[2]}")
            y -= line_height  # Passer à la ligne suivante
        # Ajouter une image
        # c.drawImage("path_to_image.jpg", 100, 500, width=200, height=150)

        # Finaliser le PDF
        c.save()
 
    def rapport_year_fc(self):
        revenue_by_month = recuperer_all_paiment() 
        depenses_by_month = recuperer_all_depenses() 
        revenue_by_month.index = pd.to_datetime(revenue_by_month.index).strftime('%Y-%m')
        
        
        path_evolution = self.generer_graphe_evolution(revenue_by_month, depenses_by_month)



        options = QFileDialog.Options()
        output_pdf, _ = QFileDialog.getSaveFileName(
            self.main_inter,
            "Enregistrer le fichier",
            "rapport-total.pdf",
            "Documents (*.pdf);;All Files (*)",
            options=options
        )
        if not output_pdf:
            QMessageBox.information(self.main_inter, "Le téléchargement est annulé.", "Le téléchargement est annulé.")
            return  
        
        # Création d'un objet Canvas pour générer le PDF
        c = canvas.Canvas(output_pdf, pagesize=letter)

        # Ajout de texte dans le PDF
        c.setFont("Helvetica", 16)
        c.drawString(100, 700, f"Rapport de résultats.")
        
        c.line(100, 680, 500, 680)
        c.setFont("Helvetica", 12) 
        introduction = f"""Ce rapport présente une vue globale des revenus et des dépenses depuis \nl’ouverture du club, en mettant l’accent sur l’évolution \ndes performances financières au fil du temps. \nL’objectif est de fournir un aperçu complet de la santé financière du club \net de proposer des axes d’amélioration pour optimiser la gestion \ndes paiements et des dépenses."""
        introduction_list=introduction.split("\n")

        for index, text in enumerate(introduction_list):
            c.drawString(100, 660-(index*20), text)


        c.drawImage(path_evolution, 100, 260, width=450, height=250) 

        date_now = datetime.now().strftime("%Y-%m")

        revenue_ce_moi = revenue_by_month[date_now] if date_now in revenue_by_month else 0
        depense_ce_moi = depenses_by_month[date_now] if date_now in depenses_by_month else 0

        c.setFont("Helvetica", 14)
        # Ajouter du texte à différentes positions
        c.drawString(100, 240, f"Situation du moi actuel ({date_now}) : ")
        c.setFont("Helvetica", 12) 
        c.drawString(120, 220, f"Revenues :  {revenue_ce_moi} Dhs")
        c.drawString(120, 200, f"Dépenses :  {depense_ce_moi} Dhs")
        c.drawString(120, 180, f"Résultats : {revenue_ce_moi - depense_ce_moi} Dhs")
        c.drawString(100, 160, f"La liste de chaque mois se trouve dans les pages suivantes.")

        c.showPage()
        union_indices = revenue_by_month.index.union(depenses_by_month.index)
        union_indices = list(union_indices)

        page_height = 720
        line_height = 20
        x = 100
        y=720 

        for index in union_indices[::-1]:

            if y < 50:  # Espace insuffisant, créer une nouvelle page
                c.showPage() 
                y = page_height  

            revenue_index = revenue_by_month[index] if index in revenue_by_month else 0
            depense_index = depenses_by_month[index] if index in depenses_by_month else 0
            c.drawString(x, y, f"Situation du mois {index} : ")
            c.setFont("Helvetica", 12) 
            c.drawString(x+10, y-20, f"Revenues :  {revenue_index} Dhs")
            c.drawString(x+10, y-40, f"Dépenses :  {depense_index} Dhs")
            c.drawString(x+10, y-60, f"Résultats : {revenue_index - depense_index} Dhs") 
            y -= (4 * line_height)
        
        
        



        c.save()


        


    



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



    def generer_graphe_situation(self, nbr_adh,nbr_pyment, date):
    
        
        # Création du graphique
        fig, ax = plt.subplots(figsize=(6, 6))  # Créer une figure et un axe
        fig.set_facecolor("white")  # Couleur de fond de la figure
        ax.set_facecolor('#ffffff')  # Couleur de fond de l'axe
        # Tracer le graphique en secteur (camembert)
        ax.pie(
            [nbr_pyment, nbr_adh - nbr_pyment], 
            labels=["Paiement effectué", "Paiement non effectué"], 
            autopct="%1.1f%%", 
            startangle=90, 
            colors=["lightgreen", "firebrick"]
        )  
        

        ax.set_title(f"Pourcentage de la situation du mois : ({date})", color='black', fontsize=16) 

        # Paramétrer les couleurs des ticks et des labels
        ax.tick_params(axis='both', labelcolor='purple')
        # Sauvegarder le graphique dans un objet BytesIO
        image_stream = BytesIO()
        fig.savefig(image_stream, format='png')
        image_stream.seek(0)
        temp_image_file = NamedTemporaryFile(delete=False, suffix='.png')
        image_path = temp_image_file.name
        fig.savefig(image_path, format='png')
        temp_image_file.close()
        return image_path

    
    

             
            


    