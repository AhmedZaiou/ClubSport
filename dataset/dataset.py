    
import pandas as pd 
import sqlite3 
from datetime import datetime
from utils.utils import *
import calendar
#path_data_set = "/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db"

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
        age, genre, tarif, seances, situation, photo_path):
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
            photo_path TEXT
        )
    """)

    # Insertion des données dans la table
    cursor.execute("""
        INSERT INTO adherents (
            nom, prenom, email, telephone, cin, num_adh, adresse,
            date_entree, age, genre, tarif, seances, situation, photo_path
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (nom, prenom, email, telephone, cin, num_adh, adresse, date_entree,
        age, genre, tarif, seances, situation, photo_path))

    # Validation de la transaction
    connection.commit() 
    if connection:
                connection.close()



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

def recuperer_paiements(adherent_id):
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT adherent_id, moi_concerner, montant, mode_paiement, date_paiement  FROM paiements WHERE adherent_id = ? ;
    ''', (adherent_id,))
    paiements = cursor.fetchall()

    conn.close()
    return paiements

def modifier_adh(adherent_id, nom, prenom, email, telephone, cin, num_adh, adresse, 
                        date_entree, age, genre, tarif, seances, situation, photo_path):
    """
    Modifier les informations d'un adhérent dans la base de données.

    Args:
        adherent_id (int): ID de l'adhérent à modifier.
        nom (str): Nouveau nom.
        prenom (str): Nouveau prénom.
        email (str): Nouveau email.
        telephone (str): Nouveau téléphone.
        cin (str): Nouveau CIN.
        num_adh (str): Nouveau numéro d'adhérent.
        adresse (str): Nouvelle adresse.
        date_entree (str): Nouvelle date d'entrée (format YYYY-MM-DD).
        age (int): Nouvel âge.
        genre (str): Nouveau genre.
        tarif (int): Nouveau tarif.
        seances (int): Nouveau nombre de séances.
        situation (str): Nouvelle situation.
        photo_path (str): Nouveau chemin de photo.
    """
    connection = sqlite3.connect(path_data_set)
    cursor = connection.cursor()

    # Requête SQL de mise à jour
    cursor.execute("""
        UPDATE adherents
        SET 
            nom = ?, prenom = ?, email = ?, telephone = ?, cin = ?, 
            num_adh = ?, adresse = ?, date_entree = ?, age = ?, 
            genre = ?, tarif = ?, seances = ?, situation = ?, photo_path = ?
        WHERE id = ?
    """, (nom, prenom, email, telephone, cin, num_adh, adresse, date_entree, 
          age, genre, tarif, seances, situation, photo_path, adherent_id))

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