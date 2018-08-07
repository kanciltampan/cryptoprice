import requests, json

req = requests.get("https://api.coinmarketcap.com/v2/ticker/1/")
parsing = req.json()

tampilkan = parsing['data']['quotes']['USD']['price']
print("Harga BTC : $",tampilkan)