import os
from src import const

def writeClientFile(content, filename):
	with open(os.path.join(const.clientScripts(), f'{filename}.js'), 'w') as clientFile:
		clientFile.write(content)

def writeServerFile(content, filename):
	with(open(os.path.join(const.serverScripts(), f'{filename}.js'), "w")) as f:
		f.write(content)

def tradeStr(output, payment, paymentNum, level=1):
	return f"  event.addTrade({level}, ['{paymentNum}x {payment}'], '{output}')\n"

def shapeless(output, ingedients, outputNum = 1):
	outStr = "  event.shapeless(\n"
	outStr += f"    Item.of('{output}', {outputNum}),\n"
	outStr += f"    {arrayToString(ingedients)})\n"
	return outStr

def removeRecipeOutput(output):
	return f"  event.remove({{ output: '{output}' }})\n"

def eventAdd(items, tooltips):
	return f"  event.add(\n{arrayToString(items, indent=4)},\n{arrayToString(tooltips, indent=4)})\n"

def eventAddItemToList(item, itemList):
	return f"  event.add(\n\t\t'{item}',\n{arrayToString(itemList, indent=4)})\n"

def eventStonecutting(outputMat, inputMat):
	return f"  event.stonecutting('{outputMat}', '{inputMat}')\n"

def eventAddSimple(item1, item2):
	return f"  event.add('{item1}', '{item2}')\n"

def woodcutting(tagInput, outputItem, outputNumber):
	outstr = ""
	outstr += "  event.custom({\n"
	outstr += '    type: "corail_woodcutter:woodcutting",\n'
	outstr += f'    ingredient:{{"tag":"{tagInput}"}},\n'
	outstr += f'    result:"{outputItem}",\n'
	outstr += f'    count:{outputNumber}\n'
	outstr += '  })\n'
	return outstr

def villagerTradeWithDefaultSales(
	villagerItem,
	villagerNum,
	playerItem,
	playerNum,
	profession,
	level,
	decreasePlayerNum=False,
	increaseVillagerNum=False
):
	# number of price: price ratio
	priceRatio = {
		8: 1,
		2: 0.75,
		1: 0.5
	}
	tradeContent = ''
	for priceOccur in priceRatio:
		for i in range(priceOccur):
			if decreasePlayerNum:
				updatedVillagerNum = villagerNum
				updatedPlayerNum = int(playerNum * priceRatio[priceOccur])
			elif increaseVillagerNum:
				updatedVillagerNum = int(villagerNum * (1 / priceRatio[priceOccur]))
				updatedPlayerNum = playerNum
			else:
				updatedVillagerNum = villagerNum
				updatedPlayerNum = playerNum

			tradeContent += villagerTradeWithDefaults(
				villagerItem,
				updatedVillagerNum,
				playerItem,
				updatedPlayerNum,
				profession,
				level
			)
	return tradeContent

def villagerTradeWithDefaults(villagerItem, villagerNum, playerItem, playerNum, profession, level):
	tradeExperience = 25
	priceMultiplier = 0.035
	return villagerTradeWCallback(
		f'{playerNum}x {playerItem}',
		f'{villagerNum}x {villagerItem}',
		profession,
		level,
		tradeExperience,
		priceMultiplier
	)

def villagerTradeWCallback(item, paymentItem, profession, level, experince, priceMultiplier):
	outStr = f"  event.addCustomTrade('{profession}', {level}, (offer, entity, random) => {{\n"
	outStr += f"    offer.setFirstInput('{item}')\n"
	# outStr += "    offer.setSecondInput(item)"
	outStr += f"    offer.setOutput('{paymentItem}')\n"
	# outStr += "    offer.setMaxUses(number)"
	outStr += f"    offer.setVillagerExperience({experince})\n"
	outStr += f"    offer.setPriceMultiplier({priceMultiplier})\n"
	outStr += "  })\n"
	return outStr

def removeTradesForProfession(profession):
	outStr = ""
	for i in range(5):
		outStr += f'  event.removeModdedTrades(["{profession}"], {i + 1})\n'
		outStr += f'  event.removeVanillaTrades(["{profession}"], {i + 1})\n'
	return outStr

def createSimple(objectId):
	return f'  event.create("{objectId}")\n'

def createMusicDisc(itemId, musicPath, musicLen, itemPath, displayName):
	outStr = ""
	outStr += f'  event.create("{itemId}", "music_disc")\n'
	outStr += f'    .song("{musicPath}", {musicLen})\n'
	outStr += f'    .analogOutput(1)\n'
	outStr += f'    .texture("{itemPath}")\n'
	outStr += f'    .displayName("{displayName}")\n'
	outStr += f'    .maxStackSize(64)\n'
	return outStr
# FILE CONTENT
def wanderingTradeFileContent(tradeStr):
	return f"MoreJSEvents.wandererTrades((event) => {{\n{tradeStr}\n}})"

def recipeFileContent(content):
	return f"ServerEvents.recipes(event => {{\n{content}\n}})"

def tooltipFileContent(content):
	return f"ItemEvents.tooltip(event => {{\n{content}\n}})"

def villagerTradesContent(content):
	return f"MoreJSEvents.villagerTrades((event) => {{\n{content}\n}})"

def registryFileContent(registryType, content):
	return f"StartupEvents.registry('{registryType}', event => {{\n{content}}})"

def tagsContent(content, tagType='item'):
	return f"ServerEvents.tags('{tagType}', event => {{\n{content}\n}})"

def generateSimpleTags(itemIds, tag, filename):
	writeServerFile(
		tagsContent(
			eventAddItemToList(tag, itemIds)
		),
		filename
	)

# HELPERS

def arrayToString(array, indent=-1):
	indentStr = ''
	if indent > -1:
		for i in range(indent):
			indentStr += ' '

	outStr = f"{indentStr}["
	if indent > -1:
		outStr += "\n"
	for i in range(len(array)):
		elem = array[i]
		if indent > -1:
			outStr += f"{indentStr}  "
		outStr += f"'{elem}'"
		if i < len(array) - 1:
			outStr += ', '
		if indent > -1:
			outStr += '\n'
	outStr += f'{indentStr}]'
	return outStr

def multipleArray(elem, num):
	outArr = []
	for i in range(num):
		outArr.append(elem)
	return outArr