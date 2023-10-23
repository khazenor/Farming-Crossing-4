from lib import pythonHelpers

def bountyObjSimple(content, amount, unitWorth, weightMult):
	return bountyObjDetail(content, amount, amount, unitWorth, weightMult)

def bountyObjDetail(content, minNum, maxNum, unitWorth, weightMult):
	return {
		"type": "item",
		"content": content,
		"amount": {
			"min": minNum,
			"max": maxNum
		},
		"unitWorth": unitWorth,
		"weightMult": weightMult
	}

def fileContent(entries):
	contentKey = "content"
	fileContentDict = { contentKey: {} }

	for entry in entries:
		fileContentDict[contentKey][pythonHelpers.uuidStr()] = entry
	return fileContentDict
