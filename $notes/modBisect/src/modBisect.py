from src import dependencies
from src import config
import json
import os

disabledStr = '.disabled'
def modBisect(excludeModIdList=[]):
	allModDict = dependencies.getDependenciesWithConfigs()
	json.dump(allModDict, open('modsInfo.json', 'w'), indent=2)

	enableMods(allModDict)

	ignoreMods = getIgnoreMods(excludeModIdList, allModDict)
	pass
	for modId in ignoreMods:
		del allModDict[modId]

	test(allModDict, allModDict)

def getIgnoreMods(excludeModIdList, modDependencies):
	ignoreMods = {}
	for modId in excludeModIdList:
		parents = modsWithParents(modId, modDependencies)
		for parent in parents:
			addModWithDependencies(ignoreMods, modDependencies, parent)
	return ignoreMods
def test(allConsideredModDict, allModDict):
	if hasMultipleToggleableMod(allConsideredModDict):
		# test first half
		firstHalfModDict, modsToDisable = splitMods(allConsideredModDict, allModDict)
		disableMods(allConsideredModDict)
		enableMods(firstHalfModDict)
		print(f"Testing: {list(firstHalfModDict.keys())}")
		firstHalfGood = askIfFeatureIsWorking()

		if firstHalfGood:
			# test second half
			secondHalfModDict = modsWithDependencies(modsToDisable.keys(), allConsideredModDict)
			test(secondHalfModDict, allModDict)
		else:
			# test first half again
			test(firstHalfModDict, allModDict)

def askIfFeatureIsWorking():
	response = input("Is the feature working?").lower().strip()
	return response == 'y' or response == 'yes'

def disableMods(modDict):
	for modId in modDict:
		modDir = os.path.join(config.modFolder, modDict[modId][dependencies.modFilenameKey])
		modDirNoDisable = modDir.replace(disabledStr, "")
		if os.path.exists(modDir) and disabledStr not in modDir:
			os.rename(modDir, modDir+disabledStr)
		elif os.path.exists(modDirNoDisable) and disabledStr not in modDirNoDisable:
			os.rename(modDirNoDisable, modDir)
		else:
			pass

def enableMods(modDict):
	for modId in modDict:
		modDir = os.path.join(config.modFolder, modDict[modId][dependencies.modFilenameKey])
		if os.path.exists(modDir) or os.path.exists(modDir+disabledStr):
			if os.path.exists(modDir):
				srcDir = modDir
			else:
				srcDir = modDir+disabledStr
			os.rename(srcDir, modDir.replace(disabledStr, ""))

def splitMods(allConsideredModDict, allModDict):
	modsToTest = {}
	modsToDisable = {}
	for modId in allConsideredModDict:
		addModWithDependencies(modsToTest, allModDict, modId)
		if len(modsToTest.keys()) >= len(allConsideredModDict) / 2:
			break

	for modId in allConsideredModDict:
		if modId not in modsToTest:
			modsToDisable[modId] = allConsideredModDict[modId]
	return modsToTest, modsToDisable

def modsWithDependencies(modIds, allModsDict):
	modsDict = {}
	for modId in modIds:
		addModWithDependencies(modsDict, allModsDict, modId)
	return modsDict

def modsWithParents(modIdCheck, allModsDict):
	parentIds = []
	for modId in allModsDict:
		dependenciesForMod = allModsDict[modId][dependencies.dependenciesKey]
		if modIdCheck in dependenciesForMod:
			parentIds.append(modId)
	if len(parentIds) == 0:
		return [modIdCheck] + parentIds
	else:
		grandParents = []
		for parentId in parentIds:
			grandParents = modsWithParents(parentId, allModsDict)
		return [modIdCheck] + parentIds + grandParents

def addModWithDependencies(testingDict, allModsDict, modId):
	if modId not in testingDict:
		testingDict[modId] = allModsDict[modId]

		childs = []
		for dependencyModId in allModsDict[modId][dependencies.dependenciesKey]:
			if dependencyModId not in testingDict and dependencyModId in allModsDict:
				testingDict[dependencyModId] = allModsDict[dependencyModId]
				childs.append(dependencyModId)
		for child in childs:
			addModWithDependencies(testingDict, allModsDict, child)

def hasMultipleToggleableMod(modsDict):
	modId = list(modsDict.keys())[0]
	modsWithDependenciesDict = modsWithDependencies([modId], modsDict)
	return modsWithDependenciesDict.keys() != modsDict.keys()
