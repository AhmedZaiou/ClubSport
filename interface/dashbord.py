from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from utils.utils import *
from dataset.dataset import *
from .main_interface import MainInterface


class Dashbord(MainInterface):
    def __init__(self):
        super().__init__()
        self.show_dashboard_inter()
        
    def show_dashboard_inter(self):
        self.clear_content_frame()

        self.dashbord_widget = QWidget()
        self.dashbord_widget.setObjectName("dashbord_widget")

        # Layout principal
        layout = QVBoxLayout(self.dashbord_widget)
        
        # Layouts horizontaux pour les graphiques
        graphs_layout = QHBoxLayout()
        
        # Graphique 1 : Pourcentage des situations pour ce mois
        self.situation_canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.plot_situation_graph()
        graphs_layout.addWidget(self.situation_canvas)
        
        # Graphique 2 : Revenus mensuels pour cette année
        self.revenue_canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.plot_revenue_graph()
        graphs_layout.addWidget(self.revenue_canvas)
        
        # Ajout des graphiques au layout principal
        layout.addLayout(graphs_layout)
        
        # Tableau pour afficher les adhérents avec situation = NON
        self.tableWidget = QTableWidget()
        self.populate_table() 
        layout.addWidget(self.tableWidget)
        
        self.content_layout.addWidget(self.dashbord_widget) 

    def plot_situation_graph(self):
        """Affiche le pourcentage des situations pour le mois actuel"""
        df = fetch_data()
        df["date_entree"] = pd.to_datetime(df["date_entree"])
        
        # Filtrer les données pour le mois actuel
        current_month = datetime.now().strftime("%Y-%m")
        df_current_month = df#[df["date_entree"].dt.strftime("%Y-%m") == current_month]
        
        if not df_current_month.empty:
            situation_counts = df_current_month["situation"].value_counts()
            ax = self.situation_canvas.figure.add_subplot(111)
            ax.clear()
            ax.pie(
                situation_counts, 
                labels=situation_counts.index, 
                autopct="%1.1f%%", 
                startangle=90, 
                colors=["skyblue", "orange"]
            )
            ax.set_title(f"Pourcentage des Situations ({current_month})")
        else:
            ax = self.situation_canvas.figure.add_subplot(111)
            ax.text(0.5, 0.5, "Aucune donnée pour ce mois", ha="center", va="center")
        
        self.situation_canvas.draw()

    def plot_revenue_graph(self):
        """Affiche les revenus mensuels pour l'année en cours avec le total annuel"""
        df = fetch_data()
        df["date_entree"] = pd.to_datetime(df["date_entree"])
        
        # Filtrer les données pour l'année en cours
        current_year = datetime.now().year
        df_current_year = df[df["date_entree"].dt.year == current_year]
        
        if not df_current_year.empty:
            df_current_year["month"] = df_current_year["date_entree"].dt.strftime("%B")
            revenue_by_month = df_current_year.groupby("month")["tarif"].sum()
            total_revenue = revenue_by_month.sum()  # Calculer le total annuel
            
            # Assurer que les mois sont bien ordonnés
            revenue_by_month = revenue_by_month.reindex(
                pd.date_range(f"{current_year}-01", f"{current_year}-12", freq="M").strftime("%B"), 
                fill_value=0
            )
            
            ax = self.revenue_canvas.figure.add_subplot(111)
            ax.clear()
            revenue_by_month.plot(kind="bar", ax=ax, color="green", alpha=0.75)
            ax.set_title(f"Revenus Mensuels ({current_year}) - Total : {total_revenue} €")
            ax.set_xlabel("Mois")
            ax.set_ylabel("Revenus (€)")
            
            # Ajouter des marges autour des barres
            ax.margins(x=0.05, y=0.1)
        else:
            ax = self.revenue_canvas.figure.add_subplot(111)
            ax.text(0.5, 0.5, "Aucune donnée pour cette année", ha="center", va="center")
        
        self.revenue_canvas.draw()

    def populate_table(self):
        """Charge les adhérents dans le tableau avec des fonctionnalités supplémentaires"""
        # Connexion à la base de données SQLite
        
        adherents = fetch_data_Non() 
        
        # Effacer les anciennes lignes dans le tableau
        self.tableWidget.setColumnCount(6)  # Nombre de colonnes affichées
        self.tableWidget.setHorizontalHeaderLabels([
            'Nom', 'Prénom', 'Email', 'Téléphone', 'Situation', 'Action'
        ])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.tableWidget.setRowCount(10)


        # Ajouter les adhérents dans le tableau
        for row_index, adherent in enumerate(adherents):
            self.tableWidget.insertRow(row_index)

            # Ajouter les données dans les colonnes respectives
            for col_index, data in enumerate(adherent[1:]):  # Exclure 'id' pour l'affichage
                
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_index, col_index, item)
                

                # Ajouter une couleur verte à la cellule de la colonne Email
                if col_index == 4 and data == 'Paiement non effectué':  # 3e colonne (Email)
                    item.setBackground(QColor(255, 0, 0))  # Vert 

            # Ajouter un lien cliquable dans la colonne Action
            action_item = QTableWidgetItem("Traiter")
            action_item.setForeground(Qt.blue)
            action_item.setTextAlignment(Qt.AlignCenter)
            action_item.setData(Qt.UserRole, adherent[0])  # Stocker l'ID de l'adhérent pour le traitement
            self.tableWidget.setItem(row_index, 5, action_item)

        

        # Connecter l'événement de clic pour traiter un adhérent
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)

    def on_cell_clicked(self, row, column): 
        # Si la colonne 12 (Action) est cliquée
        if column == 5:
            self.clear_content_frame()
            adherent_id = self.tableWidget.item(row, column).data(Qt.UserRole)
            from .profile_interface import Profile
            self.main_interface = Profile(adherent_id)
            self.main_interface.show()
            self.close()


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
        