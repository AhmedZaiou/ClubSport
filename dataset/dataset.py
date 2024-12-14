    
import pandas as pd 
import sqlite3 
from datetime import datetime
#from utils.utils import *
import calendar
path_data_set = "/Users/ahmedzaiou/Documents/Project-Taza/git/ClubSport/dataset/royal_fitness.db"

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
        poids, longeur, titre_sport, nom_parent, contact_parent, situation_sanitaire, situation_sanitaire_text):
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
            situation_sanitaire_text TEXT
        )
    """)

    # Insertion des données dans la table
    cursor.execute("""
        INSERT INTO adherents (
            nom, prenom, email, telephone, cin, num_adh, adresse,
            date_entree, age, genre, tarif, seances, situation, photo_path, poids, longeur, titre_sport, nom_parent, contact_parent, situation_sanitaire, situation_sanitaire_text
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (nom, prenom, email, telephone, cin, num_adh, adresse, date_entree,
        age, genre, tarif, seances, situation, photo_path, poids, longeur, titre_sport, nom_parent, contact_parent, situation_sanitaire, situation_sanitaire_text))

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
    SELECT adherent_id, moi_concerner, montant, mode_paiement, date_paiement  FROM paiements WHERE adherent_id = ? ;
    ''', (adherent_id,))
    paiements = cursor.fetchall()

    conn.close()
    return paiements

def modifier_adh(adherent_id, nom, prenom, email, telephone, cin, num_adh, adresse, 
                        date_entree, age, genre, tarif, seances, situation, photo_path
                        , poids, longeur, titre_sport, nom_parent, contact_parent, situation_sanitaire, situation_sanitaire_text):
     
    connection = sqlite3.connect(path_data_set)
    cursor = connection.cursor()

    # Requête SQL de mise à jour
    cursor.execute("""
        UPDATE adherents
        SET 
            nom = ?, prenom = ?, email = ?, telephone = ?, cin = ?, 
            num_adh = ?, adresse = ?, date_entree = ?, age = ?, 
            genre = ?, tarif = ?, seances = ?, situation = ?, photo_path = ?,
             poids = ?, longeur = ?, titre_sport = ?, nom_parent = ?, contact_parent = ?, situation_sanitaire = ?, situation_sanitaire_text = ?
        WHERE id = ?
    """, (nom, prenom, email, telephone, cin, num_adh, adresse, date_entree, 
          age, genre, tarif, seances, situation, photo_path, 
          poids, longeur, titre_sport, nom_parent, contact_parent, situation_sanitaire, situation_sanitaire_text,adherent_id,))

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