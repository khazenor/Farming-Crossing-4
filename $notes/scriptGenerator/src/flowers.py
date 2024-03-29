from list import collectionQuests as cqlist
from lib import kubejs
from src import const
import os

craftOutputNumber = 3
paymentItem = "minecraft:bone_meal"

def generateDuplicationRecipes():
	shapelessRecipeContent = ""

	for flower in cqlist.floraAllFlowers:
		shapelessRecipeContent += kubejs.shapeless(flower, [flower, paymentItem], craftOutputNumber)

	with open(os.path.join(const.serverScripts(), 'flower_duplication_crafting.js'), 'w') as f:
		f.write(kubejs.recipeFileContent(shapelessRecipeContent))

	with open(os.path.join(const.clientScripts(), 'flower_duplication_tooltips.js'), 'w') as tooltipFile:
		tooltipFile.write(kubejs.tooltipFileContent(kubejs.eventAdd(cqlist.floraAllFlowers, [
			"You can craft more of this flower", "with Bone Meal in a crafting table"
		])))
