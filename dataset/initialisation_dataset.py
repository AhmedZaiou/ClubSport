import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from pathlib import Path
# Configuration de Faker
fake = Faker('fr_FR')

dataset = Path.home()/"dataset"
path_data_set = dataset/"royal_fitness.db"

def create_table():
    """Crée la table adherents si elle n'existe pas."""
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS adherents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prenom TEXT,
            email TEXT,
            telephone TEXT,
            cin TEXT,
            num_adh TEXT,
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
    conn.commit()
    conn.close()

def generate_adherent():
    """Génère un adhérent fictif."""
    genre = random.choice(['Homme', 'Femme'])
    return {
        'nom': fake.last_name(),
        'prenom': fake.first_name_male() if genre == 'Homme' else fake.first_name_female(),
        'email': fake.email(),
        'telephone': fake.phone_number(),
        'cin': fake.bothify(text='??####'),
        'num_adh': fake.unique.bothify(text='ADH####'),
        'adresse': fake.address(),
        'date_entree': (datetime.now() - timedelta(days=random.randint(0, 365 * 5))).strftime('%Y-%m-%d'),
        'age': random.randint(18, 60),
        'genre': genre,
        'tarif': random.choice([100, 200, 300, 400]),
        'seances': random.randint(10, 50),
        'situation': random.choice(["100", "200", "300", "400"]),
        'photo_path': "Aucune",
        'poids': f"{random.randint(50, 100)} kg",
        'longeur': f"{random.randint(150, 200)} cm",
        'titre_sport': random.choice(["Arats martiaux ","kick-boxing", "teak-wando", "karaté ", "Fitness-musculation ", "Aérobic", "zumba" , "gymnastique",  "buildings"]),
        'nom_parent': fake.name() if random.random() > 0.7 else None,
        'contact_parent': fake.phone_number() if random.random() > 0.7 else None,
        'situation_sanitaire': random.choice([ 'Inapte','Apte']),
        'situation_sanitaire_text': fake.sentence(nb_words=10) if random.random() > 0.5 else None
    }

def insert_adherents(n):
    """Insère n adhérents fictifs dans la base de données."""
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    adherents = [generate_adherent() for _ in range(n)]

    cursor.executemany('''
        INSERT INTO adherents (
            nom, prenom, email, telephone, cin, num_adh, adresse, date_entree, age,
            genre, tarif, seances, situation, photo_path, poids, longeur, titre_sport,
            nom_parent, contact_parent, situation_sanitaire, situation_sanitaire_text
        ) VALUES (
            :nom, :prenom, :email, :telephone, :cin, :num_adh, :adresse, :date_entree, :age,
            :genre, :tarif, :seances, :situation, :photo_path, :poids, :longeur, :titre_sport,
            :nom_parent, :contact_parent, :situation_sanitaire, :situation_sanitaire_text
        )
    ''', adherents)

    conn.commit()
    conn.close()




def generate_paiement(adherent_id):
    """Génère un paiement fictif pour un adhérent."""
    res = []
    for i in range(1,12):
        date_paiement = datetime.now()- relativedelta(months=i)
        moi_concerner = date_paiement.replace(day=1) 
        res.append( {
            'adherent_id': adherent_id,
            'montant': random.choice([100, 200, 300, 400]),
            'date_paiement': date_paiement.strftime('%Y-%m-%d'),
            'mode_paiement': random.choice(['Espèce', 'Chèque', 'Carte Bancaire']),
            'moi_concerner': moi_concerner.strftime('%Y-%m-%d')
        })
    return res


def insert_paiements(n):
    """Génère et insère des paiements pour chaque adhérent."""
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()
 
    adherent_ids = n 
 

    cursor.execute('''
        INSERT INTO paiements (adherent_id, montant, date_paiement, mode_paiement, moi_concerner)
    VALUES (?, ?, ?, ?, ?)
    ''', (str(adherent_ids[0]),adherent_ids[1],adherent_ids[2], adherent_ids[3], adherent_ids[4],))
    conn.commit()
    conn.close()


def generate_pays():
    for i in range(200):
        list_ = generate_paiement(i)
        for k in list_:
            insert_paiements([k[m] for m in k])


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

def adddepenses():

    # Connexion à la base SQLite
    conn = sqlite3.connect(path_data_set)
    cursor = conn.cursor()

    # Création de la table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS depenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        commentaire TEXT,
        montant INTEGER,
        date_depense DATE
    )
    ''')
    

    # Génération des données
    current_date = datetime.now()
    for month_offset in range(24):  # 24 derniers mois
        # Calculer le début du mois en cours
        start_date = current_date - relativedelta(months=month_offset)
        start_date = start_date.replace(day=1)  # Début du mois
        
        for _ in range(10):  # 10 dépenses par mois
            # Générer une date aléatoire dans le mois
            day = random.randint(1, 28)  # Pour éviter des problèmes avec des mois courts
            date_depense = start_date.replace(day=day).strftime('%Y-%m-%d')

            # Générer un commentaire et un montant aléatoires
            commentaire = f"Dépense du {date_depense}"
            montant = random.randint(10, 500)  # Montant entre 10 et 500

            # Insérer la dépense dans la table
            cursor.execute('''
            INSERT INTO depenses (commentaire, montant, date_depense)
            VALUES (?, ?, ?)
            ''', (commentaire, montant, date_depense))

    # Sauvegarder et fermer la connexion
    conn.commit()
    conn.close()

if __name__ == "__main__":
     
    create_table()
    insert_adherents(200)
    generate_pays()
    adddepenses()






    print("200 adhérents ont été ajoutés à la base de données.")
