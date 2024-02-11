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
		y = 0
		rewardsIncreaseRate = questline[collectionQuestsInput.increaseRateKey]
		for questGroup in questline[collectionQuestsInput.questGroupsKey]:
			x = -1
			initY = y

			taskIds = questGroup[collectionQuestsInput.tasksKey]
			questGroupName = questGroup[collectionQuestsInput.nameKey]
			dependencyId = questGroup[collectionQuestsInput.dependencyIdKey]
			subQuestDependencies = []
			for taskId in taskIds:
				questId = ftbQuest.randomId(taskId)
				subQuestDependencies.append(questId)
				x += 1
				if x > numQuestPerRow:
					x = 0
					y += 1
				questsContent += ftbQuest.collectionQuestContent(
					questId,
					taskId,
					f"function {questFunctions.functionParentName}:{stringCleaning.cleanedNameStr(questGroupName)}",
					dependencyId,
					x=x,
					y=y
				)

			questIds += subQuestDependencies

			# create sub quest
			if collectionQuestsInput.additionalRewardsKey in questGroup:
				additionalRewards = questGroup[collectionQuestsInput.additionalRewardsKey]
			else:
				additionalRewards = []
			subQuestY = (y + initY) / 2
			questsContent += ftbQuest.collectionSubQuestContent(
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
				questline[collectionQuestsInput.nameKey],
				questsContent,
				orderIndex=questlineIdx + collectionQuestsInput.startingQuestlineIdx,
				questGroupId=collectionQuestsInput.questlineGroupId
			)
		)
	return questIdsByFilename

def subQuestRewardNum(numTasks, increaseRate):
	return int(numTasks * (1 + increaseRate * numTasks))