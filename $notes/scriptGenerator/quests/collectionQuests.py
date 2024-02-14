from lib import ftbQuest
from lib import stringCleaning
from input import collectionQuestsInput
from quests import questFunctions

numQuestPerRow = 5

def genQuestLines():
	questIdsByFilename = {}
	for questlineIdx, questline in enumerate(collectionQuestsInput.questlines):
		questsContent = ''
		questIds = []
		questLineName = questline[collectionQuestsInput.nameKey]
		y = 0
		for questGroup in questline[collectionQuestsInput.questGroupsKey]:
			x = -1
			initY = y

			taskIds = questGroup[collectionQuestsInput.tasksKey]
			questGroupName = questGroup[collectionQuestsInput.nameKey]
			dependencyId = questGroup[collectionQuestsInput.dependencyIdKey]
			subQuestDependencies = []
			for taskId in taskIds:

				x += 1
				if x > numQuestPerRow:
					x = 0
					y += 1
				questType = questline[collectionQuestsInput.typeKey]
				commandName = stringCleaning.cleanedNameStr(f'{questLineName} {questGroupName}')
				command = f"function {questFunctions.functionParentName}:{commandName}"
				if questType == collectionQuestsInput.itemQuestTypeConst:
					questId = ftbQuest.randomId(taskId)
					questsContent += ftbQuest.collectionQuestContent(
						questId,
						taskId,
						command,
						dependencyId,
						x=x,
						y=y
					)
				else: # questType == collectionQuestsInput.observationQuestTypeConst
					icon = taskId[collectionQuestsInput.iconKey]
					name = taskId[collectionQuestsInput.nameKey]
					observe = taskId[collectionQuestsInput.observeKey]
					questId = ftbQuest.randomId(observe)
					questsContent += ftbQuest.observationQuestContent(
						questId,
						icon,
						name,
						observe,
						command,
						dependencyId,
						x=x,
						y=y
					)
				subQuestDependencies.append(questId)

			questIds += subQuestDependencies

			# create sub quest
			if collectionQuestsInput.additionalRewardsKey in questGroup:
				additionalRewards = questGroup[collectionQuestsInput.additionalRewardsKey]
			else:
				additionalRewards = []
			if collectionQuestsInput.increaseRateKey in questGroup:
				rewardsIncreaseRate = questGroup[collectionQuestsInput.increaseRateKey]
			else:
				rewardsIncreaseRate = questline[collectionQuestsInput.increaseRateKey]
			subQuestY = (y + initY) / 2
			questId = ftbQuest.randomId(f'{questLineName}{questGroupName}')
			questsContent += ftbQuest.collectionSubQuestContent(
				questId,
				subQuestDependencies,
				questGroup[collectionQuestsInput.nameKey],
				questGroup[collectionQuestsInput.iconKey],
				subQuestRewardNum(len(subQuestDependencies), rewardsIncreaseRate),
				additionalRewards=additionalRewards,
				x=-1,
				y=subQuestY
			)
			y += 1.5

		questFilename = questline[collectionQuestsInput.filenameKey]
		questIdsByFilename[questFilename] = questIds
		ftbQuest.writeQuestChapter(
			questFilename,
			ftbQuest.questFileContent(
				questline[collectionQuestsInput.iconKey],
				questline[collectionQuestsInput.filenameKey],
				questLineName,
				questsContent,
				orderIndex=questlineIdx,
				questGroupId=collectionQuestsInput.questlineGroupId
			)
		)
	return questIdsByFilename

def subQuestRewardNum(numTasks, increaseRate):
	return int(numTasks * (1 + increaseRate * numTasks))