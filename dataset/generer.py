import sqlite3
#from faker import Faker
import random
from datetime import datetime, timedelta

from pathlib import Path

current_directory = Path(__file__).parent
racine = current_directory.parent 




path_data_set = racine / "dataset"/"royal_fitness.db"


print(path_data_set)
exit()

def creer_base_et_tables(nom_base):
    """Crée une base de données SQLite avec les tables adherents et paiements."""
    conn = sqlite3.connect(nom_base)
    cursor = conn.cursor()

    # Table adherents
    cursor.execute("""
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
        photo_path TEXT
    )
    """)

    # Table paiements
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS paiements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        adherent_id INTEGER,
        montant INTEGER,
        date_paiement DATE,
        mode_paiement TEXT,
        moi_concerner TEXT,
        FOREIGN KEY (adherent_id) REFERENCES adherents(id)
    )
    """)

    conn.commit()
    conn.close()

def generer_adherents(nom_base, nombre):
    """Génère des adhérents et les insère dans la base de données."""
    fake = Faker("fr_FR")
    conn = sqlite3.connect(nom_base)
    cursor = conn.cursor()

    for _ in range(nombre):
        nom = fake.last_name()
        prenom = fake.first_name()
        email = fake.email()
        telephone = fake.phone_number()
        cin = fake.bothify(text="??####")
        num_adh = fake.uuid4()[:8]
        adresse = fake.address()
        date_entree = fake.date_between(start_date="-5y", end_date="today")
        age = random.randint(18, 60)
        genre = random.choice(["Homme", "Femme"])
        tarif = random.choice([300, 400, 500])
        seances = random.randint(1, 20)
        situation = random.choice(["Paiement effectué", "Paiement non effectué"])
        photo_path = ""

        cursor.execute("""
        INSERT INTO adherents (nom, prenom, email, telephone, cin, num_adh, adresse, date_entree, age, genre, tarif, seances, situation, photo_path)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nom, prenom, email, telephone, cin, num_adh, adresse, date_entree, age, genre, tarif, seances, situation, photo_path))

    conn.commit()
    conn.close()

def generer_paiements(nom_base):
    """Génère des paiements pour chaque adhérent sur les 5 dernières années."""
    fake = Faker()
    conn = sqlite3.connect(nom_base)
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM adherents")
    adherents = [row[0] for row in cursor.fetchall()]

    modes_paiement = ["Espèces", "Carte bancaire", "Virement", "Chèque"]

    for adherent_id in adherents:
        for _ in range(10):  # Nombre aléatoire de paiements par adhérent
            montant = random.choice([300, 400, 500])
            date_paiement = fake.date_between(start_date="-5y", end_date="today")
            moi_concerner = date_paiement.strftime("%Y-%m")+"-01"
            mode_paiement = random.choice(modes_paiement)

            cursor.execute("""
            INSERT INTO paiements (adherent_id, montant, date_paiement, mode_paiement, moi_concerner)
            VALUES (?, ?, ?, ?, ?)
            """, (adherent_id, montant, date_paiement, mode_paiement, moi_concerner))

    conn.commit()
    conn.close()

def generer_depenses(nom_base):
    """Génère des dépéense pour chaque adhérent sur les 5 dernières années."""
    fake = Faker()
    conn = sqlite3.connect(nom_base)
    cursor = conn.cursor()

    for _ in range(500):  # Nombre aléatoire de paiements par adhérent
        montant = random.choice([300, 400, 500])
        date_paiement = fake.date_between(start_date="-5y", end_date="today")  
        commentaire="Commentaire"

        cursor.execute("""
        INSERT INTO depenses (commentaire, montant, date_depense )
        VALUES (?, ?, ?)
        """, (commentaire, montant, date_paiement))

    conn.commit()
    conn.close()

# Utilisation
if __name__ == "__main__":
    nom_base = path_data_set
    creer_base_et_tables(nom_base)
    generer_adherents(nom_base, 200)
    generer_paiements(nom_base)
    generer_depenses(nom_base)
    print("Base de données remplie avec succès !")
