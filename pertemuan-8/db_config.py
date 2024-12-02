import mysql.connector


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="127.0.0.1", user="root", password="root", database="inventory_db"
        )
        self.cursor = self.connection.cursor()

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def fetchAll(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetchOne(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()
