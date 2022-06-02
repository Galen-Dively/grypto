import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

def getCoins():
    url = "https://crypto.com/price"
    text = requests.get(url).text # get html in text
    soup = BeautifulSoup(text, "html.parser") # parse html

    coins = []
    # get where info is stored
    rows = soup.findAll("tr")
    rows.pop(0) # get rid of the first row as it has no useful info
    for row in rows:
        sets = row.findAll("td")
        sets.pop(0)
        name = sets[1].text[1:] # gets rid of random first character

        # trying to get rid of ticker
        # if ticker is three
        ticker = len(name)

        for i in range(2, 6):
            if name[len(name)-i].upper() == name[len(name)-i]:
                ticker = i


        # print(sets[1].text)
        data = sets[2].text.split("$")
        data.pop(0)
        price = float(data[0].replace(",", ""))
        negChange = data[1].split("-")
        posChange = data[1].split("+")
        if len(negChange) == 2:
            dayChange = negChange
            symbol = "-"
        if len(posChange) == 2:
            dayChange = posChange
            symbol = "+"

        coin = {"Position": sets[0].text, "Day Change": dayChange[1], "Symbol": symbol, "Price": price, "Name": name[:len(name)-ticker]}
        coins.append(coin)
    return coins

# for i in range(0, 100):
#     print("Getting Prices")
#     coins = getCoins()
#     coins = {"Coins": coins}
#     saveToJson(coins)
#     print("Saved and now waiting")
#     time.sleep(61)
