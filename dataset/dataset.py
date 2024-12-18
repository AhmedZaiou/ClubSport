    
import pandas as pd 
import sqlite3 
from datetime import datetime
#from utils.utils import *
import calendar
#path_data_set = "/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db"
import subprocess



from pathlib import Path
import hashlib
from datetime import datetime, timedelta 

current_directory = Path(__file__).parent
racine = current_directory.parent 



dataset = Path.home()/"dataset"


path_profils_images = Path.home()/"images"/"profiles"

path_data_set = dataset/"royal_fitness.db"

from datetime import datetime
from dateutil.relativedelta import relativedelta

def fetch_data():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect(path_data_set)
    query = "SELECT * FROM adherents"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df  


def fetch_data_Non():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect(path_data_set)  # Nom de votre fichier de base de données
    cursor = conn.cursor()

    # Récupérer ment les colonnes nécessaires
    cursor.execute("SELECT id, nom, prenom, email, telephone, situation FROM adherents")
    adherents = cursor.fetchall()
    filtred_adh = []
    for data in adherents:
        last_paiment = recuperer_last_payment(data[0])
        # Define the date to compare
        date_to_compare = datetime.strptime(last_paiment, "%Y-%m-%d") 
        current_date = datetime.now() 
        if date_to_compare.year == current_date.year and date_to_compare.month == current_date.month:
            pass
        else:
            filtred_adh.append(data)    
    return filtred_adh

def fetch_data_Non_all():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect(path_data_set)  # Nom de votre fichier de base de données
    cursor = conn.cursor()

    # Récupérer ment les colonnes nécessaires
    cursor.execute("SELECT id, nom, prenom, email, telephone, situation FROM adherents")
    adherents = cursor.fetchall()
    filtred_adh = []
    for data in adherents:
        last_paiment = recuperer_last_payment(data[0])
        # Define the date to compare
        date_to_compare = datetime.strptime(last_paiment, "%Y-%m-%d") 
        current_date = datetime.now() 
        if date_to_compare.year == current_date.year and date_to_compare.month == current_date.month:
            pass
        else:
            filtred_adh.append(data)    
    return filtred_adh

def fetch_data_Oui_all():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect(path_data_set)  # Nom de votre fichier de base de données
    cursor = conn.cursor()

    # Récupérer ment les colonnes nécessaires
    cursor.execute("SELECT id, nom, prenom, email, telephone, situation FROM adherents")
    adherents = cursor.fetchall()
    filtred_adh = []
    for data in adherents:
        last_paiment = recuperer_last_payment(data[0])
        # Define the date to compare
        date_to_compare = datetime.strptime(last_paiment, "%Y-%m-%d") 
        current_date = datetime.now() 
        if date_to_compare.year == current_date.year and date_to_compare.month == current_date.month:
            filtred_adh.append(data) 
                
    return filtred_adh


def fetch_data_all():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect(path_data_set)  # Nom de votre fichier de base de données
    cursor = conn.cursor()

    # Récupérer ment les colonnes nécessaires
    cursor.execute("SELECT id, nom, prenom, email, telephone, situation FROM adherents")
    adherents = cursor.fetchall()
    return pd.DataFrame(adherents)

def load_data( adherent_id):
        connection = sqlite3.connect(path_data_set)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM adherents WHERE id = ?", (adherent_id,))
        row = cursor.fetchone()
        connection.close()  
        return row

def ajouter_adh(nom, prenom, email, telephone, cin, num_adh, adresse, date_entree,
        age, genre, tarif, seances, situation, photo_path,
        poids, longeur, titre_sport, nom_parent, contact_parent, situation_sanitaire, situation_sanitaire_text, discipline, numero_assurance, centure, dautre_information):
    connection = sqlite3.connect(path_data_set)
    cursor = connection.cursor()

    # Création de la table si elle n'existe pas encore
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS adherents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prenom TEXT,
            email TEXT,
            telephone TEXT,
            cin TEXT ,
            num_adh TEXT ,
            adresse TEXT,
            date_entree DATE,
            age INTEGER,
            genre TEXT,
            tarif INTEGER,
            seances INTEGER,
            situation TEXT,
            photo_path TEXT,
            poids TEXT,
            longeur TEXT,
            titre_sport TEXT,
            nom_parent TEXT,
            contact_parent TEXT,
            situation_sanitaire TEXT,
            situation_sanitaire_text TEXT, 
            discipline TEXT,
            numero_assurance TEXT,
            centure TEXT,
            dautre_information TEXT
        )
    """)

    # Insertion des données dans la table
    cursor.execute("""
        INSERT INTO adherents (
            nom, prenom, email, telephone, cin, num_adh, adresse,
            date_entree, age, genre, tarif, seances, situation, photo_path, poids, longeur, titre_sport, nom_parent, contact_parent, situation_sanitaire, situation_sanitaire_text, discipline, numero_assurance, centure, dautre_information
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (nom, prenom, email, telephone, cin, num_adh, adresse, date_entree,
        age, genre, tarif, seances, situation, photo_path, poids, longeur, titre_sport, nom_parent, contact_parent, situation_sanitaire, situation_sanitaire_text, discipline, numero_assurance, centure, dautre_information,))

    # Validation de la transaction
    connection.commit() 
    if connection:
                connection.close()



def inser_db_sinistre(data): 
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor() 
    
    cursor.execute('''
        INSERT INTO accidents (id_adherent, name_haderent,nom, date, nature, gravite, soins, hospitalisation, rapport, indispo, temoins, mesures)
        VALUES (:id_adherent, :name_haderent,:nom, :date, :nature, :gravite, :soins, :hospitalisation, :rapport, :indispo, :temoins, :mesures)
    ''', data)
    conn.commit() 

    conn.close()

def recuperer_sinistre():
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT *  FROM accidents;
    ''')
    paiements = cursor.fetchall()

    conn.close()
    return paiements

 

def affectuer_paiment():
    # Connexion à la base de données
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    # Création de la table des paiements
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS paiements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        adherent_id INTEGER,
        montant INTEGER,
        date_paiement DATE,
        mode_paiement TEXT,
        moi_concerner DATE,
        FOREIGN KEY (adherent_id) REFERENCES adherents (id)
    )
    ''')

    conn.commit()
    conn.close()    
    
def ajouter_paiement(adherent_id, montant, date_paiement, mode_paiement, month_to_pay):
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO paiements (adherent_id, montant, date_paiement, mode_paiement, moi_concerner)
    VALUES (?, ?, ?, ?, ?)
    ''', (adherent_id, montant, date_paiement, mode_paiement, month_to_pay))

    conn.commit()
    conn.close()

def ajouter_sanction(id_adherent, cause, genre, duree, date_s,date_f):
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()
 
    cursor.execute('''
    INSERT INTO sanction (id_adherent, cause, genre, duree, date_start, date_fin)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (id_adherent, cause, genre, duree, date_s,date_f))

    conn.commit()
    conn.close()


def recuperer_paiements(adherent_id):
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT adherent_id, moi_concerner, montant, mode_paiement, date_paiement  FROM paiements WHERE adherent_id = ? ORDER BY moi_concerner;
    ''', (adherent_id,))
    paiements = cursor.fetchall()

    conn.close()
    return paiements

def modifier_adh(adherent_id, nom, prenom, email, telephone, cin, num_adh, adresse, 
                        date_entree, age, genre, tarif, seances, situation, photo_path
                        , poids, longeur, titre_sport, nom_parent, contact_parent, situation_sanitaire, situation_sanitaire_text, discipline, numero_assurance, centure, dautre_information):
     
    connection = sqlite3.connect(path_data_set)
    cursor = connection.cursor()

    # Requête SQL de mise à jour
    cursor.execute("""
        UPDATE adherents
        SET 
            nom = ?, prenom = ?, email = ?, telephone = ?, cin = ?, 
            num_adh = ?, adresse = ?, date_entree = ?, age = ?, 
            genre = ?, tarif = ?, seances = ?, situation = ?, photo_path = ?,
             poids = ?, longeur = ?, titre_sport = ?, nom_parent = ?, contact_parent = ?, situation_sanitaire = ?, situation_sanitaire_text = ?, discipline = ?, numero_assurance = ?, centure = ?, dautre_information = ?
        WHERE id = ?
    """, (nom, prenom, email, telephone, cin, num_adh, adresse, date_entree, 
          age, genre, tarif, seances, situation, photo_path, 
          poids, longeur, titre_sport, nom_parent, contact_parent, situation_sanitaire, situation_sanitaire_text,discipline, numero_assurance, centure, dautre_information,adherent_id,))

    # Validation de la transaction
    connection.commit()
    print(f"Adhérent ID {adherent_id} modifié avec succès.")

    # Fermeture de la connexion
    if connection:
        connection.close()



def recuperer_last_payment(adherent_id):
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT moi_concerner FROM paiements WHERE adherent_id = ? ;
    ''', (adherent_id,))
    paiements = cursor.fetchall()
    conn.close()
    if len(paiements) >0:
        dates_converted = [datetime.strptime(date[0], '%Y-%m-%d') for date in paiements] 
        date_la_plus_recente = max(dates_converted)
        return date_la_plus_recente.strftime('%Y-%m-%d')
    else:
         return '2010-10-01' 




def recuperer_porcentage_paiment():
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT COUNT(*) AS total_adherents FROM adherents;
    ''',)
    number_of_adhs = cursor.fetchall()

    cursor.execute('''
    SELECT COUNT(*) AS paiements_ce_mois
    FROM paiements
    WHERE  moi_concerner = ?
    ''',(f'{datetime.now().strftime("%Y-%m")}-01',)) 
    number_of_payment = cursor.fetchall()

    conn.close()
    return number_of_adhs[0][0],number_of_payment[0][0]

def recuperer_porcentage_paiment_date(date):
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT COUNT(*) AS total_adherents FROM adherents;
    ''',)
    number_of_adhs = cursor.fetchall()

    cursor.execute('''
    SELECT COUNT(*) AS paiements_ce_mois
    FROM paiements
    WHERE  moi_concerner = ?
    ''',(f'{date.strftime("%Y-%m")}-01',)) 
    number_of_payment = cursor.fetchall()

    conn.close()
    return number_of_adhs[0][0],number_of_payment[0][0]

def recuperer_stat_paiment():
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    dict_moths = {}
    mois_noms = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

    for i in range(1,int(datetime.now().strftime("%m"))+1):
        month = str(i) if i>10 else str(f'0{i}')
        cursor.execute('''
        SELECT 
        SUM(montant) AS revenu_total_annuel
        FROM paiements
        WHERE moi_concerner  = ?
        ''',(f'{datetime.now().strftime("%Y")}-{month}-01',))
        summ_moth = cursor.fetchall()
        dict_moths[mois_noms[i-1]]=summ_moth[0][0] if summ_moth[0][0]  else 0
    return dict_moths, sum(dict_moths.values())

def recuperer_all_paiment():
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT 
        *
        FROM paiements
         ''',()) 
    summ_moth = cursor.fetchall()
    df = pd.DataFrame(summ_moth, columns=['id',  's',  'montant',  'date_inscr' , 'modep',  'date'])
    df = df.groupby('date')['montant'].sum().reset_index()
    return pd.Series(data=df['montant'].values, index=df['date'])

def recuperer_all_depenses():
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT 
        *
        FROM depenses
         ''',()) 
    summ_moth = cursor.fetchall()
    df = pd.DataFrame(summ_moth, columns=['id',  'commentaire',  'montant', 'date'])
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m')
    df = df.groupby('date')['montant'].sum().reset_index()
    return pd.Series(data=df['montant'].values, index=df['date'])


 
def dinscription(id):

    data = load_data( id)

    (id_profile ,nom, prenom, email, telephone, cin, num_adh, adresse, date_entree, age, genre, tarif, seances, situation, photo_path) = data
    connection = sqlite3.connect(path_data_set)
    cursor = connection.cursor()

    # Création de la table si elle n'existe pas encore
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS old_adh (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_profil TEXT,
            nom TEXT,
            prenom TEXT,
            email TEXT,
            telephone TEXT,
            cin TEXT ,
            num_adh TEXT ,
            adresse TEXT,
            date_entree DATE,
            age INTEGER,
            genre TEXT,
            tarif INTEGER,
            seances INTEGER,
            situation TEXT,
            photo_path TEXT
        )
    """)

    # Insertion des données dans la table
    cursor.execute("""
        INSERT INTO old_adh (
            id_profil, nom, prenom, email, telephone, cin, num_adh, adresse,
            date_entree, age, genre, tarif, seances, situation, photo_path
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (id_profile, nom, prenom, email, telephone, cin, num_adh, adresse, date_entree,
        age, genre, tarif, seances, situation, photo_path))
    
    cursor.execute("""
        DELETE FROM adherents WHERE id = ?;
    """, (id,))
    

    # Validation de la transaction
    connection.commit() 
    if connection:
                connection.close()





def fetch_data_with_last():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect(path_data_set)  # Nom de votre fichier de base de données
    cursor = conn.cursor()

    # Récupérer ment les colonnes nécessaires
    cursor.execute("SELECT id, nom, prenom, email, telephone, situation FROM adherents")
    adherents = cursor.fetchall()
    cursor.execute("SELECT moi_concerner,adherent_id FROM paiements")
    paiements = cursor.fetchall()
    adherents, paiements =  pd.DataFrame(adherents, columns=["id", "nom", "prenom", "email", "telephone", "situation" ]), pd.DataFrame(paiements, columns=["moi_concerner","adherent_id"])
    paiements["moi_concerner"] = pd.to_datetime(paiements["moi_concerner"], format='%Y-%m-%d')
    paiements = paiements.groupby("adherent_id")["moi_concerner"].max().reset_index() 
    merged_df = adherents.merge(paiements, left_on="id", right_on="adherent_id", how="left")
    merged_df["moi_concerner"] = merged_df["moi_concerner"].fillna(datetime.now() - pd.DateOffset(months=1))

    return merged_df

def fetch_data_sanctionner():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect(path_data_set)  # Nom de votre fichier de base de données
    cursor = conn.cursor()

    # Récupérer ment les colonnes nécessaires
    cursor.execute("SELECT id, nom, prenom FROM adherents")
    adherents = cursor.fetchall()
    cursor.execute("SELECT * FROM sanction")
    sanctions = cursor.fetchall()
    adherents, sanctions =  pd.DataFrame(adherents, columns=["id", "nom", "prenom" ]), pd.DataFrame(sanctions, columns=["id","id_adherent", "cause", "genre", "duree", "date_start", "date_fin"])
    
    merged_df = adherents.merge(sanctions, left_on="id", right_on="id_adherent") 

    return merged_df

def fetch_data_Non_df():
    merged_df = fetch_data_with_last()
    year_now = datetime.now().year
    month_now = datetime.now().month

    # Create a date with year_now, month_now, and 01 as the day
    date = datetime(year_now, month_now, 1)
    merged_df = merged_df[merged_df["moi_concerner"] < date]
    merged_df.reset_index(drop=True, inplace=True)
    
    return merged_df


def recuperer_all_paiements():
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM paiements ;
    ''', ())
    paiements = cursor.fetchall()
    conn.close()
    return paiements
def recuperer_all_depenses1():
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM depenses ;
    ''', ())
    paiements = cursor.fetchall()
    conn.close()
    return paiements

def fetch_data():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect(path_data_set)
    
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM adherents;
    ''', ())
    paiements = cursor.fetchall()
    conn.close()
    return paiements

def fetch_depenses():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect(path_data_set)
    
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM depenses;
    ''', ())
    paiements = cursor.fetchall()
    conn.close()
    return paiements

def fetch_products():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect(path_data_set)
    
    cursor = conn.cursor()
    cursor.execute('''
    SELECT nom_produit FROM produits;
    ''', ())
    paiements = cursor.fetchall()
    conn.close()
    list_product = [i[0] for i in paiements]
    list_product.append("Autre")
    return list_product




def insertion_depense(commentaire,montant, date):
    # Connexion à la base de données
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    # Création de la table des paiements
    cursor.execute("""
        INSERT INTO depenses (
            commentaire, montant, date_depense ) VALUES (?, ?, ?)
    """, (commentaire,montant, date)) 

    conn.commit()
    conn.close() 

def recuperer_stat_depenses():
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    dict_moths = {}
    mois_noms = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    current_date = datetime.now()
    last_day_of_current_month = datetime(current_date.year, current_date.month, calendar.monthrange(current_date.year, current_date.month)[1])


    for i in range(1,int(datetime.now().strftime("%m"))+1):
        month = str(i) if i>10 else str(f'0{i}') 
        cursor.execute('''
                       SELECT SUM(montant) AS revenu_total_annuel
                        FROM depenses
                        WHERE  date_depense BETWEEN ? AND ?
        ''',(f'{datetime.now().strftime("%Y")}-{month}-01', f'{datetime.now().strftime("%Y")}-{month}-{str(last_day_of_current_month)}'))
        summ_moth = cursor.fetchall()
        dict_moths[mois_noms[i-1]]=summ_moth[0][0] if summ_moth[0][0]  else 0 
    return dict_moths, sum(dict_moths.values())


def insertion_produit(produit):
    # Connexion à la base de données
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    # Création de la table des paiements
    cursor.execute("""
        INSERT INTO produits (
            nom_produit) VALUES (?)
    """, (produit,)) 

    conn.commit()
    conn.close() 
    return cursor.lastrowid

def get_id_produit(produit):
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect(path_data_set)
    
    cursor = conn.cursor()
    cursor.execute('''
    SELECT id FROM produits WHERE  nom_produit = ?
    ''', (produit,))
    paiements = cursor.fetchall()
    conn.close()
    return paiements[-1][0]
def insertion_product_stock(id_prodult, quantite, prix_achat,prix_vente, datae_expiration):
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    # Création de la table des paiements
    cursor.execute("""
        INSERT INTO stock (id_produit, 
        quentite,
        prix_achat,
        prix_vent_proposer,
        date_expiration,
        date_ajout) VALUES (?,?,?,?,?,?)
    """, (id_prodult, quantite, prix_achat,prix_vente, datae_expiration, datetime.now().strftime('%Y-%m-%d'),)) 

    conn.commit()
    conn.close()



def fetch_stock():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect(path_data_set)
    
    cursor = conn.cursor()
    cursor.execute('''
    SELECT p.nom_produit, s.* FROM  stock s JOIN   produits p ON  s.id_produit = p.id;
    ''', ())
    stock = cursor.fetchall()
    conn.close()
     
    return stock

def fetch_ventes():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect(path_data_set)
    
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * from vente;
    ''', ())
    stock = cursor.fetchall()
    conn.close()
     
    return stock


def insertion_vente(nom_produit, quantite, prix_achat,prix_vente, datae_expiration, idvent, ancien_q):
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    # Création de la table des paiements
    cursor.execute("""
        INSERT INTO vente (nom_produit, 
        quentite,
        prix_achat,
        prix_vent_final,
        date_expiration,
        date_vente) VALUES (?,?,?,?,?,?)
    """, (nom_produit, quantite, prix_achat,prix_vente, datae_expiration, datetime.now().strftime('%Y-%m-%d'),)) 

    cursor.execute("""
        UPDATE stock
        SET quentite = ?
        WHERE id = ?;
    """, (ancien_q-quantite, idvent,)) 
    cursor.execute("""
        DELETE FROM stock WHERE quentite = ?;
    """, (0,)) 


    
    conn.commit()
    conn.close()



def supprimer_sanction(sanction_id):
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM sanction WHERE id = ?;
    """, (sanction_id,))  


    
    conn.commit()
    conn.close()



def insertSalarie(nom_prenom, contact, salaire,admin,password):

    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    # Création de la table des paiements
    cursor.execute("""
        INSERT INTO salaries (nomprenem , 
        contat , 
        salaire ,
        date_commance ,
        last_payment,
        admin,
        password ) VALUES (?,?,?,?,?,?,?)
    """, (nom_prenom, contact, salaire,datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'),admin,password,)) 

    
    conn.commit()
    conn.close()

def fetch_salaeir() :

    conn = sqlite3.connect(path_data_set)
    
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * from salaries;
    ''', ())
    stock = cursor.fetchall()
    conn.close()
     
    return stock







  


def insertpaySalarie(nomprenem, commentaire, salaire,date_con):

    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    # Création de la table des paiements
    cursor.execute("""
        INSERT INTO paysalaries (nomprenem, commentaire, salaire,date_con,date_paymet) VALUES (?,?,?,?,?)
    """, (nomprenem, commentaire, salaire,date_con,datetime.now().strftime('%Y-%m-%d'),)) 

    
    conn.commit()
    conn.close()

def insert_code(code):

    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    # Création de la table des paiements
    cursor.execute("""
        INSERT INTO log (code) VALUES (?)
    """, (code,)) 

    
    conn.commit()
    conn.close()

def selectcode():

    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    # Création de la table des paiements
    cursor.execute("""
        SELECT * FROM log
    """, ()) 
    codes = cursor.fetchall() 

    
    conn.commit()
    conn.close()
    
    return  len(codes)>0



def update_salarie_lastpay(salarie_id, date):
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE salaries
        SET last_payment = ?
        WHERE id = ?;
    """, (date,salarie_id,)) 
    conn.commit()
    conn.close()

def update_salarie_password(salarie_id, nvpassword):
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE salaries
        SET password = ?
        WHERE id = ?;
    """, (nvpassword,salarie_id,)) 
    conn.commit()
    conn.close()

def supprimer_salarie(salarie_id):
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM salaries WHERE id = ?;
    """, (salarie_id,))  

    conn.commit()
    conn.close()



def loging_pass(username, password):
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor() 
    cursor.execute("""
        SELECT admin FROM salaries WHERE nomprenem = ? AND password = ?
    """, (username,password,)) 
    admin = cursor.fetchall() 

    conn.commit()
    conn.close() 

    if len(admin)>0:
        return admin[0][0] =='Oui'
    else:
        return False




def recuperer_all_salarie():
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM salaries ;
    ''', ())
    paiements = cursor.fetchall()
    conn.close()
    return paiements


def recuperer_all_stock():
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM stock ;
    ''', ())
    paiements = cursor.fetchall()
    conn.close()
    return paiements



def recuperer_all_ventes():
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM vente ;
    ''', ())
    paiements = cursor.fetchall()
    conn.close()
    return paiements



def recuperer_all_sanction():
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM sanction ;
    ''', ())
    paiements = cursor.fetchall()
    conn.close()
    return paiements



def recuperer_all_paysalaries():
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM paysalaries ;
    ''', ())
    paiements = cursor.fetchall()
    conn.close()
    return paiements






def initialiser_dataset(path_data_set): 
    if not dataset.exists():
        dataset.mkdir(parents=True,exist_ok=True)
    if not path_profils_images.exists():
        path_profils_images.mkdir(parents=True,exist_ok=True)

    
    try:
        subprocess.run(['attrib', '+h', str(dataset)], check=True)
        subprocess.run(['attrib', '+h', str(path_profils_images)], check=True)
    except:
        pass
    



    # Connexion à la base de données SQLite
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    # Création de la table adherents si elle n'existe pas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS adherents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        prenom TEXT,
        email TEXT,
        telephone TEXT,
        cin TEXT ,
        num_adh TEXT ,
        adresse TEXT,
        date_entree DATE,
        age INTEGER,
        genre TEXT,
        tarif INTEGER,
        seances INTEGER,
        situation TEXT,
        photo_path TEXT,
                poids TEXT,
                longeur TEXT,
                titre_sport TEXT,
                nom_parent TEXT,
                contact_parent TEXT,
                situation_sanitaire TEXT,
                situation_sanitaire_text TEXT
    )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS paiements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            adherent_id INTEGER,
            montant INTEGER,
            date_paiement DATE,
            mode_paiement TEXT,
            moi_concerner DATE,
            FOREIGN KEY (adherent_id) REFERENCES adherents (id)
        )
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS depenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            commentaire TEXT,
            montant INTEGER,
            date_depense DATE
        )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS salaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nomprenem TEXT, 
            contat TEXT, 
            salaire INTEGER,
            date_commance DATE,
            last_payment DATE,
            admin TEXT, 
            password TEXT
        )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS paysalaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nomprenem TEXT, 
            commentaire TEXT, 
            salaire INTEGER,
            date_con DATE,
            date_paymet DATE 
        )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produits (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nom_produit TEXT
        )
        ''')



    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_produit INTEGER,
            quentite INTEGER,
            prix_achat INTEGER,
            prix_vent_proposer INTEGER,
            date_expiration DATE,
            date_ajout DATE,
            FOREIGN KEY (id_produit) REFERENCES produits (id)
        )
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vente (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nom_produit TEXT,
            quentite INTEGER,
            prix_achat INTEGER,
            prix_vent_final INTEGER,
            date_expiration DATE,
            date_vente DATE
        )
        ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sanction (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_adherent INTEGER,
            cause TEXT,
            genre TEXT,
            duree INTEGER,
            date_start DATE,
            date_fin DATE
        )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS log (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            code TEXT
        )
        ''')

    conn.commit()
    conn.close()


def recuperer_compta_each_month(number = 12):
    
    # Date de départ
    start_date = datetime.now() - relativedelta(months=number)
    start_date = start_date.strftime('%Y-%m') 
    date_actuelle = datetime.strptime(start_date, '%Y-%m')  # Convertir en objet datetime
    mois_actuel = datetime.now().strftime('%Y-%m')
    mois_actuel = datetime.strptime(mois_actuel, '%Y-%m') 
    list_compta = []
     
    while mois_actuel >= date_actuelle: 
        list_compta.append(comptabilite_par_mois(date_actuelle.strftime('%Y-%m')))

        date_actuelle += relativedelta(months=1)
    return list_compta



def recuperer_compta_each_year():
     # Date de départ
    start_date = '2023'
    date_actuelle = datetime.strptime(start_date, '%Y')  # Convertir en objet datetime
    mois_actuel = datetime.now().strftime('%Y')
    mois_actuel = datetime.strptime(mois_actuel, '%Y') 
    list_compta = []
     
    while datetime.now() > date_actuelle: 
        list_compta.append(comptabilite_par_annee(date_actuelle.strftime('%Y')))
        date_actuelle += relativedelta(months=12)
    return list_compta


# Fonction pour obtenir la comptabilité par mois
def comptabilite_par_mois(mois_actuel):
    # Connexion à la base de données
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()
    # Récupérer la date actuelle

    # Ventes par mois
    cursor.execute('''
    SELECT strftime('%Y-%m', date_vente) AS mois, SUM(prix_vent_final * quentite) AS total_ventes
    FROM vente
    GROUP BY mois
    HAVING mois = ?
    ''', (mois_actuel,))
    ventes_mois = cursor.fetchone()

    # Ventes par mois
    cursor.execute('''
    SELECT strftime('%Y-%m', date_vente) AS mois, SUM(prix_achat * quentite) AS total_ventes
    FROM vente
    GROUP BY mois
    HAVING mois = ?
    ''', (mois_actuel,))
    achat_mois = cursor.fetchone()
    
    # Paiements par mois
    cursor.execute('''
    SELECT strftime('%Y-%m', date_paiement) AS mois, SUM(montant) AS total_paiements
    FROM paiements
    GROUP BY mois
    HAVING mois = ?
    ''', (mois_actuel,))
    paiements_mois = cursor.fetchone()

    # Dépenses par mois
    cursor.execute('''
    SELECT strftime('%Y-%m', date_depense) AS mois, SUM(montant) AS total_depenses
    FROM depenses
    GROUP BY mois
    HAVING mois = ?
    ''', (mois_actuel,))
    depenses_mois = cursor.fetchone()

    # Salaires par mois
    cursor.execute('''
    SELECT strftime('%Y-%m', date_con) AS mois, SUM(salaire) AS total_salaires
    FROM paysalaries
    GROUP BY mois
    HAVING mois = ?
    ''', (mois_actuel,))
    salaires_mois = cursor.fetchone()
    conn.close()
    resultats = {
        "mois" : mois_actuel,
        "ventes" : ventes_mois[1] if ventes_mois else 0,
        "achats" :  achat_mois[1] if achat_mois else 0,
        "paiments" : paiements_mois[1] if paiements_mois else 0,
        "dépenses" : depenses_mois[1] if depenses_mois else 0,
        "salaires" : salaires_mois[1] if salaires_mois else 0 
    }

    return resultats


# Fonction pour obtenir la comptabilité par année
def comptabilite_par_annee(annee_actuelle):
    # Connexion à la base de données
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor() 

    # Ventes par année
    cursor.execute('''
    SELECT strftime('%Y', date_vente) AS annee, SUM(prix_vent_final * quentite) AS total_ventes
    FROM vente
    GROUP BY annee
    HAVING annee = ?
    ''', (annee_actuelle,))
    ventes_annee = cursor.fetchone()

    # Ventes par année
    cursor.execute('''
    SELECT strftime('%Y', date_vente) AS annee, SUM(prix_achat * quentite) AS total_ventes
    FROM vente
    GROUP BY annee
    HAVING annee = ?
    ''', (annee_actuelle,))
    achat_annee = cursor.fetchone()

    # Paiements par année
    cursor.execute('''
    SELECT strftime('%Y', date_paiement) AS annee, SUM(montant) AS total_paiements
    FROM paiements
    GROUP BY annee
    HAVING annee = ?
    ''', (annee_actuelle,))
    paiements_annee = cursor.fetchone()

    # Dépenses par année
    cursor.execute('''
    SELECT strftime('%Y', date_depense) AS annee, SUM(montant) AS total_depenses
    FROM depenses
    GROUP BY annee
    HAVING annee = ?
    ''', (annee_actuelle,))
    depenses_annee = cursor.fetchone()

    # Salaires par année
    cursor.execute('''
    SELECT strftime('%Y', date_con) AS annee, SUM(salaire) AS total_salaires
    FROM paysalaries
    GROUP BY annee
    HAVING annee = ?
    ''', (annee_actuelle,))
    salaires_annee = cursor.fetchone()
    conn.close()
    resultats ={
        "annee" : annee_actuelle,
        "ventes" : ventes_annee[1] if ventes_annee else 0,
        "achats" : achat_annee[1] if achat_annee else 0,
        "paiements" : paiements_annee[1] if paiements_annee else 0,
        "dépenses" : depenses_annee[1] if depenses_annee else 0,
        "salaires" : salaires_annee[1] if salaires_annee else 0
     }
    
    return resultats