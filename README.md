# Python Simple API Client for CoinLore

Simple library for Python to use coinlore crypto api [Coinlore.com API](https://www.coinlore.com/cryptocurrency-data-api)

[Coinlore](https://www.coinlore.com) provides original cryptocurrency data, coin prices calculated by own algorithm, market caps, trade volumes and more, information updated every minute or less.

## Installation

```sh
pip install coinlore
```

## Usage
```python
from coinlore.client import Client

client = Client();

//Get Bitcoin Info (Bitcoin)
print(client.getcoin(90))

//Get coins from 0 to 100
print(client.getcoins(0, 100))

//Get coin markets (Bitcoin)
print(client.getmarkets(90))

//Get exchanges
print(client.getexchanges(5))

//Get exchange (Binance)
print(client.getexchange(5))

//Get social stats (Ethereum)
print(client.getsocial(80))

```
## License
MIT license