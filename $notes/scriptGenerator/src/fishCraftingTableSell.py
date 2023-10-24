from input import fishingWeights
from lib import kubejs
from lib import util
from src import const
import math
import os

numFishToSell = 4
maxFishPrice = 5

def price(fishWeight, highestWeight):
	return math.ceil(
		float(highestWeight - fishWeight) * maxFishPrice / float(highestWeight) + 0.5
	)

def tooltip(fishPrice):
	return [
		f'You can sell {numFishToSell} of these fishes',
		f'for {fishPrice} miles tickets'
	]

def generateFishSellingRecipe(fishPrices):
	recipeContent = ""
	for fish in fishPrices:
		recipeContent += kubejs.shapeless(
			const.priceItem,
			kubejs.multipleArray(fish, numFishToSell),
			fishPrices[fish]
		)
	with open(os.path.join(const.serverScripts(), 'fish_selling_recipes.js'), 'w') as sellingFile:
		sellingFile.write(kubejs.recipeFileContent(recipeContent))

def generateFishTooltips(fishPrices):
	fishByPrice = util.invertDict(fishPrices)
	tooltipContent = ""
	for fishPrice in fishByPrice:
		tooltipContent += kubejs.eventAdd(
			fishByPrice[fishPrice],
			tooltip(fishPrice)
		)
	with open(os.path.join(const.clientScripts(), 'fish_selling_tooltips.js'), 'w') as f:
		f.write(kubejs.tooltipFileContent(tooltipContent))

def generateFishCraftingSellRecipes():
	fishPrices = getFishPrices()

	generateFishSellingRecipe(fishPrices)
	generateFishTooltips(fishPrices)

def getFishPrices():
	fishWeights = fishingWeights.weights
	highestWeight = 0

	for fish in fishWeights:
		highestWeight = max(highestWeight, fishWeights[fish])

	fishPrices = {}
	for fish in fishWeights:
		fishPrices[fish] = price(fishWeights[fish], highestWeight)
	return fishPrices
