from src import furnitureScripts
from src import fishCraftingTableSell
from src import buildingMaterialsScripts
from src import marketShopGen
if __name__ == "__main__":
	marketShopGen.generateMarketShops()
	buildingMaterialsScripts.exportScripts()
	fishCraftingTableSell.generateFishCraftingSellRecipes()
	furnitureScripts.exportTrades()
