from list import cosmeticArmors
from list import collectionQuests
from lib import kubejs
from lib import util

profession = 'spacecatcustomprofessions:clothes_seller'

itemsForSell = [
	[],
	cosmeticArmors.accessories,
	cosmeticArmors.helmet,
	cosmeticArmors.chestplate,
	cosmeticArmors.leggings,
	cosmeticArmors.boots
]

hatPrice = 5
defaultPrice = 4
priceReference = {
	5: cosmeticArmors.armor1,
	7: cosmeticArmors.armor2,
	9: cosmeticArmors.armor3,
	15: cosmeticArmors.armor5,
	20: cosmeticArmors.armor6
}


def genClotheVillagerTrades():
	tradeContent = ''
	itemsByPrice = {}
	for level, villagerItems in enumerate(itemsForSell):
		for villagerItem in villagerItems:
			price = priceLookup(villagerItem)
			util.addToDictList(itemsByPrice, price, villagerItem)
			tradeContent += kubejs.villagerTradeWithDefaultSales(
				villagerItem,
				1,
				'kubejs:miles_ticket',
				price,
				profession,
				level,
				False
			)
	kubejs.writeServerFile(
		kubejs.villagerTradesContent(tradeContent),
		'clothes_villager_trades'
	)
	generatePriceTooltips(itemsByPrice)
	removeCraftingRecipes()

def generatePriceTooltips(itemsByPrice):
	tooltipContent = ''
	for price in itemsByPrice:
		pluralString = 's' if price > 1 else ''
		tooltipContent += kubejs.eventAdd(
			itemsByPrice[price],
			["Can be purchased from Elna\\'s fashion shop", f'Regular Price: {price} ticket{pluralString}']
		)
	kubejs.writeClientFile(
		kubejs.tooltipFileContent(
			tooltipContent
		),
		'clothing_pricing_tooltips'
	)

def removeCraftingRecipes():
	removeContent = ""
	for itemId in collectionQuests.allCosm:
		removeContent += kubejs.removeRecipeOutput(itemId)
	kubejs.writeServerFile(
		kubejs.recipeFileContent(
			removeContent
		),
		'clothes_recipe_removal'
	)

def priceLookup(itemId):
	if itemId in collectionQuests.allHats:
		return hatPrice
	for price in priceReference:
		if itemId in priceReference[price]:
			return price
	return defaultPrice
