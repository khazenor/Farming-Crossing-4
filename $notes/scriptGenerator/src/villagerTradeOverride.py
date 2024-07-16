import os
from lib import kubejs
import json

# to update trades
# 1. install custom villager trades
# 2. in a world, run 'exportCVT'
# 3. locate the profession file generated
# 4. copy to input folder and modify trades
# 5. run this script
# 6. remove custom villager trades

def genVillagerTrades():
	professionFolder = os.path.join('input', 'professionOverrides')

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
	), 'villager_trade_overrides')