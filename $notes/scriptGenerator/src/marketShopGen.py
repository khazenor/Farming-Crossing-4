from lib import farmingForBlockheads
from lib import nbt
from lib import pythonHelpers
from input import marketShop
from src import const
import json
import os

numMeat = 8
meatPrice = 2
numSeed = 4
seedPrice = 32
numSapling = 2
saplingPrice = 32
flowerPrice = 32
spawnEggPrice = 64

def generateMarketShops():
	meatShop = generateMarketShop(
		marketShop.meats,
		numMeat,
		meatPrice,
		'meats',
		"Ethically Sourced Meats",
		"minecraft:rabbit",
	)
	meatShop = addEntries(meatShop, marketShop.more_meats, 'meats')
	json.dump(meatShop, open(os.path.join(const.farmingForBlockheads(), 'meats.json'), 'w'), indent=2)

	generateMarketShopAndWriteFile(
		marketShop.seeds,
		numSeed,
		seedPrice,
		'seed',
		"Seed Bank",
		"minecraft:wheat_seeds",
		os.path.join(const.farmingForBlockheads(), 'seeds.json')
	)

	generateMarketShopAndWriteFile(
		marketShop.saplings,
		numSeed,
		saplingPrice,
		'sapling',
		"The Nursery",
		"minecraft:oak_sapling",
		os.path.join(const.farmingForBlockheads(), 'saplings.json')
	)

	generateMarketShopAndWriteFile(
		marketShop.flowers,
		numSeed,
		flowerPrice,
		'flowers',
		"Flower Shop",
		"minecraft:poppy",
		os.path.join(const.farmingForBlockheads(), 'flowers.json')
	)

	generateMarketShopAndWriteFile(
		marketShop.spawn_eggs,
		1,
		spawnEggPrice,
		'spawneggs',
		"Spawn Eggs Shop",
		"alexsmobs:spawn_egg_anaconda",
		os.path.join(const.farmingForBlockheads(), 'spawn_eggs.json')
	)

	generateShopFromEnchantments(
		marketShop.enchantments,
		'enchantments',
		'Enchantment Book Store',
		'minecraft:enchanted_book',
		os.path.join(const.farmingForBlockheads(), 'enchantments.json')
	)

def generateMarketShop(items, itemCount, price, category, categoryName, categoryItem):
	entries = []
	for item in items:
		entries.append(farmingForBlockheads.entry(
			item,
			itemCount,
			const.priceItem,
			price,
			category
		))

	shop = farmingForBlockheads.categoryStore(
		entries,
		category,
		categoryName,
		categoryItem
	)
	return shop

def addEntries(shop, entries, category):
	outShop = shop
	for entry in entries:
		outShop['customEntries'].append(farmingForBlockheads.entry(
			entry[1],
			entry[0],
			const.priceItem,
			entry[2],
			category
		))
	return outShop


def generateMarketShopAndWriteFile(items, itemCount, price, category, categoryName, categoryItem, fileLocation):
	shop = generateMarketShop(items, itemCount, price, category, categoryName, categoryItem)
	json.dump(shop, open(fileLocation, 'w'), indent=2)


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

