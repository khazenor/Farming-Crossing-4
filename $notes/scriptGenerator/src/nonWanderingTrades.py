from input import wandererTrade1
from input import wandererTrade1NoRemove
from input import wandererTrade2
from lib import kubejs
import os
from src import const

profession = 'non_wandering_trader:traveller'
tradeExperience = 25
priceMultiplier = 0.035

commonKey = 'common'
rareKey = 'rare'
ticketPriceKey = "ticketPrice"
numCopiesKey = 'numCopies'
priceRarity = {
	commonKey: [
		{
			ticketPriceKey: 8,
			numCopiesKey: 4
		}, {
			ticketPriceKey: 4,
			numCopiesKey: 1
		}
	],
	rareKey: [
		{
			ticketPriceKey: 64,
			numCopiesKey: 4
		}, {
			ticketPriceKey: 40,
			numCopiesKey: 1
		}
	]
}


def genNonWanderingTrades():
	writeTrades()
	writeToolTips()
	kubejs.generateSimpleTags(
		wandererTrade1.items + wandererTrade1NoRemove.items + wandererTrade2.items,
		'forge:all_tradeables',
		'allTradeablesTag'
	)


def writeTrades():
	kubejsContent = ""

	for priceOccur in priceRarity[commonKey]:
		kubejsContent += villagerTradeContent(
			wandererTrade1.items,
			priceOccur[numCopiesKey],
			priceOccur[ticketPriceKey]
		)
		kubejsContent += villagerTradeContent(
			wandererTrade1NoRemove.items,
			priceOccur[numCopiesKey],
			priceOccur[ticketPriceKey]
		)
	for priceOccur in priceRarity[rareKey]:
		kubejsContent += villagerTradeContent(
			wandererTrade2.items,
			priceOccur[numCopiesKey],
			priceOccur[ticketPriceKey],
			5
		)


	with(open(os.path.join(const.serverScripts(), "non_wander_trade_sales.js"), "w")) as f:
		f.write(kubejs.villagerTradesContent(kubejsContent))


def villagerTradeContent(itemIds, numCopies, ticketPrice, level = -1):
	kubejsContent = ""
	for itemdIdx, itemId in enumerate(itemIds):
		if level == -1:
			tradeLevel = itemdIdx % 4 + 1
		else:
			tradeLevel = level
		for i in range(numCopies):
			kubejsContent += kubejs.villagerTradeWCallback(
				f"{ticketPrice}x kubejs:miles_ticket",
				itemId,
				profession,
				tradeLevel,
				tradeExperience,
				priceMultiplier
			)
	return kubejsContent

def writeToolTips():
	tradeableItemsCommon = wandererTrade1.items + wandererTrade1NoRemove.items

	tradeableItemsRare = wandererTrade2.items

	with open(os.path.join(const.clientScripts(), 'furniture_duplication_tooltips.js'), 'w') as f:
		f.write(kubejs.tooltipFileContent(
			kubejs.eventAdd(tradeableItemsCommon, [
				"Available at Jess\\'s shop (common section)"
			]) +
			kubejs.eventAdd(tradeableItemsRare, [
				"Available at Jess\\'s shop (rare section)"
			]) +
			kubejs.eventAdd(wandererTrade1.items, [
				"",
				"You can duplicate this furniture",
				"using the crafting table"
			])
		))


