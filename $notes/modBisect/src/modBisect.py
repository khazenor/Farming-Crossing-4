from src import fileGroupings
from src import config
import json
import os

disabledStr = '.disabled'
fileGroupingCacheFilename = 'fileGroupings.json'
def modBisect(excludeModIdList=[]):
	allFileGroups = fileGroupings.getFileGroupings()

	goodGroups = fileGroupsWithSubstrings(excludeModIdList, allFileGroups)
	mysteryGroups = listSubtract(allFileGroups, goodGroups)
	test(goodGroups, mysteryGroups)
	enableGroups(allFileGroups)
	input("press enter to continue... ")

def test(goodGroups, mysteryGroups):
	if len(mysteryGroups) > 1:
		group1, group2 = splitList(mysteryGroups)
		# test group 1
		print(f"Disable({len(group2)}): {group2}")
		disableGroups(group2)
		print(f"Good({len(goodGroups)}): {goodGroups}")
		enableGroups(goodGroups)
		print(f"Testing({len(group1)}): {group1}")
		enableGroups(group1)

		firstHalfGood = askIfFeatureIsWorking()

		if firstHalfGood:
			goodGroups += group1
			test(goodGroups, group2)
		else:
			test(goodGroups, group1)
	else:
		print(f"Found Problem Mod Group: {mysteryGroups[0]}")

def askIfFeatureIsWorking():
	response = input("Is the feature working? ").lower().strip()
	return 'y' in response

def disableGroups(fileGroups):
	for fileGroup in fileGroups:
		disableMods(fileGroup)

def enableGroups(filegroups):
	for fileGroup in filegroups:
		enableMods(fileGroup)

def disableMods(filenames):
	for filename in filenames:
		modDir = os.path.join(config.modFolder, filename)
		modDirNoDisable = modDir.replace(disabledStr, "")
		if os.path.exists(modDir) and disabledStr not in modDir:
			os.rename(modDir, modDir+disabledStr)
		elif os.path.exists(modDirNoDisable) and disabledStr not in modDirNoDisable:
			os.rename(modDirNoDisable, modDir)
		else:
			pass

def enableMods(filenames):
	for filename in filenames:
		modDir = os.path.join(config.modFolder, filename)
		if os.path.exists(modDir) or os.path.exists(modDir+disabledStr):
			if os.path.exists(modDir):
				srcDir = modDir
			else:
				srcDir = modDir+disabledStr
			os.rename(srcDir, modDir.replace(disabledStr, ""))

def splitList(targetList):
	return targetList[len(targetList)//2:], targetList[:len(targetList)//2]

def listSubtract(mainList, subList):
	differenceList = []
	for elm in mainList:
		if elm not in subList:
			differenceList.append(elm)
	return differenceList
def fileGroupsWithSubstrings(modSubstrings, allFileGroups):
	fileGroups = []
	for modSubstring in modSubstrings:
		for fileGroup in allFileGroups:
			for filename in fileGroup:
				if modSubstring.lower() in filename.lower():
					fileGroups.append(fileGroup)
					break
	return fileGroups
