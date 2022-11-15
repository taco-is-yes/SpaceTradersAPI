import requests
from time import sleep
import os
import json
from MarketScan import GetHighestProfitItem

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
	HighestProfitItem = GetHighestProfitItem()
	print(HighestProfitItem)
	FlyTo("clahenpzw14448415s6z4b5pmyv", HighestProfitItem[2])
	BuyGoods("clahenpzw14448415s6z4b5pmyv", HighestProfitItem[0], 240)
	FlyTo("clahenpzw14448415s6z4b5pmyv",  HighestProfitItem[3])
	SellGoods("clahenpzw14448415s6z4b5pmyv", HighestProfitItem[0], 240)