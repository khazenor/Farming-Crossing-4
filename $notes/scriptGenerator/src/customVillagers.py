from lib import mcfunction
import os
nameKey = 'name'
textureKey = 'texture'

villagersWithTrades = [
	{nameKey: 'Andre', textureKey: 'dog'},
	{nameKey: 'Laly', textureKey: 'merekat'},
	{nameKey: 'Pamela', textureKey: 'rabbit'},
	{nameKey: 'Ren', textureKey: 'woodpecker'},
	{nameKey: 'Sam', textureKey: 'eagle'},
	{nameKey: 'Yukkie', textureKey: 'bat'}
]

otherVillagers = [
	{nameKey: 'Jess', textureKey: 'beaver'},
	{nameKey: 'Bernina', textureKey: 'hedgehog'},
	{nameKey: 'Elna', textureKey: 'hedgehog2'}
]

def offerFolder():
	return os.path.join('input', 'customVillagersOffers')

def deployFunctions():
	writeSummonCommands()
	writeHighlightCommands()
	writeTradeUpdateCommands()

def writeSummonCommands():
	for villager in villagersWithTrades:
		name = villager[nameKey]
		mcfunction.writeFunction(
			'fc_villagers',
			name,
			summonNpcCommand(
				villager[textureKey],
				name,
				offerStr=readOffer(name)
			)
		)
	for villager in otherVillagers:
		name = villager[nameKey]
		mcfunction.writeFunction(
			'fc_villagers',
			name,
			summonNpcCommand(
				villager[textureKey],
				name
			)
		)

def summonNpcCommand(texture, name, offerStr=""):
	outStr = ""
	outStr += 'summon ssls_npc_maker_mod:npc ~ ~ ~ {'
	outStr += f'texture_name: "{texture}",'
	outStr += f'CustomName: "{{\\"text\\":\\"{name}\\"}}"'
	if offerStr != "":
		outStr += f',Offers: '
		outStr += offerStr
		outStr += ',VillagerData: { profession: "minecraft:nitwit", level: 5, type: "minecraft:plains" }'
	outStr += "}"
	return outStr

def writeHighlightCommands():
	for villager in villagersWithTrades + otherVillagers:
		name = villager[nameKey]
		mcfunction.writeFunction('fc_villagers', f'{name}_highlight', highlightVillagerCommand(name))

def writeTradeUpdateCommands():
	for villager in villagersWithTrades:
		name = villager[nameKey]
		mcfunction.writeFunction(
			'fc_villagers',
			f'{name}_update_trades',
			highlightVillagerCommand(name) + "\n" +
			tradeUpdateCommand(name)
		)


def highlightVillagerCommand(name, time=30):
	outStr = f'execute at @p if entity {nearestVillagerSelector(name)} '
	outStr += f'run effect give {nearestVillagerSelector(name)} minecraft:glowing {time} 1 true'
	return outStr

def tradeUpdateCommand(name):
	return f'data modify entity {nearestVillagerSelector(name)} Offers set value {readOffer(name)}'

def nearestVillagerSelector(name):
	return f'@e[type=ssls_npc_maker_mod:npc, name={name}, sort=nearest, limit=1]'
def readOffer(name):
	offerStr = ""
	with open(os.path.join(offerFolder(), f"{name}.txt"), 'r') as f:
		fileContent = f.read()
		for line in fileContent.split("\n"):
			offerStr += line.strip()
	return offerStr


