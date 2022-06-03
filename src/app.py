from src.database import DatabaseManager
from src.getCoins import getCoins


class App:
    def __init__(self):
        self.coins = getCoins()
        print(self.coins)
        self.databaseManager = DatabaseManager()
        # write to database
        for coin in self.coins:
            self.databaseManager.insertData({"Name"})

        # # debuging
        # self.databaseManager.createTable("Cryptos", columns=[{"Name": "Price", "Datatype": "VARCHAR(255)"},
        #                                                      {"Name": "Name", "Datatype": "VARCHAR(255)"}])
