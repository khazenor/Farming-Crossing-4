from input import collectionQuestsInput as cqIn
from lib import lootBags
from lib import stringCleaning
from lib import farmingForBlockheads
from src import const

regularPriceKey = 'regularPriceKey'
lootBagId = "lootbags:loot_bag"
categoryId = 'clothes_and_deco_kits'
categoryName = 'Clothes and Decoration Kits'

collectionPrices = {
	'common_decorations': 8,
	'rare_decorations': 64,
	'clothing_collection': 8,
	'hat_collection': 8
}
rarity = "UNCOMMON"

def genClothesAndDecoLootBagSupport():
	marketEntries = []
	printTestCalcPrice() # for testing pricing
	for questline in cqIn.questlines:
		if questline[cqIn.filenameKey] in collectionPrices:
			for questGroup in questline[cqIn.questGroupsKey]:
				writeLootBagFile(questGroup, questline)
				marketEntries.append(marketEntry(questGroup, questline))
	farmingForBlockheads.writeCategoryStoreWithEntries(
		categoryId,
		categoryName,
		"moa_decor_holidays:olladeoro",
		marketEntries
	)

def writeLootBagFile(questGroup, questline):
	lootName = getLootName(questGroup, questline)
	lootBags.writeLootFile(
		parentId(questline),
		childId(questGroup),
		lootName,
		questGroup[cqIn.tasksKey],
		rarity
	)

def marketEntry(questGroup, questline):
	price = lootBagPrice(questGroup, questline)
	return farmingForBlockheads.entryNBT(
		lootBagId,
		1,
		const.priceItem,
		price,
		categoryId,
		{
			"Color": 13882323,
			"Loot": lootBagEntryId(questGroup, questline),
			"Name": getLootName(questGroup, questline),
			"Type": rarity
		}
	)
def lootBagPrice(questGroup, questline):
	lootSize = len(questGroup[cqIn.tasksKey])
	basePrice = collectionPrices[questline[cqIn.filenameKey]]
	return calcPrice(lootSize, basePrice)

def calcPrice(lootSize, basePrice):
	if lootSize <= 4:
		return int(1.5 * basePrice)
	if lootSize <= 8:
		return basePrice
	if lootSize <= 12:
		return int(basePrice * .8)
	if lootSize <= 20:
		return int(basePrice * .6)
	return int(basePrice / 2)

def printTestCalcPrice():
	size = 4
	while size < 40:
		print('size:', size)
		print('basePrice:', 64)
		print('price:', calcPrice(size, 64))
		print()
		size += 8
	size = 4
	while size < 40:
		print('size:', size)
		print('basePrice:', 8)
		print('price:', calcPrice(size, 8))
		print()
		size += 8

def lootBagEntryId(questGroup, questline):
	return f"lootbags:{parentId(questline)}/{childId(questGroup)}"

def getLootName(questGroup, questline):
	subCat = questGroup[cqIn.nameKey].replace(' Completion', '')
	mainCat = questline[cqIn.nameKey]
	return f"{subCat} {mainCat} Kit"
def parentId(questline):
	return questline[cqIn.filenameKey]

def childId(questGroup):
	return stringCleaning.cleanedNameStr(questGroup[cqIn.nameKey])