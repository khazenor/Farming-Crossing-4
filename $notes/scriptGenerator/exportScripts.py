from src import furnitureScripts
from src import buildingMaterialsScripts
from src import marketShopGen
from src import furnitureCutting
if __name__ == "__main__":
	furnitureCutting.generateFurnitureCuttingRecipes()
	marketShopGen.generateMarketShops()
	buildingMaterialsScripts.exportScripts()
	furnitureScripts.exportTrades()
