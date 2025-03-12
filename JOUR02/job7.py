import mysql.connector

# Connexion à MySQL
# conex = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "password"
# )
# cursor = conex.cursor()
# Création de la base de donnée si elle n'existe pas 
# cursor.execute("CREATE DATABASE IF NOT EXISTS entreprise;")
# Séléction de la base de données
# cursor.execute("USE entreprise;")
# cursor.close()
# conex.close()


# Solution avec "with"
# Connexion à MySQL
with mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password"
) as conn :
    with conn.cursor() as cursor :
        # Création de la base de données si elle n'existe pas
        cursor.execute("CREATE DATABASE IF NOT EXISTS entreprise;")

        # Sélection de la base de donnée
        cursor.execute("USE entreprise;")

        # Création d'une table employe
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS employe(
                           id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                           nom VARCHAR(255) NOT NULL,
                           premon VARCHAR(255) NOT NULL,
                           salaire DECIMAL(10, 2) NOT NULL,
                           id_service INT NOT NULL
                       )
                       """)
        
        # Création d'une table service
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS service(
                           id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                           nom VARCHAR(255) NOT NULL
                       )
                       """)        




def inserer_employe(e_nom, e_prenom, e_salaire, e_id_service):
    with mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "password",
        database = "entreprise"
    ) as conn :
        with conn.cursor() as cursor:
            # Vérifier qu'il n'y a pas de doublon
            sql_check = "SELECT COUNT(*) FROM employe WHERE nom = %s AND premon = %s;"
            cursor.execute(sql_check, (e_nom, e_prenom))
            result = cursor.fetchone()

            if result[0] > 0:
                print("L'employé existe déjà, insertion annulé.")
                return

            # Ajout d'un salarié avec une requête paramétrée
            sql_insert = "INSERT INTO employe(nom, premon, salaire, id_service) VALUES (%s, %s, %s, %s);"
            valeurs = (e_nom, e_prenom, e_salaire, e_id_service)
            cursor.execute(sql_insert, valeurs)
            # Commit les changement sur la connexion
            conn.commit()

# inserer_employe("Dupont", "Jean", 1500.00, 1)
# inserer_employe("Dupuis", "Jérôme", 2000.00, 2)
# inserer_employe("Dubois", "Adèle", 2500.00, 3)
# inserer_employe("Pontavel", "Marie", 3500.00, 4)
# inserer_employe("Moulin", "Ange", 4000.00, 4)
# inserer_employe("Groupama", "Cerise", 2900.00, 3)

# # Requête SQL pour récuper tous les employés dont le salaire est supérieur à 3000
# with mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "password",
#     database = "entreprise"
# ) as conn :
#     with conn.cursor() as cursor :
#         cursor.execute("SELECT * FROM employe WHERE salaire > 3000;")
#         resultats = cursor.fetchall()
#         # print(resultats)

#         # Récupération des noms des colonnes
#         colonnes = [desc[0] for desc in cursor.description]

#         # Affichage formaté
#         print("\nListe des employés avec un salaire supérieur à 3000€ :\n")
#         for ligne in resultats:
#             print(" | ".join(f"{col}: {val}" for col, val in zip(colonnes, ligne)))
#             print("-" * 50)  # Séparateur entre chaque ligne


def inserer_service(s_nom):
    with mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "password",
        database = "entreprise"
    ) as conn :
        with conn.cursor() as cursor:
            # Ajout d'un service avec une requête paramétrée
            sql_insert = "INSERT INTO service (nom) VALUES (%s);"
            valeurs = (s_nom,) # on passe par un tuple
            cursor.execute(sql_insert, valeurs)
            # Commit les changement sur la connexion
            conn.commit()

# inserer_service("alternant")
# inserer_service("développeur")
# inserer_service("devops")
# inserer_service("ingénieur logiciel")


