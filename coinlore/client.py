#!/usr/bin/env python
import requests

class Client:

    def getglobal(self):
        self.r = requests.get('https://api.coinlore.com/api/global/')
        return self.r.json()[0]

    def getcoin(self, coin):
        self.r = requests.get('https://api.coinlore.com/api/ticker/?id=' + str(coin))
        return self.r.json()[0]

    def getcoins(self, start='0', limit='100'):
        if start.isnumeric() == False:
            start = 0;
        if limit.isnumeric() == False:
            limit = 100;
        self.r = requests.get('https://api.coinlore.com/api/tickers/?start=' + str(start) + '&limit=' + str(limit))
        return self.r.json()

    def getmarkets(self, coin):
        self.r = requests.get('https://api.coinlore.com/api/coin/markets/?id=' + str(coin))
        return self.r.json()

    def getsocial(self, coin):
        self.r = requests.get('https://api.coinlore.com/api/coin/social_stats/?id=' + str(coin))
        return self.r.json()

    def getexchange(self, exchange):
        self.r = requests.get('https://api.coinlore.com/api/exchange/?id=' + str(exchange))
        return self.r.json()

    def getexchanges(self):
        self.r = requests.get('https://api.coinlore.com/api/exchanges/')
        return self.r.json()
