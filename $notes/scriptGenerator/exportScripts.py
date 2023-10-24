from src import furnitureScripts
from src import buildingMaterialsScripts
from src import marketShopGen
from src import furnitureCutting
from src import foodVillagerSales
from src import fishCraftingTableSell
if __name__ == "__main__":
	fishCraftingTableSell.generateFishCraftingSellRecipes()
	foodVillagerSales.generateSales()
	furnitureCutting.generateFurnitureCuttingRecipes()
	marketShopGen.generateMarketShops()
	buildingMaterialsScripts.exportScripts()
	furnitureScripts.exportTrades()
