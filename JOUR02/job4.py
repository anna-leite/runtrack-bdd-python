import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "LaPlateforme"
)

cursor = my_db.cursor()

cursor.execute("SELECT nom, capacite FROM salle;")

resultat = cursor.fetchall()

print(resultat)

my_db.close()