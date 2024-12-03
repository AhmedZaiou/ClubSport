    
import pandas as pd 
import sqlite3 

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
    cursor.execute("SELECT id, nom, prenom, email, telephone, situation FROM adherents where situation = 'Paiement non effectué'")
    adherents = cursor.fetchall()
    return adherents

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
        moi_concerner TEXT,
        FOREIGN KEY (adherent_id) REFERENCES adherents (id)
    )
    ''')

    conn.commit()
    conn.close() 

def ajouter_paiement(adherent_id, montant, date_paiement, mode_paiement, moi_concerner=""):
    conn = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO paiements (adherent_id, montant, date_paiement, mode_paiement, moi_concerner)
    VALUES (?, ?, ?, ?, ?)
    ''', (adherent_id, montant, date_paiement, mode_paiement, moi_concerner))

    conn.commit()
    conn.close()

def recuperer_paiements(adherent_id):
    conn = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM paiements WHERE adherent_id = ? ORDER BY date_paiement DESC;
    ''', (adherent_id,))
    paiements = cursor.fetchall()

    conn.close()
    return paiements
