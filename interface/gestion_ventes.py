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

 

class Ventes( ):
    def __init__(self,main_inter): 
       self.main_inter = main_inter
       self.show_dashboard_inter()
    
    def show_dashboard_inter(self):
        self.main_inter.clear_content_frame()

        self.dashbord_widget = QWidget()
        self.dashbord_widget.setObjectName("dashbord_widget")

        # Layout principal
        layout = QVBoxLayout(self.dashbord_widget)
        title_layout = QHBoxLayout()
        self.title1 = QLabel("Ajouter des produits au stock ")
        self.title1.setObjectName("FormulaireWidgetstock1") 
        self.title1.setAlignment(Qt.AlignCenter)
        title_layout.addWidget(self.title1 )
        self.title2 = QLabel("Confirmer la vente")
        title_layout.addWidget(self.title2 )
        self.title2.setObjectName("FormulaireWidgetstock2") 
        self.title2.setAlignment(Qt.AlignCenter)
 
        
        
        
        # Layouts horizontaux pour les graphiques
        graphs_layout = QHBoxLayout()
 
        

        self.form_widget = QWidget()
        self.form_widget.setObjectName("FormulaireWidgetstock") 
        
        form_layout = QFormLayout(self.form_widget)


        self.produits = QComboBox()
        self.produits.addItems(fetch_products())
        self.produits.currentIndexChanged.connect(self.update_produit)
        self.autre_produit = QLineEdit()
        self.autre_produit.setReadOnly(True)

        self.quantite = QSpinBox()
        self.quantite.setRange(1, 10000)

        self.date_expiration = QDateEdit()
        self.date_expiration.setDate(QDate.currentDate())

        self.prix_achat = QSpinBox()
        self.prix_achat.setRange(1, 10000) 

        self.prix_vente = QSpinBox()
        self.prix_vente.setRange(1, 10000)  




        


        form_layout.addRow(" ", QLabel(" "))
        row_layout_1 = QHBoxLayout()
        row_layout_1.addWidget(self.produits)
        row_layout_1.addWidget(QLabel("Autre : ")) 
        row_layout_1.addWidget(self.autre_produit)
        form_layout.addRow("Produit :", row_layout_1)

        row_layout_2 = QHBoxLayout()
        row_layout_2.addWidget(self.quantite)
        row_layout_2.addWidget(QLabel("Date d'expiration : ")) 
        row_layout_2.addWidget(self.date_expiration)
        form_layout.addRow("Quantité :", row_layout_2)


        row_layout_3 = QHBoxLayout()
        row_layout_3.addWidget(self.prix_achat)
        row_layout_3.addWidget(QLabel("Prix de vente : ")) 
        row_layout_3.addWidget(self.prix_vente)
        form_layout.addRow("Prix d'achat :", row_layout_3)

        self.save_button = QPushButton("Ajouter dans le Stock")
        self.save_button.clicked.connect(self.save_stock)
        self.save_button.setObjectName("buttonExtraction")

        row_layout_4 = QHBoxLayout()
        row_layout_4.addWidget(self.save_button) 
        
        form_layout.addRow(" ", row_layout_4)


        graphs_layout.addWidget(self.form_widget)
        

        # Page de connexion
        self.login_frame = QFrame() 
        self.login_frame.setObjectName("FormulaireWidgetstock22") 
        #self.connexion = QLabel("Ajouter produits dans le stocks ")
        #self.connexion.setObjectName('depensesvente')
        
        
        # Layout de la frame de connexion
        self.login_layout = QFormLayout(self.login_frame)
        #self.login_layout.addWidget(self.connexion ) 

        self.user_label = QLabel("Selectionner un produit")
        self.login_layout.addRow('Nom de Produit :', self.user_label)
        
        self.priscons = QLabel("Selectionner un produit")
        self.login_layout.addRow('Prix conseillé :', self.priscons)
        self.datexp = QLabel("Selectionner un produit")
        self.login_layout.addRow("Date d'expiration :", self.datexp)
        
        self.quantite_vente = QSpinBox()
        self.quantite_vente.setRange(1, 10000) 
        self.login_layout.addRow("Quantité : ", self.quantite_vente )
        
        self.prix_finale = QSpinBox()
        self.prix_finale.setRange(1, 10000) 
        self.login_layout.addRow("Prix de vente ", self.prix_finale)
        
 

        self.login_button = QPushButton("Confirmer la vente")
        self.login_button.clicked.connect(self.ajouter_vente)
        self.login_button.setObjectName("buttonExtraction")
        self.login_layout.addRow("",self.login_button)
        graphs_layout.addWidget(self.login_frame)

        
        # Ajout des graphiques au layout principal
        
        
        # Tableau pour afficher les adhérents avec situation = NON

        titre_table = QLabel('Produits en stock :')
        titre_table.setObjectName("titre_table")
        layout.addWidget(titre_table)

        # Search bar for filtering
        self.search_bar = QLineEdit(self.main_inter)
        self.search_bar.setPlaceholderText("Chercher par 'Nom'...")
        self.search_bar.textChanged.connect(self.filter_table)  # Trigger filter when text changes
        layout.addWidget(self.search_bar)

        self.tableWidget = QTableWidget()
        self.srock_table()  
        layout.addWidget(self.tableWidget)
        layout.addLayout(title_layout)
        layout.addLayout(graphs_layout)

        



        rapport_mont = QHBoxLayout()

        # Bouton de sélection de photo
        self.rapport_month = QPushButton("Générer l'historique des ventes")
        self.rapport_month.clicked.connect(self.rapport_month_fc)
        self.rapport_month.setObjectName("buttonExtraction") 

        """
        # Bouton de sélection de photo
        self.rapport_year = QPushButton("Extraire la disponibilité des produits en stock")
        self.rapport_year.clicked.connect(self.rapport_year_fc)
        self.rapport_year.setObjectName("buttonExtraction")   """      

         
        rapport_mont.addWidget(self.rapport_month)
        #rapport_mont.addWidget(self.rapport_year) 
        layout.addLayout(rapport_mont )
        
        
        self.main_inter.content_layout.addWidget(self.dashbord_widget) 
    

    def ajouter_vente(self): 
        if self.user_label.text()  != "Selectionner un produit":
            insertion_vente(self.user_label.text(), self.quantite_vente.value(), self.prisachat_c,self.prix_finale.text(), self.datexp.text(), self.stock_id_av, self.anc_q )
            self.main_inter = Ventes(self.main_inter)
        else:
            QMessageBox.information(self.main_inter, "Succès", "Merci de sélectionner un produit")


    def save_stock(self):
        datae_expiration = self.date_expiration.date().toString("yyyy-MM-dd")
        produit = self.produits.currentText() 
        quantite = self.quantite.value()
        prix_achat = self.prix_achat.value()
        prix_vente = self.prix_vente.value()
        if produit in 'Autre':
            autre = self.autre_produit.text()
            id_prodult = insertion_produit(autre)
        else:
            id_prodult = get_id_produit(produit)


        insertion_product_stock(id_prodult, quantite, prix_achat,prix_vente, datae_expiration)
        self.main_interface = Ventes( self.main_inter)

    
    
    def update_produit(self):
        if self.produits.currentText() == 'Autre':
            self.autre_produit.setReadOnly(False) 
        else:
            self.autre_produit.setReadOnly(True)
    


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

 
 
    def srock_table(self):
        """Charge les adhérents dans le tableau avec des fonctionnalités supplémentaires"""
        # Connexion à la base de données SQLite
        
        self.stock = fetch_stock()  
        
        # Effacer les anciennes lignes dans le tableau
        self.tableWidget.setColumnCount(7)  # Nombre de colonnes affichées
        self.tableWidget.setHorizontalHeaderLabels([
            'Nom du produit',   "Quantité",  "Prix d'achat",   "Prix conseillé",    "Date d'expiration", "Date d'achat", "Vendre"
        ])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #self.all_data = False  # Nombre de lignes visibles à chaque fois 
        #self.tableWidget.verticalScrollBar().valueChanged.connect(self.on_scroll)

        # Ajouter les adhérents dans le tableau
        for  row_index, adherent in enumerate(self.stock):
            self.tableWidget.insertRow(row_index)
            # Ajouter les données dans les colonnes respectives
            element = [adherent[i] for i in range(8) if i not in (1,2)] 
            for col_index, data in enumerate(element):  # Exclure 'id' pour l'affichage

                
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_index, col_index, item)
                if col_index == 4:
                    date_cible = datetime.strptime(str(data), "%Y-%m-%d") 
                    date_actuelle = datetime.now() 
                    difference = (date_cible - date_actuelle).days
                    if difference <=10:
                        item.setBackground(QColor(255, 0, 0))



            # Ajouter un lien cliquable dans la colonne Action
            action_item = QTableWidgetItem("Vendre")
            action_item.setForeground(QColor('white'))
            action_item.setTextAlignment(Qt.AlignCenter)
            action_item.setData(Qt.UserRole, adherent[1])  # Stocker l'ID de l'adhérent pour le traitement
            action_item.setBackground(QColor(0, 0, 255))  # Vert
            self.tableWidget.setItem(row_index, 6, action_item) 

        self.tableWidget.cellClicked.connect(self.on_cell_clicked_vente)
    
     

    def on_cell_clicked_vente(self, row, column):
        # Si la colonne 12 (Action) est cliquée
        try:
            if column == 6:
                #self.main_inter.clear_content_frame()
                self.stock_id_av = self.tableWidget.item(row, column).data(Qt.UserRole) 
                self.user_label.setText(self.tableWidget.item(row, 0).text())
                self.priscons.setText(self.tableWidget.item(row, 3).text())
                self.quantite_vente.setRange(0, int(self.tableWidget.item(row, 1).text()))
                self.anc_q = int(self.tableWidget.item(row, 1).text())
                self.prisachat_c = self.tableWidget.item(row, 2).text()
                self.datexp.setText(self.tableWidget.item(row, 4).text())
                self.quantite_vente.setValue(1)
                self.prix_finale.setValue(int(self.tableWidget.item(row, 3).text()))
        except:
            pass
    def rapport_month_fc(self):  
        
        #graphe porcentage de paiment
        # Liste Dépenses et liste payment, list de non payment 
        # Chemin du fichier PDF de sortie
  
 

        
        options = QFileDialog.Options()
        output_pdf, _ = QFileDialog.getSaveFileName(
            self.main_inter,
            "Enregistrer le fichier",
            f"rapport-historique-vente-{datetime.now()}.pdf",
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
        ventes = fetch_ventes()
        
        page = 1
        nombre_pages = int(len(ventes)/31) if len(ventes)%31 ==0. else int(len(ventes)/31)+1 
        
        c.drawString(100, 710, f"Rapport d'historique des ventes : {datetime.now()}. (page {page}/{nombre_pages}).")
        c.line(100, 680, 500, 680) 
        c.drawString(100, 660, "Nom Produit | Quantité | Prix Achat | Prix Vent Final | Date Expiration | Date Vente") 
        c.setFont("Helvetica", 11)
        page_height = 640
        line_height = 20
        x = 100
        y=640
        
        for idx, non_payment in enumerate(ventes, start=1):
            # Vérifier si une nouvelle page est nécessaire
            if y < 50:  # Espace insuffisant, créer une nouvelle page
                c.showPage() 
                page+=1 
                c.setFont("Helvetica", 16)
                c.drawString(100, 700, f"Rapport d'historique des ventes : {datetime.now()}. (page {page}/{nombre_pages}).")
                c.line(100, 680, 500, 680)  
                y = page_height  
            c.drawString(100, y-20, f"Nom Produit  |  {non_payment[1]}") 
            c.drawString(100, y-40, f"Quantité | {non_payment[2]}") 
            c.drawString(100, y-60, f"Prix Achat :{non_payment[3]} (dhs) ") 
            c.drawString(100, y-80, f"Prix Vent Final : {non_payment[4]}(dhs)") 
            c.drawString(100, y-100, f" Date Expiration : {non_payment[5]}") 
            c.drawString(100, y-120, f"Date Vente : {non_payment[6]}")  
            c.line(100, y-4, 500, y-4)  
 
            y -= 8 *line_height  # Passer à la ligne suivante
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

    
    

             
            


    