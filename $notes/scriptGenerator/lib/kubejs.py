

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

# FILE CONTENT
def wanderingTradeFileContent(tradeStr):
	return f"MoreJSEvents.wandererTrades((event) => {{\n{tradeStr}\n}})"

def recipeFileContent(content):
	return f"ServerEvents.recipes(event => {{\n{content}\n}})"

def tooltipFileContent(content):
	return f"ItemEvents.tooltip(event => {{\n{content}\n}})"

def villagerTradesContent(content):
	return f"MoreJSEvents.villagerTrades((event) => {{\n{content}\n}})"

def tagsContent(content):
	return f"ServerEvents.tags('item', event => {{\n{content}\n}})"


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