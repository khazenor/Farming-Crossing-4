from list import collectionQuests as cqlist
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
commonRegularPrice = 8
rareRegularPrice = 64
jessTrades = [
	[], (
		cqlist.commonHandheldInstruments + cqlist.commonSnare + cqlist.commonBathroom + cqlist.commonArts
		+ cqlist.commonToy + cqlist.commonFilm + cqlist.commonTrophies
	), (
		cqlist.commonMariachi + cqlist.commonGraveyard + cqlist.commonFestive + cqlist.commonLab
		+ cqlist.commonBooksExploration +
		cqlist.commonPlushSheep + cqlist.commonPlushHorse
	), (
		cqlist.commonPlushHomeAnimal + cqlist.commonPlushCat + cqlist.commonPlushParrot
		+ cqlist.commonPlushFrog + cqlist.commonPlushLlama + cqlist.commonPlushWildAnimal + cqlist.commonPlushAxolotl
		+ cqlist.commonPlushWaterAnimal + cqlist.commonPlushVillage + cqlist.commonPlushNether + cqlist.commonPlushZombie
		+ cqlist.commonPlushRaid + cqlist.commonPlushHostileMob + cqlist.commonPlushBoss + cqlist.commonPlushRabbit
	),
	cqlist.allRareMusic,
	cqlist.allRareDeco
]
prices = [
	0, commonRegularPrice, commonRegularPrice, commonRegularPrice,
	rareRegularPrice,rareRegularPrice
]

def genNonWanderingTrades():
	writeTrades()
	writeToolTips()
	kubejs.generateSimpleTags(
		cqlist.allCommon + cqlist.allRare,
		'forge:all_tradeables',
		'allTradeablesTag'
	)
	updateRecipes()


def writeTrades():
	tradeContent = ""
	for level, shopItems in enumerate(jessTrades):
		for shopItem in shopItems:
			tradeContent += kubejs.villagerTradeWithDefaultSales(
				shopItem,
				1,
				const.priceItem,
				prices[level],
				profession,
				level,
				decreasePlayerNum=True
			)

	with(open(os.path.join(const.serverScripts(), "jess_shop_trades.js"), "w")) as f:
		f.write(kubejs.villagerTradesContent(tradeContent))

def writeToolTips():
	tradeableItemsCommon = cqlist.allCommon

	tradeableItemsRare = cqlist.allRare

	with open(os.path.join(const.clientScripts(), 'furniture_duplication_tooltips.js'), 'w') as f:
		f.write(kubejs.tooltipFileContent(
			kubejs.eventAdd(tradeableItemsCommon, [
				"Available at Jess\\'s shop (common section)",
				f"Regular Price: {commonRegularPrice} Tickets"
			]) +
			kubejs.eventAdd(tradeableItemsRare, [
				"Available at Jess\\'s shop (rare section)",
				f"Regular Price: {rareRegularPrice} Tickets"
			]) +
			kubejs.eventAdd(tradeableItemsCommon, [
				"",
				"You can duplicate this decoration",
				"using the crafting table"
			])
		))

def updateRecipes():
	recipeContent = ""
	for itemId in (cqlist.allCommon + cqlist.allRare):
		recipeContent += kubejs.removeRecipeOutput(itemId)
	for itemId in cqlist.allCommon:
		recipeContent += kubejs.shapeless(
			itemId, [
				itemId,
				const.priceItem
			],
			2
		)
	kubejs.writeServerFile(
		kubejs.recipeFileContent(recipeContent),
		'jess_shop_items_recipe_updates'
	)

