from lib import pythonHelpers

def ingredientList(ingIds):
	ingList = []
	for ingId in ingIds:
		ingList.append(kubejsToItemDict(ingId))
	return ingList

def kubejsToItemDict(kubejsStr):
	outDict = {}
	parseStr = kubejsStr
	numParse = 'x '
	tagParse = "#"
	if numParse in parseStr:
		count = int(parseStr.split(numParse)[0])
		parseStr = parseStr.split(numParse)[1]
		outDict = pythonHelpers.mergeDicts(outDict, {"count": count})

	if tagParse in parseStr:
		parseStr = parseStr.replace(tagParse, "")
		outDict = pythonHelpers.mergeDicts(outDict, {"tag": parseStr})
	else:
		outDict = pythonHelpers.mergeDicts(outDict, {"item": parseStr})

	return outDict

def fileNameFromKubejs(kubejsStr):
	kubejsStr = kubejsStr.replace("#", "")
	kubejsStr = kubejsStr.replace(" ", "_")
	kubejsStr = kubejsStr.replace(":", "_")
	return kubejsStr