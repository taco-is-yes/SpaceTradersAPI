import requests
from os import getenv
from time import sleep

TravelToOEPMS1 = {'destination': 'OE-PM', 'shipId': 'value1'}
TravelToOEPMTRS1 = {'destination': 'OE-PM-TR', 'shipId': 'value1'}
BuyFuelS1 = {'good': 'FUEL', 'shipId': 'value1', "quantity": 50}
SellFuelS1 = {'good': 'FUEL', 'shipId': 'value1', "quantity": 50}

TravelToOEPMS2 = {'destination': 'OE-PM', 'shipId': 'value2'}
TravelToOEPMTRS2 = {'destination': 'OE-PM-TR', 'shipId': 'value2'}
BuyFuelS2 = {'good': 'FUEL', 'shipId': 'value2', "quantity": 100}
SellFuelS2 = {'good': 'FUEL', 'shipId': 'value2', "quantity": 100}

while True:
	requests.get('https://api.spacetraders.io/my/flight-plans', auth=getenv("TOKEN"), params=TravelToOEPMTRS1)
	requests.get('https://api.spacetraders.io/my/flight-plans', auth=getenv("TOKEN"), params=TravelToOEPMTRS2)
	sleep(33)
	requests.get('https://api.spacetraders.io/my/purchase-orders', auth=getenv("TOKEN"), params=BuyFuelS1)
	requests.get('https://api.spacetraders.io/my/purchase-orders', auth=getenv("TOKEN"), params=BuyFuelS2)
	print("Bought")
	#buy
	requests.get('https://api.spacetraders.io/my/flight-plans', auth=getenv("TOKEN"), params=TravelToOEPMS1)
	requests.get('https://api.spacetraders.io/my/flight-plans', auth=getenv("TOKEN"), params=TravelToOEPMS2)
	sleep(33)
	requests.get('https://api.spacetraders.io/my/flight-plans', auth=getenv("TOKEN"), params=TravelToOEPMTRS1)
	requests.get('https://api.spacetraders.io/my/flight-plans', auth=getenv("TOKEN"), params=TravelToOEPMTRS2)
	print("Sold")
	#sell22