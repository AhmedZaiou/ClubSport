import sqlite3
from faker import Faker
import random

# Configuration de Faker
fake = Faker()
Faker.seed(0)

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

# Génération de 2000 adhérents
adherents = []
cin_set = set()
num_adh_set = set()

for _ in range(20):
    nom = fake.last_name()
    prenom = fake.first_name()
    email = fake.email()
    telephone = fake.phone_number()
    
    # Générer des valeurs uniques pour CIN et num_adh
    cin = fake.unique.ssn()  # CIN unique
    while cin in cin_set:
        cin = fake.unique.ssn()
    cin_set.add(cin)

    num_adh = fake.unique.random_number(digits=8, fix_len=True)  # Numéro adhérent unique
    while num_adh in num_adh_set:
        num_adh = fake.unique.random_number(digits=8, fix_len=True)
    num_adh_set.add(num_adh)

    adresse = fake.address()
    date_entree = fake.date_this_decade(before_today=True)
    age = random.randint(18, 70)
    genre = random.choice(["Homme", "Femme"])
    tarif = random.randint(100, 1000)
    seances = random.randint(10, 50)
    situation = random.choice(["Paiement effectué", "Paiement non effectué"])
    photo_path = "/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/images/logos/profile.png"
    
    adherents.append((
        nom, prenom, email, telephone, cin, num_adh, adresse, date_entree,
        age, genre, tarif, seances, situation, photo_path
    ))

# Insertion des données dans la base de données
cursor.executemany('''
INSERT INTO adherents (
    nom, prenom, email, telephone, cin, num_adh, adresse, date_entree,
    age, genre, tarif, seances, situation, photo_path
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', adherents)

conn.commit()
conn.close()

print("2000 lignes insérées dans la table adherents.")
