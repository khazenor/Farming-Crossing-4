from src import buildingMaterialsScripts
from src import marketShopGen
from src import furnitureCutting
from src import fishCraftingTableSell
from src import flowers
from src import gemCraftingTableSell
from src import jessDecoShop
from src import customVillagers
from src import musicDiscs
from src import clothesVillagerSell
from src import hatVillagerSell
from src import foodProfessionTrades

if __name__ == "__main__":
	foodProfessionTrades.genFoodProfessionTrades()
	hatVillagerSell.genHatVillagerTrades()
	clothesVillagerSell.genClotheVillagerTrades()
	musicDiscs.deployMusicDiscs()
	customVillagers.deployFunctions()
	jessDecoShop.genNonWanderingTrades()
	gemCraftingTableSell.genGemCraftingTableSell()
	flowers.generateDuplicationRecipes()
	fishCraftingTableSell.generateFishCraftingSellRecipes()
	furnitureCutting.genFurnitureCuttingSupport()
	marketShopGen.generateMarketShops()
	buildingMaterialsScripts.exportScripts()
