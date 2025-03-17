import mysql.connector
from database import create_database_stock

class ManageDatabase:
    def __init__(self):
        self.stock = create_database_stock()
        self.connexion = None
        self.cursor = self.connexion.cursor()

    def connect(self):
        try:
            self.connexion = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "password",
                database = "Stock"
            ) 
        except mysql.connector.Error as e:
            print(f"Error connecting to the database : {e}")
            

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connexion:
            self.connexion.close()

    def create_table(self, table_name, columns):
        self.connect()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});")
        self.close()

    def insert(self, table_name, values):
        """add a new row in a table"""
        self.connect()
        query_create = f"INSERT INTO {table_name} VALUES ({values});"
        self.cursor.execute(query_create)
        self.connexion.commit()
        self.close()

    def read(self, table_name, columns, condition = "1=1"):
        """select and read informations from a table"""
        self.connect()
        query_read = f"SELECT {columns} FROM {table_name} WHERE {condition};"
        self.cursor.execute(query_read)
        results = self.cursor.fetchall()
        self.close()
        return results
    
    def update(self, table_name, updates, condition):
        self.connect()
        query_update = f"UPDATE {table_name} SET {updates} WHERE {condition};"
        self.cursor.execute(query_update)
        self.connexion.commit()
        self.close
    
    def delete(self, table_name, condition):
        self.connect()
        query_delete = f"DELETE FROM {table_name} WHERE {condition};"
        self.cursor.execute(query_delete)
        self.connexion.commit()
        self.close()

