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
from src import botanyPotSeedSupport
from src import tips
from src import clothesAndDecoLootBags
from src import letsDoVillagerTradeToTickets
from src import villagerTradeOverride

if __name__ == "__main__":
	villagerTradeOverride.genVillagerTrades()
	letsDoVillagerTradeToTickets.genVillagerTrades()
	clothesAndDecoLootBags.genClothesAndDecoLootBagSupport()
	tips.genTips()
	botanyPotSeedSupport.genBotanySeedSupport()
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
