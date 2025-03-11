import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "LaPlateforme"
)

cursor = my_db.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage;")

resultat = cursor.fetchone()

print(f"La superficie de la Plateforme est de {resultat[0]} m2")

my_db.close()