import os
from lib import kubejs
import json
from src import const
from input import foodCustomerPricingInput as fprice
from lib import util

def getPrice(item):
	for price in fprice.pricing:
		for itemStack in fprice.pricing[price]:
			if itemStack[fprice.itemKey] == item:
				return price, util.defaultDict(itemStack, fprice.countKey, 1)
	return -1, -1
def genVillagerTrades():
	professionFolder = os.path.join('input','letsDoProfessions')

	villagerTradeContent = ""
	for professionFilename in os.listdir(professionFolder):
		professsionInfo = json.load(open(os.path.join(professionFolder, professionFilename), 'r'))
		profession = professsionInfo['profession']
		villagerTradeContent += kubejs.removeTradesForProfession(profession)
		for trade in professsionInfo['trades']:
			playerItem = trade["request"]["itemKey"]
			playerAmt = trade["request"]["amount"]
			villagerItem = trade["offer"]["itemKey"]
			villagerAmt = trade["offer"]["amount"]
			if playerItem == 'minecraft:emerald':
				playerItem = const.priceItem
			price, count = getPrice(villagerItem)
			if price > 0:
				playerAmt = int(1.5 * price)
				villagerAmt = count
			villagerTradeContent += kubejs.villagerTradeWCallback(
				f'{playerAmt}x {playerItem}',
				f'{villagerAmt}x {villagerItem}',
				profession,
				trade["tradeLevel"],
				trade["tradeExp"],
				trade["priceMultiplier"]
			)

	kubejs.writeServerFile(kubejs.villagerTradesContent(
		villagerTradeContent
	), 'lets_do_villager_trades_updates')