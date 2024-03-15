from lib import sslNpc
from input import fcVillagersInput as vil
from lib import mcfunction
from lib import util
from src import const
from lib import kubejs
from lib import stringCleaning

def deployFunctions():
	for villager in vil.villagers:
		writeSummonCommand(villager)
		writeHighlightCommand(villager)
		if hasTrades(villager):
			writeHighlightAndUpdateTradeCommand(villager)
			writeTradeTooltips(villager)

def writeSummonCommand(villager):
	name = villager[vil.nameKey]
	mcfunction.writeFunction(
		'fc_villagers',
		name,
		sslNpc.summonNpcCommand(
			villager[vil.textureKey],
			name,
			getVillagerOffers(villager),
			hasTrades(villager)
		)
	)

def writeHighlightCommand(villager):
	name = villager[vil.nameKey]
	mcfunction.writeFunction(
		'fc_villagers',
		f'{name}_highlight',
		sslNpc.highlightNpcCommand(name)
	)

def writeHighlightAndUpdateTradeCommand(villager):
	name = villager[vil.nameKey]
	mcfunction.writeFunction(
		'fc_villagers',
		f'{name}_highlight_and_update_trades',
		sslNpc.highlightNpcCommand(name) +
		sslNpc.updateNpcCommand(name, getVillagerOffers(villager))
	)

def writeTradeTooltips(villager):
	buyFromVillager = []
	sellToVillager = []
	getFromVillager = []
	for offer in getVillagerOffers(villager):
		if offer[sslNpc.playerGiveKey] == const.priceItem:
			buyFromVillager.append(offer[sslNpc.villagerItemKey])
		elif offer[sslNpc.villagerItemKey] == const.priceItem:
			sellToVillager.append(offer[sslNpc.playerGiveKey])
		else:
			getFromVillager.append(offer[sslNpc.villagerItemKey])

	name = villager[vil.nameKey]
	tooltipContent = ""
	if len(buyFromVillager) > 0:
		tooltipContent += kubejs.eventAdd(
			buyFromVillager,
			[f'You can buy this item from {name}']
		)
	if len(sellToVillager) > 0:
		tooltipContent += kubejs.eventAdd(
			sellToVillager,
			[f'You can sell this item to {name}']
		)
	if len(getFromVillager) > 0:
		tooltipContent += kubejs.eventAdd(
			getFromVillager,
			[f'You can get this item from {name}']
		)
	if len(tooltipContent) > 0:
		kubejs.writeClientFile(
			kubejs.tooltipFileContent(tooltipContent),
			f'fc_villager_trades_tooltips_{stringCleaning.cleanedNameStr(name)}'
		)


def getVillagerOffers(villager):
	if hasTrades(villager):
		offers = []
		for smartTrade in villager[vil.tradesKey]:
			villagerGiveItems = util.defaultDict(
				smartTrade,
				vil.villagerGiveItemsKey,
				[const.priceItem]
			)
			playerGiveItems = util.defaultDict(
				smartTrade,
				vil.playerGiveItemsKey,
				[const.priceItem]
			)
			for villagerGiveItem in villagerGiveItems:
				for playerGiveItem in playerGiveItems:
					offers.append({
						sslNpc.villagerItemKey: villagerGiveItem,
						sslNpc.villagerQtyKey: util.defaultDict(
							smartTrade,
							vil.villagerGiveNumKey,
							1
						),
						sslNpc.playerGiveKey: playerGiveItem,
						sslNpc.playerQtyKey: util.defaultDict(
							smartTrade,
							vil.playerGiveNumKey,
							1
						)
					})
		return offers
	else:
		return []

def hasTrades(villager):
	return vil.tradesKey in villager
