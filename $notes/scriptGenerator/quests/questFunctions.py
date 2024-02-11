from input import collectionQuestsInput
from lib import mcfunction
from lib import commands
from lib import stringCleaning

functionParentName = 'fc_collection'
def genQuestFunctions():
	initFunctionContent = ''
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
			subGroupObjName = stringCleaning.cleanedNameStr(subGroupName)
			fullCollectionNotification = (
				questline[collectionQuestsInput.collectionNotificationKey] + " " +
				questlineName
			)

			mcfunction.writeFunction(
				functionParentName,
				subGroupName,
				commands.collectionNotification(
					fullCollectionNotification,
					questlineObjName,
					totalCollectibles
				) +
				commands.collectionNotification(
					subGroupName,
					subGroupObjName,
					totalSubCollectibles
				) +
				commands.tellRaw([])
			)
			initFunctionContent += commands.initScoreBoard(subGroupName)
			totalCollectibles += totalSubCollectibles

		questlineName = questline[collectionQuestsInput.nameKey]
		initFunctionContent += commands.initScoreBoard(questlineName)
		mcfunction.writeFunction(functionParentName, 'init_all_scores', initFunctionContent)
		mcfunction.writeFunction(functionParentName, 'check_collection_scores', checkScoreContent)

def totalTasksForQuestline(questline):
	totalNumTasks = 0
	for questGroup in questline[collectionQuestsInput.questGroupsKey]:
		totalNumTasks += len(questGroup[collectionQuestsInput.tasksKey])
	return totalNumTasks