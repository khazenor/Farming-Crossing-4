from lib import minecraftRecipes
from lib import pythonHelpers
from src import const
import os
import json

def cookingRecipe(result, ingIds, cookingTime=200, experience=1.0, recipeBookTab="meals", container=None):
	outDict = {
		"type": "farmersdelight:cooking",
		"cookingtime": cookingTime,
		"experience": experience,
		"ingredients": minecraftRecipes.ingredientList(ingIds),
		"recipe_book_tab": recipeBookTab,
		"result": minecraftRecipes.kubejsToItemDict(result)
	}
	if container:
		outDict = pythonHelpers.mergeDicts(outDict, {"container": minecraftRecipes.kubejsToItemDict(container)})
	return outDict

def genCookingRecipe(result, ingIds, cookingTime=200, experience=1.0, recipeBookTab="meals", container=None):
	json.dump(
		cookingRecipe(result, ingIds, cookingTime, experience, recipeBookTab, container),
		open(os.path.join(const.farmersDelightCooking(), minecraftRecipes.fileNameFromKubejs(result)+".json"), 'w'),
		indent=2
	)