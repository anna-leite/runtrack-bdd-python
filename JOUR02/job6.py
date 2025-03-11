import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "LaPlateforme"
)

cursor = my_db.cursor()

cursor.execute("SELECT SUM(capacite) FROM salle;")

resultat = cursor.fetchone()

print(f"La capacité de toutes les salles est de : {resultat[0]}")

my_db.close()