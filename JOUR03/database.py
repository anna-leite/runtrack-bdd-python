import mysql.connector

def create_database_stock():
        """create an empty database"""
        connexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password"
        )

        cursor = connexion.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS Stock;")

        cursor.close()
        connexion.close()