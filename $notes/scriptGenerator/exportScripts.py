from src import furnitureScripts
from src import buildingMaterialsScripts
from src import marketShopGen
from src import furnitureCutting
from src import bountifulEntries
if __name__ == "__main__":
	bountifulEntries.generateBountifulEntries()
	furnitureCutting.generateFurnitureCuttingRecipes()
	marketShopGen.generateMarketShops()
	buildingMaterialsScripts.exportScripts()
	furnitureScripts.exportTrades()
