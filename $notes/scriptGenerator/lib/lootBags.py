def defaultOutput(name, entries, rarity="COMMON"):
	return {
		"type": "lootbags:loot",
		"name": name,
		"rarity": rarity,
		"output": {
			"rolls": 1,
			"entries": entries
		}
	}

def entries(entryList):
	outList = []
	for entry in entryList:
		outList.append({"stack": entry, "weight": 1})
	return outList

