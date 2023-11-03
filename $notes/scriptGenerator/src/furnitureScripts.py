from lib import kubejs, lootBags
from input import wandererTrade1
from input import wandererTrade2
from input import wandererTrade1NoRemove
from input import wandererTrade1RemoveNoDuplicate
from input import wandererTrade2NoRemove
from src import const
import json, os

def exportTrades():
	tradeStrs = ""
	recipeString = ""

	paymentNum = 8
	for output in wandererTrade1.items:
		tradeStrs += kubejs.tradeStr(output, const.priceItem, paymentNum)
		recipeString += kubejs.removeRecipeOutput(output)
		recipeString += kubejs.shapeless(output, [
			output, const.priceItem
		], outputNum=2)

	for output in wandererTrade1NoRemove.items:
		tradeStrs += kubejs.tradeStr(output, const.priceItem, paymentNum)

	for output in wandererTrade1RemoveNoDuplicate.items:
		tradeStrs += kubejs.tradeStr(output, const.priceItem, paymentNum)
		recipeString += kubejs.removeRecipeOutput(output)
		


	paymentNum = 64
	for output in wandererTrade2.items:
		recipeString += kubejs.removeRecipeOutput(output)
		tradeStrs += kubejs.tradeStr(output, const.priceItem, paymentNum, level=2)

	for output in wandererTrade2NoRemove.items:
		tradeStrs += kubejs.tradeStr(output, const.priceItem, paymentNum, level=2)

	tradeableItemsCommon = wandererTrade1.items + wandererTrade1NoRemove.items\
		+ wandererTrade1RemoveNoDuplicate.items

	tradeableItemsRare = wandererTrade2.items + wandererTrade2NoRemove.items

	with open(os.path.join(const.clientScripts(), 'furniture_duplication_tooltips.js'), 'w') as f:
		f.write(kubejs.tooltipFileContent(
			kubejs.eventAdd(tradeableItemsCommon, [
				"Available at the wandering trader shop (common section)"
			]) +
			kubejs.eventAdd(tradeableItemsRare, [
				"Available at the wandering trader shop (rare section)"
			]) +
			kubejs.eventAdd(wandererTrade1.items, [
				"",
				"You can duplicate this furniture",
				"using the crafting table"
			])
		))

	allTradeableItems = tradeableItemsRare + tradeableItemsCommon
	tagContent = ""
	for itemId in allTradeableItems:
		tagContent += kubejs.eventAddSimple('forge:all_tradeables', itemId)

	with open(os.path.join(const.serverScripts(), 'allTradeablesTag.js'), 'w') as f:
		f.write(kubejs.tagsContent(tagContent))

	with open(os.path.join(const.serverScripts(), 'wandering_trades.js'), 'w') as f:
		f.write(kubejs.wanderingTradeFileContent(tradeStrs))
	with open(os.path.join(const.serverScripts(), 'furniture_recipes.js'), 'w') as f:
		f.write(kubejs.recipeFileContent(recipeString))
	json.dump(
		lootBags.defaultOutput("Furniture Kit", lootBags.entries(wandererTrade1.items)),
		open('../../kubejs/data/lootbags/recipes/furniture/loot_furniture.json', 'w'),
		indent=2
	)