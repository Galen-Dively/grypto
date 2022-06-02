from src.database import DatabaseManager
from src.getCoins import getCoins


class App:
    def __init__(self):
        self.coins = getCoins()
        self.databseManager = DatabaseManager()
