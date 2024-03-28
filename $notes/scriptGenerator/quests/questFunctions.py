from input import collectionQuestsInput
from lib import mcfunction
from lib import commands
from lib import stringCleaning
from lib import util
import os

functionParentName = 'fc_collection'
initScoreFilename = 'init_all_scores'
def genQuestFunctions():
	initFunctionContent = ''
	prevInitScoreFiles = getPrevInitScoreFiles()
	mcfunction.clearFunctionFiles(functionParentName)

	checkScoreContent = ''

	for questline in collectionQuestsInput.questlines:
		totalCollectibles = totalTasksForQuestline(questline)
		questlineObjName = stringCleaning.cleanedNameStr(questline[collectionQuestsInput.nameKey])
		questlineName = questline[collectionQuestsInput.nameKey]

		checkScoreContent += commands.collectionNotification(
			questlineName,
			questlineObjName,
			totalCollectibles
		)
		for questGroup in questline[collectionQuestsInput.questGroupsKey]:
			subGroupName = questGroup[collectionQuestsInput.nameKey]
			totalSubCollectibles = len(questGroup[collectionQuestsInput.tasksKey])
			subGroupNameCleaned = stringCleaning.cleanedNameStr(subGroupName)
			fullCollectionNotification = (
				questline[collectionQuestsInput.collectionNotificationKey] + " " +
				questlineName
			)

			subGroupObjName = f'{questlineObjName}_{subGroupNameCleaned}'
			groupFunctionContent = (
				commands.collectionTally(questlineObjName) +
				commands.collectionNotification(
					fullCollectionNotification,
					questlineObjName,
					totalCollectibles
				)
			)
			mcfunction.writeFunction(
				functionParentName,
				questlineObjName,
				groupFunctionContent
			)

			subGroupFunctionContent = (
				commands.collectionTally(subGroupObjName) +
				commands.collectionNotification(
					subGroupName,
					subGroupObjName,
					totalSubCollectibles
				) +
				commands.tellRaw([])
			)
			mcfunction.writeFunction(
				functionParentName,
				subGroupObjName,
				subGroupFunctionContent
			)
			initFunctionContent += commands.initScoreBoard(subGroupObjName)

		questlineName = questline[collectionQuestsInput.nameKey]
		initFunctionContent += commands.initScoreBoard(questlineName)
		writeInitScoreFunctions(initFunctionContent, prevInitScoreFiles)
		mcfunction.writeFunction(functionParentName, 'check_collection_scores', checkScoreContent)

def totalTasksForQuestline(questline):
	totalNumTasks = 0
	for questGroup in questline[collectionQuestsInput.questGroupsKey]:
		totalNumTasks += len(questGroup[collectionQuestsInput.tasksKey])
	return totalNumTasks

def getPrevInitScoreFiles():
	fileIdx = 0
	initFileContents = []
	while os.path.exists(initScoreFileUrl(fileIdx)):
		with open(initScoreFileUrl(fileIdx), 'r') as initScoreFile:
			initFileContents.append(initScoreFile.read())
		fileIdx += 1
	return initFileContents

def initScoreFileUrl(fileIdx):
	return mcfunction.functionFileUrl(
		functionParentName,
		f"{initScoreFilename}_{fileIdx}"
	)

def writeInitScoreFunctions(initFunctionContent, prevInitScoreFiles):
	fileContents = {}
	for functionLine in initFunctionContent.split('\n'):
		updateFileContents(fileContents, functionLine, prevInitScoreFiles)
	for fileUrl in fileContents:
		with open(fileUrl, 'w') as f:
			f.write(fileContents[fileUrl])

def updateFileContents(fileContents, functionLine, prevInitScoreFiles):
	if len(functionLine) > 0:
		for i, prevInitScoreFile in enumerate(prevInitScoreFiles):
			if functionLine in prevInitScoreFile:
				util.addToDictString(fileContents, initScoreFileUrl(i), functionLine)
				return
		util.addToDictString(fileContents, initScoreFileUrl(len(prevInitScoreFiles)), functionLine)
