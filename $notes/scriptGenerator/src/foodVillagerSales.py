from input import foodVillagerTrades
from lib import kubejs
from src import const
import os

# no longer in use

professionName = "villagersplus:horticulturist"
tradeExperience = 25
priceMultiplier = 0.035
numberToSell = 8

# priceMod to frequency
priceModFreq = {
	-1: 1,
	0: 4,
	2: 2,
	6: 1
}

def generateSales():
	trades = ""
	tradeEntries = foodVillagerTrades.villagerTrades
	for tradeLevel in tradeEntries:
		itemIds = tradeEntries[tradeLevel]
		for itemId in itemIds:
			basePrice = tradeLevel
			if tradeLevel == 1:
				trades += kubejs.villagerTradeWCallback(
					f'{numberToSell}x {itemId}',
					f"{basePrice}x kubejs:miles_ticket",
					professionName,
					tradeLevel,
					tradeExperience,
					priceMultiplier
				)
			else:
				for priceMod in priceModFreq:
					price = basePrice + priceMod
					if price > 0:
						freq = priceModFreq[priceMod]
						for i in range(freq):
							trades += kubejs.villagerTradeWCallback(
								f'{numberToSell}x {itemId}',
								f"{price}x kubejs:miles_ticket",
								professionName,
								tradeLevel,
								tradeExperience,
								priceMultiplier
							)

	with(open(os.path.join(const.serverScripts(), "food_villager_sales.js"), "w")) as f:
		f.write(kubejs.villagerTradesContent(trades))


