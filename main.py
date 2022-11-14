import requests
from time import sleep
import os
import json
import re

def SellGoods(ShipId, GoodId, Amount):
	requests.post('https://api.spacetraders.io/my/sell-orders', params={'shipId': ShipId, 'good': GoodId, 'quantity': Amount, 'token': os.getenv("TOKEN")})

def BuyGoods(ShipId, GoodId, Amount):
	requests.post('https://api.spacetraders.io/my/sell-orders', params={'shipId': ShipId, 'good': GoodId, 'quantity': Amount, 'token': os.getenv("TOKEN")})

def FlyTo(ShipId, Destination):
	ResJson = requests.post('https://api.spacetraders.io/my/flight-plans', params={'shipId': ShipId, 'destination': Destination, "token": os.getenv("TOKEN")}).text
	ResJson=json.loads(ResJson)
	try:
		sleep(ResJson["flightPlan"]["timeRemainingInSeconds"])
	except:
		requests.post('https://api.spacetraders.io/my/purchase-orders', params={'shipId': ShipId, 'good': 'FUEL', 'quantity': int(re.search(r'\d+',ResJson['error']['message']).group()), 'token': os.getenv("TOKEN")})
		FlyTo(ShipId, Destination)

while True:
	BuyGoods("clag1cyu459697816s6koq9kcme", "FUEL", 2)
	FlyTo("clag1cyu459697816s6koq9kcme", "OE-PM-TR")
	print("Traveled")
	BuyGoods("clag1cyu459697816s6koq9kcme", "METALS", 99)
	BuyGoods("clag1cyu459697816s6koq9kcme", "FUEL", 1)
	print("Bought")
	FlyTo("clag1cyu459697816s6koq9kcme", "OE-PM")
	print("Traveled")
	SellGoods("clag1cyu459697816s6koq9kcme", "METALS", 98)
	print("Sold")