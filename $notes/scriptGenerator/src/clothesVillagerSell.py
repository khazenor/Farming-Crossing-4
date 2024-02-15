from list import cosmeticArmors
from list import collectionQuests
from lib import kubejs

profession = 'spacecatcustomprofessions:clothes_seller'

itemsForSell = [
	[],
	collectionQuests.allHats,
	cosmeticArmors.boots,
	cosmeticArmors.helmet,
	cosmeticArmors.leggings,
	cosmeticArmors.chestplate
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
	for level, villagerItems in enumerate(itemsForSell):
		for villagerItem in villagerItems:
			tradeContent += kubejs.villagerTradeWithDefaults(
				villagerItem,
				1,
				'kubejs:miles_ticket',
				priceLookup(villagerItem),
				profession,
				level
			)
	kubejs.writeServerFile(
		kubejs.villagerTradesContent(tradeContent),
		'clothes_villager_trades'
	)

def priceLookup(itemId):
	if itemId in collectionQuests.allHats:
		return hatPrice
	for price in priceReference:
		if itemId in priceReference[price]:
			return price
	return defaultPrice
