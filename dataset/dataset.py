    
import pandas as pd 
import sqlite3 
from datetime import datetime
def fetch_data():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")
    query = "SELECT * FROM adherents"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df 


def fetch_data_Non():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")  # Nom de votre fichier de base de données
    cursor = conn.cursor()

    # Récupérer uniquement les colonnes nécessaires
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

def fetch_data_all():
    """Récupère les données de la base SQLite"""
    conn = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")  # Nom de votre fichier de base de données
    cursor = conn.cursor()

    # Récupérer uniquement les colonnes nécessaires
    cursor.execute("SELECT id, nom, prenom, email, telephone, situation FROM adherents")
    adherents = cursor.fetchall()
    return adherents

def load_data( adherent_id):
        connection = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM adherents WHERE id = ?", (adherent_id,))
        row = cursor.fetchone()
        connection.close()  
        return row

def ajouter_adh(nom, prenom, email, telephone, cin, num_adh, adresse, date_entree,
        age, genre, tarif, seances, situation, photo_path):
    connection = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")
    cursor = connection.cursor()

    # Création de la table si elle n'existe pas encore
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS adherents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prenom TEXT,
            email TEXT,
            telephone TEXT,
            cin TEXT UNIQUE,
            num_adh TEXT UNIQUE,
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
    conn = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")
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
    conn = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO paiements (adherent_id, montant, date_paiement, mode_paiement, moi_concerner)
    VALUES (?, ?, ?, ?, ?)
    ''', (adherent_id, montant, date_paiement, mode_paiement, month_to_pay))

    conn.commit()
    conn.close()

def recuperer_paiements(adherent_id):
    conn = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")
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
    connection = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")
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
    conn = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")
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
    conn = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")
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

def recuperer_stat_paiment():
    conn = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")
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

 