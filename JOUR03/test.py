import mysql.connector

class ManageDatabase:
    def __init__(self):
        self.stock = create_database()
        self.product = create_table()
        self.category = create_table()

    
    def connect(self):
        connexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password"
        )

        cursor = connexion.cursor()