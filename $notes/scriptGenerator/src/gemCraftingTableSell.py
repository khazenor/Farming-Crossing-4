from input import gemRarity
from lib import kubejs
from lib import util
from src import const
import math
import os

numGemToSell = 4

def price(gemWeight, highestWeight):
	return math.ceil(
		float(highestWeight - gemWeight) * maxGemPrice / float(highestWeight) + 0.5
	)

def tooltip(gemPrice):
	return [
		f'You can sell {numGemToSell} of these gems',
		f'for {gemPrice} miles tickets'
	]

def generateGemSellingRecipe(gemPrices):
	recipeContent = ""
	for gem in gemPrices:
		recipeContent += kubejs.shapeless(
			const.priceItem,
			kubejs.multipleArray(gem, numGemToSell),
			gemPrices[gem]
		)
	with open(os.path.join(const.serverScripts(), 'gem_selling_recipes.js'), 'w') as sellingFile:
		sellingFile.write(kubejs.recipeFileContent(recipeContent))

def generateGemTooltips(gemPrices):
	gemByPrice = util.invertDict(gemPrices)
	tooltipContent = ""
	for gemPrice in gemByPrice:
		tooltipContent += kubejs.eventAdd(
			gemByPrice[gemPrice],
			tooltip(gemPrice)
		)
	with open(os.path.join(const.clientScripts(), 'gem_selling_tooltips.js'), 'w') as f:
		f.write(kubejs.tooltipFileContent(tooltipContent))

def getGemPrices():
	gemRates = gemRarity.gemRates
	gemPrices = {}

	for gemRate in gemRates:
		for gemId in gemRates[gemRate]:
			gemPrices[gemId] = gemRate
	return gemPrices

def generateGemCraftingSellRecipes():
	gemPrices = getGemPrices()

	generateGemSellingRecipe(gemPrices)
	generateGemTooltips(gemPrices)