from src.database import DatabaseManager # controls database
from src.getCoins import getCoins # gets the coin info

# TODO: refactor databaseManager, insertData is to complicated with not so good
# code,
# features: save databases, select databases, 


class App:
    def __init__(self):
        self.coins = getCoins() # returns a list of dictionarys storing coins
        self.databaseManager = DatabaseManager()

        # write to database
        # loop trough each dictionary in self.coins()
        # creates a table in database,stored in dict
        # {"Name: (str) name of table, "Vars"; a list of vars in table}
        for coin in self.coins:
            self.databaseManager.insertData({"Name": "cryptos", "Vars": ["DayChange", "Name", "Price"]}, [coin["Day Change"].replace("%", ""), coin["Name"], coin["Price"]])


        # # debuging
        # self.databaseManager.createTable("Cryptos", columns=[{"Name": "Price", "Datatype": "VARCHAR(255)"},
        #                                                      {"Name": "Name", "Datatype": "VARCHAR(255)"}])
