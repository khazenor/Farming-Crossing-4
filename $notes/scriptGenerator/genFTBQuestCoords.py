import math
import os
if __name__ == "__main__":
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
