import json
import os
from src import const

def writeLootFile(parentId, childId, name, lootEntries, rarity="COMMON"):
	dataFolder = os.path.join(const.data(), 'lootbags', 'recipes', parentId)
	if not os.path.exists(dataFolder):
		os.makedirs(dataFolder)
	json.dump(
		defaultOutput(name,entries(lootEntries), rarity),
		open(os.path.join(dataFolder, childId+'.json'), 'w'),
		indent=2
	)

def defaultOutput(name, lootEntries, rarity="COMMON"):
	return {
		"type": "lootbags:loot",
		"name": name,
		"rarity": rarity,
		"output": {
			"rolls": 1,
			"entries": lootEntries
		}
	}

def entries(entryList):
	outList = []
	for entry in entryList:
		outList.append({"stack": entry, "weight": 1})
	return outList

