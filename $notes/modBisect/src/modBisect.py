from src import fileGroupings
from src import config
import random
import os

disabledStr = '.disabled'
fileGroupingCacheFilename = 'fileGroupings.json'
def modBisect(excludeModIdList=[]):
	allFileGroups = fileGroupings.getFileGroupings()

	goodGroups = fileGroupsWithSubstrings(excludeModIdList, allFileGroups)
	mysteryGroups = listSubtract(allFileGroups, goodGroups)
	test(goodGroups, mysteryGroups)
	enableGroups(allFileGroups)

def test(goodGroups, mysteryGroups):
	if len(mysteryGroups) > 1:
		group1, group2 = splitListRandom(mysteryGroups)
		# test group 1
		print(f"Group1: ")
		disableAndEnableMods(group2, goodGroups, group1)

		firstHalfResponse = ''
		while firstHalfResponse != 'yes' and firstHalfResponse != 'no':
			firstHalfResponse = askIfFeatureIsWorking()
			if firstHalfResponse == 'quit':
				return
			if firstHalfResponse == 'reroll':
				test(goodGroups, mysteryGroups)

		if firstHalfResponse == 'yes':
			goodGroups += group1
			# test group 2
			print("Group2:")
			disableAndEnableMods(group1, goodGroups, group2)
			secondHalfResponse = ''
			while secondHalfResponse != 'yes' and secondHalfResponse != 'no':
				secondHalfResponse = askIfFeatureIsWorking()
				if secondHalfResponse == 'quit':
					return
				if secondHalfResponse == 'reroll':
					print('cannot resole on group 2')
					secondHalfResponse = askIfFeatureIsWorking()

			if secondHalfResponse == 'yes':
				print("Can't find issue, both split parts are issue free, trying again with different split")
				test(goodGroups, mysteryGroups)
			else:
				test(goodGroups, group2)
		else:
			test(goodGroups, group1)
	else:
		print(f"Found Problem Mod Group: {mysteryGroups[0]}")

def disableAndEnableMods(disable, good, testing):
	print(f"Disable({len(disable)}): {disable}")
	disableGroups(disable)
	print(f"Good({len(good)}): {good}")
	enableGroups(good)
	print(f"Testing({len(testing)}): {testing}")
	enableGroups(testing)
def askIfFeatureIsWorking():
	response = input("Is the feature working? ")
	if haveSubstrings(['stop', 'quit'], response):
		return 'quit'
	elif haveSubstrings(['reroll', 'roll'], response):
		return 'reroll'
	elif haveSubstrings(['yes'], response):
		return 'yes'
	elif haveSubstrings(['no'], response):
		return 'no'
	else:
		return 'error'

def haveSubstrings(subStrings, targetString):
	for subString in subStrings:
		if subString in targetString.lower().strip():
			return True
	return False

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

def splitListRandom(targetList):
	group1 = []
	group2 = []

	for group in targetList:
		if int(random.random() * 2):
			group1.append(group)
		else:
			group2.append(group)
	if len(group1) == 0 or len(group2) == 0:
		return splitListRandom(targetList)

	return group1, group2

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
