from src import const
import os
import json
from lib import stringCleaning

exportFolder = os.path.join(const.kubejs(), 'data', 'botanypots', 'recipes', 'farming_crossing', 'crop')

def writeSeedJson(seedId, cropId, blockId):
	filename = stringCleaning.cleanedNameStr(seedId)
	if not os.path.exists(exportFolder):
		os.makedirs(exportFolder)
	json.dump(
		defaultSeedDict(seedId, cropId, blockId),
		open(os.path.join(exportFolder, filename + ".json"), 'w'),
		indent=2
	)

def defaultSeedDict(seedId, cropId, blockId):
	return {
		"bookshelf:load_conditions": [
			{
				"type": "bookshelf:item_exists",
				"values": [
					seedId
				]
			}
		],
		"type": "botanypots:crop",
		"seed": {
			"item": seedId
		},
		"categories": [
			"dirt",
			"farmland"
		],
		"growthTicks": 20000,
		"display": {
			"type": "botanypots:aging",
			"block": blockId
		},
		"drops": [
			{
				"chance": 1.00,
				"output": {
					"item": cropId
				}
			},
			{
				"chance": 0.01,
				"output": {
					"item": seedId
				}
			}
		]
	}
