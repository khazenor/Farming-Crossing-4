from input import buildingMaterials
from lib import kubejs
from src import const
import os

ticketCost = 1
craftOutputNumber = 32

def exportScripts():
	shapelessRecipeContent = ""

	for material in buildingMaterials.buildingMaterials:
		shapelessRecipeContent += kubejs.shapeless(material, [material, const.priceItem], craftOutputNumber)

	with open(os.path.join(const.serverScripts(), 'building_materials_crafting.js'), 'w') as f:
		f.write(kubejs.recipeFileContent(shapelessRecipeContent))

	with open(os.path.join(const.clientScripts(), 'building_materials_tooltips.js'), 'w') as tooltipFile:
		tooltipFile.write(kubejs.tooltipFileContent(kubejs.eventAdd(buildingMaterials.buildingMaterials, [
			"You can craft more of this block", "with Miles Tickets in a crafting table"
		])))
