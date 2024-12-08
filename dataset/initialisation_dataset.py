import sqlite3  



from pathlib import Path

current_directory = Path(__file__).parent
racine = current_directory.parent 




path_data_set = racine / "dataset"/"royal_fitness.db"


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
cursor.execute('''
    CREATE TABLE IF NOT EXISTS depenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        commentaire TEXT,
        montant INTEGER,
        date_depense DATE
    )
    ''')

conn.commit()
conn.close()