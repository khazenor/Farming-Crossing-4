from src import dependencies
import json

def fileGroupings():
	groupsWithSubsets = fileGroupingsWithSubSets()

	while haveSubSet(groupsWithSubsets):
		subset = findSubSetIdx(groupsWithSubsets)
		groupsWithSubsets.remove(subset)

	return groupsWithSubsets

def haveSubSet(filenameGroups):
	return findSubSetIdx(filenameGroups) != -1

def findSubSetIdx(filenameGroups):
	for filenameGroup1 in filenameGroups:
		for filenameGroup2 in filenameGroups:
			if isSubSet(filenameGroup1, filenameGroup2):
				return filenameGroup2
	return -1

def isSubSet(targetList, checkList):
	if targetList == checkList:
		return False
	for checkMod in checkList:
		if checkMod not in targetList:
			return False
	return True

def fileGroupingsWithSubSets():
	allModDict = dependencies.getDependenciesWithConfigs()
	json.dump(allModDict, open('modsInfo.json', 'w'), indent=2)

	modNames = []
	for modId in allModDict:
		modNames.append(modWithDependencies(modId, allModDict))

	filenames = []
	for modNameGroup in modNames:
		filenameGroup = []
		for modName in modNameGroup:
			filenameGroup.append(allModDict[modName][dependencies.modFilenameKey])
		filenames.append(filenameGroup)
	return filenames
def modWithDependencies(modId, allModsDict):
	if modId in allModsDict:
		modDepends = allModsDict[modId][dependencies.dependenciesKey]
		if len(modDepends) == 0:
			return [modId]
		else:
			otherDepends = []
			for dependId in modDepends:
				otherDepends += modWithDependencies(dependId, allModsDict)
			return [modId] + otherDepends
	else:
		return []
