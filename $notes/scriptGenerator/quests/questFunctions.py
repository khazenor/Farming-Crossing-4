from input import collectionQuestsInput
from lib import mcfunction
from lib import commands
from lib import stringCleaning

functionParentName = 'fc_collection'
def genQuestFunctions():
	initFunctionContent = ''
	mcfunction.clearFunctionFiles(functionParentName)

	for questline in collectionQuestsInput.questlines:
		totalCollectibles = 0
		for questGroup in questline[collectionQuestsInput.questGroupsKey]:
			subGroupName = questGroup[collectionQuestsInput.nameKey]
			totalSubCollectibles = len(questGroup[collectionQuestsInput.tasksKey])
			mcfunction.writeFunction(
				functionParentName,
				subGroupName,
				commands.collectionNotification(
					subGroupName,
					stringCleaning.cleanedNameStr(subGroupName),
					totalSubCollectibles
				)
			)
			initFunctionContent += commands.initScoreBoard(subGroupName)
			totalCollectibles += totalSubCollectibles

		questlineName = questline[collectionQuestsInput.nameKey]
		initFunctionContent += commands.initScoreBoard(questlineName)
		mcfunction.writeFunction(
			functionParentName,
			questlineName,
			commands.collectionNotification(
				questline[collectionQuestsInput.collectionNotificationKey],
				stringCleaning.cleanedNameStr(questlineName),
				totalCollectibles
			)
		)
		mcfunction.writeFunction(functionParentName, 'init_all_scores', initFunctionContent)
