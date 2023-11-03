import math
import os

def hundredsOfItems():
	numQuests = 239
	outputFileDir = os.path.join("output", "ftbQuestCoords.txt")
	numHundredsInRow = math.ceil(math.sqrt(numQuests/100))

	with open(outputFileDir, "w") as f:
		for i in range(numQuests):
			hundredIdx = math.floor(i / 100)
			hundredX = hundredIdx % numHundredsInRow * 11
			hundredY = math.floor(hundredIdx / numHundredsInRow) * 11

			indX = i % 10
			indY = math.floor((i % 100) / 10)

			finalX = hundredX + indX
			finalY = hundredY + indY

			f.write(f'x: {finalX}.0d\n')
			f.write(f'y: {finalY}.0d\n')

def verticalColumns():
	numQuests = 25
	columnHeight = 5
	outputFileDir = os.path.join("output", "ftbQuestCoords.txt")

	with open(outputFileDir, "w") as f:
		for i in range(numQuests):
			indX = math.floor(i / columnHeight)
			indY = i % columnHeight

			f.write(f'x: {indX}.0d\n')
			f.write(f'y: {indY}.0d\n')

def groupsOfSixes():
	numQuests = 133
	rowWidth = 6
	doGrouping = False
	outputFileDir = os.path.join("output", "ftbQuestCoords.txt")

	with open(outputFileDir, "w") as f:
		for i in range(numQuests):
			groupIdx = math.floor(i / (rowWidth * rowWidth))
			indX = float(i % rowWidth)
			indY = float(math.floor(i / rowWidth))

			if doGrouping:
				indY = float(indY + groupIdx * .5)

			f.write(f'x: {indX}d\n')
			f.write(f'y: {indY}d\n')

if __name__ == "__main__":
	groupsOfSixes()
