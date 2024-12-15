import sqlite3  



from pathlib import Path

current_directory = Path(__file__).parent
racine = current_directory.parent 


path_data_set = racine / "dataset"/"royal_fitness.db"


def initialiser_dataset(path_data_set): 
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