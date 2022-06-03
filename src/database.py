import mysql.connector
import json


# TODO: Get config data

class DatabaseManager:
    def __init__(self):
        self.database = self.connect()
        self.cursor = self.database.cursor()

    def connect(self):
        # get sql info from config file
        with open("src/config.json", "r") as f:
            databaseConfig = json.load(f)["Config"]

        mydb = mysql.connector.connect(
            host=databaseConfig["Host"],
            user=databaseConfig["User"],
            password=databaseConfig["Password"],
            database=databaseConfig["Database"]
        )
        return mydb

    def createTable(self, name, **kwargs):
        # kwargs dict {"name", "datatype"}
        columns = kwargs["columns"]
        command = f"CREATE TABLE {name} (" # command to create database
        for column in columns:
            if columns.index(column) == 0:
                command =  f"{command}{column['Name']} {column['Datatype']}" # adding first colmn and last
            elif columns.index(column) < len(columns):
                command = f"{command} ,{column['Name']} {column['Datatype']}" # adding first colmn
        command = f"{command})"

        try:
            self.cursor.execute(command)
        except Exception as e:
            pass

    def insertData(self, table, values):
        # get table details
        command=""
        # stored as dict {"Name": name of table, "Vars": list of vars in order}
        tableVars = table["Vars"]
        tableNames = table["Name"]
        insertCommand = f"INSERT INTO {tableNames} ("

        for var in tableVars:
            insertCommand = f"{insertCommand}{var},"

        insertCommand = f"{insertCommand[:-1]})" # gets rid of last comma
        print(insertCommand)
        # self.cursor.execute(insertCommand)
        # add values
        valuesCommand = "VALUES ("
        for value in values:
            valuesCommand = f"{valuesCommand}{value},"

        valuesCommand = f"{valuesCommand[:-1]}"
        valuesCommand = f"{valuesCommand});"
        print(valuesCommand)
        # self.cursor.execute(valuesCommand)
        self.cursor.execute(f"{insertCommand} {valuesCommand}")
        self.database.commit()
