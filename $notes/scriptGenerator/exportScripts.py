from src import buildingMaterialsScripts
from src import marketShopGen
from src import furnitureCutting
from src import foodVillagerSales
from src import fishCraftingTableSell
from src import flowers
from src import gemCraftingTableSell
from src import nonWanderingTrades
from src import customVillagers
from src import musicDiscs
from src import clothesVillagerSell

if __name__ == "__main__":
	clothesVillagerSell.genClotheVillagerTrades()
	musicDiscs.deployMusicDiscs()
	customVillagers.deployFunctions()
	nonWanderingTrades.genNonWanderingTrades()
	gemCraftingTableSell.genGemCraftingTableSell()
	flowers.generateDuplicationRecipes()
	fishCraftingTableSell.generateFishCraftingSellRecipes()
	foodVillagerSales.generateSales()
	furnitureCutting.generateFurnitureCuttingRecipes()
	marketShopGen.generateMarketShops()
	buildingMaterialsScripts.exportScripts()
