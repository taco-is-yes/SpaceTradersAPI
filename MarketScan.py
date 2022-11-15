import requests
import json
import os
import copy


def GetMarkets():
	MarketLocations = [
	 "OE-PM", "OE-PM-TR", "OE-CR", "OE-KO", "OE-UC", "OE-UC-AD", "OE-UC-OB",
	 "OE-NY", "OE-BO"
	]
	Markets = []
	for Location in MarketLocations:
		Mjson = json.loads(
		 requests.get(
		  f'https://api.spacetraders.io/locations/{Location}/marketplace?token={os.getenv("MARKETSCANTOKEN")}'
		 ).text)
		Mjson['location'] = Location
		Markets.append(Mjson)
	return (Markets)


def GetHighestProfitItem():
	HighestSellPrices = {}
	LowestBuyPrices = {}
	for Market in GetMarkets():
		for Item in Market['marketplace']:
			if Item['symbol'] in LowestBuyPrices:
				if LowestBuyPrices[Item['symbol']][0] > Item['purchasePricePerUnit']:
					LowestBuyPrices[Item['symbol']] = [
					 Item['purchasePricePerUnit'], Market['location'], Item['volumePerUnit']
					]
			else:
				LowestBuyPrices[Item['symbol']] = [
				 Item['purchasePricePerUnit'], Market['location'], Item['volumePerUnit']
				]
			if Item['symbol'] in HighestSellPrices:
				if HighestSellPrices[Item['symbol']][0] < Item['sellPricePerUnit']:
					HighestSellPrices[Item['symbol']] = [
					 Item['sellPricePerUnit'], Market['location'], Item['volumePerUnit']
					]
			else:
				HighestSellPrices[Item['symbol']] = [
				 Item['sellPricePerUnit'], Market['location'], Item['volumePerUnit']
				]

	ProfitPerItem = {}
	ProfitPerItemTemp = {}
	for Item in HighestSellPrices:
		ProfitPerItem[Item] = [
		 HighestSellPrices[Item][0] - LowestBuyPrices[Item][0],
		 LowestBuyPrices[Item][1], HighestSellPrices[Item][1],
		 HighestSellPrices[Item][2]
		]  #Profit, Buy location, Sell location
		if ProfitPerItem[Item][0] >= 0:
			ProfitPerItemTemp[Item] = ProfitPerItem[Item]
	ProfitPerItem = copy.copy(ProfitPerItemTemp)
	HighestProfitItem = ["G", 0, "FL", "TL", 0]
	for Item in ProfitPerItem:
		if ProfitPerItem[Item][0] > HighestProfitItem[1]:
			HighestProfitItem[0] = Item
			HighestProfitItem[1] = ProfitPerItem[Item][0]
			HighestProfitItem[2] = ProfitPerItem[Item][1]
			HighestProfitItem[3] = ProfitPerItem[Item][2]
			HighestProfitItem[4] = ProfitPerItem[Item][3]
	return HighestProfitItem