from lib import stringCleaning
def collectionNotification(collectedText, objName, total):
	outStr = f"scoreboard players add @p {objName} 1\n"
	outStr += tellRaw([
		textJson(f'{collectedText} ('),
		scoreJson(objName),
		textJson(f'/{total})'),
	])
	return outStr

def tellRaw(texts):
	outStr = 'tellraw @p ["",'
	for i, text in enumerate(texts):
		outStr += text
		if i < len(texts) - 1:
			outStr += ','
	outStr += ']\n'
	return outStr

def scoreJson(objective):
	return f'{{"score":{{"name":"@p","objective":"{objective}"}}}}'

def initScoreBoard(title):
	objName = stringCleaning.cleanedNameStr(title)
	outStr = f'scoreboard objectives add {objName} dummy {textJson(title)}\n'
	outStr += f'scoreboard players set @p {objName} 0\n'
	return outStr

def textJson(text):
	return f'{{"text":"{text}"}}'
