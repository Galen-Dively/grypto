import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.database = self.connect()
        self.cursor = self.database.cursor()

    def connect(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = ""
        )
        return mydb

    def createDatabase(self, database):
        self.cursor.execute(f"CREATE DATABASE {database}")

    def createTable(self, name, **kwargs):
        # kwargs dict {"name", "datatype"}
        columns = **kwargs["Columns"]
        command = f"CREATE TABLE {name}"
        for column in columns:
            command = command+ f" ({column["Name"]} {column["Datatype"]})"
