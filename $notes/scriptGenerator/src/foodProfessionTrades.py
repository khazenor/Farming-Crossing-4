from input import foodCustomerPricingInput as fcInput
from list import collectionQuests as cqlist
from lib import util
from lib import kubejs
from src import const

professionHeader = "spacecatcustomprofessions:"
professionFooter = "_customer"

priceKey = 'price'
playerNumberKey = 'playerNumber'
itemKey = 'item'

professionTradeItems = {
	'bakery': cqlist.foodOven + cqlist.foodSmallCookingPot + cqlist.foodBakerStation,
	'beach': cqlist.foodMiniFridge + cqlist.foodTikiBar + cqlist.foodTeaKettle + cqlist.foodCauldron,
	'candlelight': cqlist.foodCookingPot + cqlist.foodCookingPan + cqlist.foodCraftingTable,
	'drink': cqlist.foodGrapevinePot + cqlist.foodAgingBarrel + cqlist.foodBrewingCopper + cqlist.foodBrewingWood,
	'farmers_delight': cqlist.foodDelightful + cqlist.foodAlex + cqlist.foodAquaculture + cqlist.foodFarmersDelight
}

def genFoodProfessionTrades():
	tradesByProfessions = getTradesByProfessions()
	writeProfessionScripts(tradesByProfessions)
	writeTooltips(tradesByProfessions)

def writeTooltips(tradesByProfessions):
	tooltipContent = ''
	for profession in tradesByProfessions:
		professionName = profession.replace(professionHeader, '').replace('_', ' ')
		for trade in tradesByProfessions[profession]:
			playerNum = trade[playerNumberKey]
			if playerNum > 1:
				numStr = f"{playerNum} of "
			else:
				numStr = ''

			price = trade[priceKey]

			if price > 1:
				plural = 's'
			else:
				plural = ''

			tooltipContent += kubejs.eventAddItemToList(
				trade[itemKey],
				[
					f'A {professionName} villager regularly',
					f'buys {numStr}this meal for {price} ticket{plural}',
				]
			)
	kubejs.writeClientFile(
		kubejs.tooltipFileContent(
			tooltipContent
		),
		'customer_villager_professions_trades_tooltips'
	)


def writeProfessionScripts(tradesByProfessions):
	tradeContent = ""
	for profession in tradesByProfessions:
		trades = tradesByProfessions[profession]
		for i, trade in enumerate(trades):
			level = int(i * 5 / len(trades)) + 1
			tradeContent += kubejs.villagerTradeWithDefaultSales(
				const.priceItem,
				trade[priceKey],
				trade[itemKey],
				trade[playerNumberKey],
				profession,
				level,
				increaseVillagerNum=True
			)
	kubejs.writeServerFile(
		kubejs.villagerTradesContent(
			tradeContent
		),
		'customer_villager_professions_trades'
	)
def getTradesByProfessions():
	tradesByProfession = {}
	for professionName in professionTradeItems:
		profession = professionHeader + professionName + professionFooter
		for tradeItem in professionTradeItems[professionName]:
			price, playerNumber = priceAndNumberToSell(tradeItem)
			if price > 0:
				util.addToDictList(
					tradesByProfession,
					profession,
					{
						itemKey: tradeItem,
						priceKey: price,
						playerNumberKey: playerNumber
					}
				)
	for professionName in tradesByProfession:
		tradesByProfession[professionName] = sorted(
			tradesByProfession[professionName],
			key=lambda trade: trade[priceKey]
		)
	return tradesByProfession

def priceAndNumberToSell(itemId):
	pricing = fcInput.pricing
	for price in pricing:
		for itemDict in pricing[price]:
			if itemDict[fcInput.itemKey] == itemId:
				if price == 1:
					return price * 2, util.defaultDict(itemDict, fcInput.countKey, 1) * 2
				else:
					return price, util.defaultDict(itemDict, fcInput.countKey, 1)
	return -1, -1
