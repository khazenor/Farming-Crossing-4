from list import collectionQuests as cql
from lib import kubejs
from src import const

villagerLevels = [
	[],
	cql.hatFlat + cql.hatTall,
	cql.hatMedium + cql.hatHeadTopper,
	cql.hatFaceCovering + cql.hatDisguise,
	cql.hatAnimal + cql.hatAroundHead,
	cql.hatEyewear + cql.hatAnimatedDetail + cql.hatAccesories
]

profession = 'spacecatcustomprofessions:hat_seller'
hatPrice = 8

def genHatVillagerTrades():
	tradeContent = ''
	for level, villagerItems in enumerate(villagerLevels):
		for villagerItem in villagerItems:
			tradeContent += kubejs.villagerTradeWithDefaultSales(
				villagerItem,
				1,
				const.priceItem,
				hatPrice,
				profession,
				level,
				False
			)
	kubejs.writeServerFile(
		kubejs.villagerTradesContent(
			tradeContent
		),
		'hat_villager_trades'
	)
	kubejs.writeClientFile(
		kubejs.tooltipFileContent(
			kubejs.eventAdd(
				cql.allHats,
				[f'Regular Price: {hatPrice} tickets']
			)
		),
		'hat_villager_price_tooltips'
	)
