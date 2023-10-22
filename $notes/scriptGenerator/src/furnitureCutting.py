from lib import kubejs
from src import const
import os

def furnitureFolder():
	return os.path.join('input', 'furniture')

def tag(material):
	return f"forge:furniture_{material}"

cuttableFurnitureTag = 'forge:furniture_cuttable'

def tooltip():
	return ["Put this in a sawmill or stonecutter to", "convert it to another furniture"]

def generateFurnitureCuttingRecipes():
	tagContent = ""
	allCuttableTagContent = ""
	cuttingContent = ""
	allFurniture = readFurniture()
	allFurnitureList = []

	for material in allFurniture:
		furniture = allFurniture[material]
		allFurnitureList += furniture

		for i in range(len(furniture)):
			singleFurniture = furniture[i]

			# don't tag the first item:
			if i > 0:
				allCuttableTagContent += kubejs.eventAddSimple(cuttableFurnitureTag, singleFurniture)
			tagContent += kubejs.eventAddSimple(tag(material), singleFurniture)
			cuttingContent += kubejs.eventStonecutting(singleFurniture, f"#{tag(material)}")
			cuttingContent += kubejs.woodcutting(tag(material), singleFurniture, 1)

	with open(os.path.join(const.serverScripts(), 'furniture_cutting_recipes.js'), 'w') as cuttingFile:
		cuttingFile.write(kubejs.recipeFileContent(cuttingContent))

	with open(os.path.join(const.serverScripts(), 'furniture_cutting_tags.js'), 'w') as tagFile:
		tagFile.write(kubejs.tagsContent(tagContent))

	with open(os.path.join(const.serverScripts(), 'furniture_all_cuttable_tags.js'), 'w') as allTagFile:
		allTagFile.write(kubejs.tagsContent(allCuttableTagContent))

	with open(os.path.join(const.clientScripts(), 'furniture_cutting_tooltips.js'), 'w') as tooltipFile:
		tooltipFile.write(kubejs.tooltipFileContent(
			kubejs.eventAdd(allFurnitureList, tooltip())
		))

def readFurniture():
	allFurniture = {}
	for furnitureFile in os.listdir(furnitureFolder()):
		material = furnitureFile.replace('.txt', '')
		with open(os.path.join(furnitureFolder(), furnitureFile), 'r') as f:
			allFurniture[material] = f.read().split('\n')
	return allFurniture

