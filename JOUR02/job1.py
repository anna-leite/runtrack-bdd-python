import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "LaPlateforme"
)

cursor = my_db.cursor()

cursor.execute("SELECT * FROM etudiant;")

etudiant = cursor.fetchall()

print(etudiant)

my_db.close()