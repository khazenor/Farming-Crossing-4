from input import bountifulQuestItems
from input import fishingWeights
from lib import bountiful
from src import const
from lib import pythonHelpers
import os

numObjKey = 'numObj'
weightMultKey = "weightMult"

def generateBountifulEntries():
	generateObjectives()

def generateObjectives():
	filename = "farming_crossing_4_objectives.json"
	pythonHelpers.exportJson(
		bountiful.fileContent(bountifulEntries()),
		os.path.join(const.bountifulPools(), filename)
	)

def bountifulEntries():
	determineObjWeights() # weights stored in bountifulQuestItems.bountyCategories
	objEntries = []
	for category in bountifulQuestItems.bountyCategories:
		if category[bountifulQuestItems.categoryKey] == bountifulQuestItems.fishKey:
			objEntries += fishObjEntries(category)
		elif category[bountifulQuestItems.categoryKey] == bountifulQuestItems.cookingKey:
			objEntries += cookingObjEntries(category)
		else: # deco
			objEntries += decoObjEntries(category)
	return objEntries

def fishObjEntries(category):
	numContent = 2
	objEntries = []
	weightMult = category[weightMultKey]
	for itemId in category[bountifulQuestItems.itemsKey]:
		fishWeight = fishingWeights.weights[itemId]
		if fishWeight < 10:
			worth = 3000
		elif fishWeight < 40:
			worth = 1500
		else:
			worth = 1000
		objEntries.append(bountiful.bountyObjSimple(itemId, numContent, worth, weightMult))
	return objEntries

def cookingObjEntries(category):
	numContent = 4
	unitWorth = 1500
	return simpleObjEntries(numContent, unitWorth, category)

def decoObjEntries(category):
	numContent = 1
	unitWorth = 1000
	return simpleObjEntries(numContent, unitWorth, category)

def simpleObjEntries(numContent, unitWorth, category):
	objEntries = []
	weightMult = category[weightMultKey]

	for itemId in category[bountifulQuestItems.itemsKey]:
		objEntries.append(bountiful.bountyObjSimple(itemId, numContent, unitWorth, weightMult))

	return objEntries

def determineObjWeights():
	categories = bountifulQuestItems.bountyCategories
	for category in categories:
		category[numObjKey] = len(category[bountifulQuestItems.itemsKey])

	for i in range(len(categories)):
		category = categories[i]
		if i == 0:
			category[weightMultKey] = 5
		else:
			previousCategory = categories[i-1]
			previousCategoryTotalWeight = previousCategory[numObjKey] * previousCategory[weightMultKey]
			previousCategoryRatio = previousCategory[bountifulQuestItems.weightKey]
			currentCategoryDesiredRatio = category[bountifulQuestItems.weightKey]
			currentCategoryDesiredWeight = float(previousCategoryTotalWeight)/float(previousCategoryRatio) * currentCategoryDesiredRatio
			category[weightMultKey] = round(currentCategoryDesiredWeight/category[numObjKey], 1)
