import sqlite3 
 

# Connexion à la base de données SQLite
conn = sqlite3.connect("/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db")
cursor = conn.cursor()

# Création de la table adherents si elle n'existe pas
cursor.execute('''
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
conn.commit()
conn.close()