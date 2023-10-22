from input import woodFurnitureInput
import os

def genFurnitureCuttingInputs():
	furnitureCuttingInputFolderDir = os.path.join("input", "furniture")
	woodTypeContents = findWoodTypeFurniture()
	for woodTypeContent in woodTypeContents:
		with open(os.path.join(furnitureCuttingInputFolderDir, woodTypeContent[woodFurnitureInput.fileKey]), "w") as f:
			f.write(woodTypeContent[woodFurnitureInput.contentKey])
def findWoodTypeFurniture():
	woodTypeContents = woodFurnitureInput.woodTypesInfo.copy()

	for itemId in woodFurnitureInput.possibleWoodFurniture:
		insertIdx = woodTypeContentIdx(itemId, woodTypeContents)
		if insertIdx >= 0:
			woodTypeContents[insertIdx][woodFurnitureInput.contentKey] += f'\n{itemId}'
	return woodTypeContents

def woodTypeContentIdx(itemId, woodTypeContents):
	for i, woodTypeContent in enumerate(woodTypeContents):
		if isItemOfWoodType(itemId, woodTypeContent):
			return i
	return -1

def isItemOfWoodType(itemId, woodTypeContent):
	for translation in woodTypeContent[woodFurnitureInput.translationKey]:
		if translation in itemId:
			return True

if __name__ == "__main__":
	genFurnitureCuttingInputs()