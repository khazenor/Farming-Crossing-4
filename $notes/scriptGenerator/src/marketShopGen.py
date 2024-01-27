from lib import farmingForBlockheads
from lib import nbt
from lib import pythonHelpers
from input import marketShop
from src import const
import json
import os

def generateMarketShops():
	farmingForBlockheads.genCategoryStores(marketShop.categories)
	generateShopFromEnchantments(
		marketShop.enchantments,
		'enchantments',
		'Enchantment Book Store',
		'minecraft:enchanted_book',
		os.path.join(const.farmingForBlockheads(), 'enchantments.json')
	)

def generateShopFromEnchantments(enchantments, category, categoryName, categoryItem, fileLocation):
	entries = []
	for enchantment in enchantments:
		maxLvPrice = enchantments[enchantment]["maxLvCost"]
		maxLevel = enchantments[enchantment]["maxLv"]
		for i in range(maxLevel):
			level = i + 1
			displayName = enchantmentDisplayName(enchantment)
			if maxLevel > 1:
				displayName += f" {level}"
			nbtTag = pythonHelpers.mergeDicts(
				nbt.enchantment(enchantment, level),
				nbt.nametag(displayName)
			)
			entries.append(farmingForBlockheads.entryNBT(
				"minecraft:enchanted_book",
				1,
				const.priceItem,
				enchantmentPrice(maxLvPrice, level, maxLevel),
				category,
				nbtTag
			))

	shop = farmingForBlockheads.categoryStore(
		entries,
		category,
		categoryName,
		categoryItem
	)

	json.dump(shop, open(fileLocation, 'w'), indent=2)

def enchantmentDisplayName(enchantment):
	outStr = enchantment.split(":")[1]
	outStr = outStr.replace("_", " ")
	outStr = outStr.title()
	return outStr

def enchantmentPrice(base, lv, maxLv):
	if lv == maxLv:
		return base
	else:
		return int(float(enchantmentPrice(base, lv + 1, maxLv))/2)

