import requests
from time import sleep
import os
import json

def SellGoods(ShipId, GoodId, Amount):
	requests.post('https://api.spacetraders.io/my/sell-orders', params={'shipId': ShipId, 'good': GoodId, 'quantity': Amount, 'token': os.getenv("TOKEN")})

def BuyGoods(ShipId, GoodId, Amount):
	requests.post('https://api.spacetraders.io/my/purchase-orders', params={'shipId': ShipId, 'good': GoodId, 'quantity': Amount, 'token': os.getenv("TOKEN")})

def FlyTo(ShipId, Destination):
	ResJson = requests.post('https://api.spacetraders.io/my/flight-plans', params={'shipId': ShipId, 'destination': Destination, "token": os.getenv("TOKEN")}).text
	ResJson=json.loads(ResJson)
	try:
		sleep(ResJson["flightPlan"]["timeRemainingInSeconds"])
	except:
		if ResJson['error']['code'] != 3003:
			requests.post('https://api.spacetraders.io/my/purchase-orders', params={'shipId': ShipId, 'good': 'FUEL', 'quantity': 1, 'token': os.getenv("TOKEN")})
			FlyTo(ShipId, Destination)
		else:
			print(ResJson)

while True:
	BuyGoods("clag1cyu459697816s6koq9kcme", "FUEL", 2)
	print("Bought")
	FlyTo("clag1cyu459697816s6koq9kcme", "OE-PM-TR")
	print("Traveled")
	BuyGoods("clag1cyu459697816s6koq9kcme", "METALS", 99)
	BuyGoods("clag1cyu459697816s6koq9kcme", "FUEL", 1)
	print("Bought")
	FlyTo("clag1cyu459697816s6koq9kcme", "OE-PM")
	print("Traveled")
	SellGoods("clag1cyu459697816s6koq9kcme", "METALS", 99)
	print("Sold")