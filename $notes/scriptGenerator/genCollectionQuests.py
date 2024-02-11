from quests import questFunctions
from quests import collectionQuests
from quests import achievementQuestGen

if __name__ == "__main__":
	questFunctions.genQuestFunctions()
	questIdsByFilename = collectionQuests.genQuestLines()
	achievementQuestGen.genMileageRewardProgramQuests(questIdsByFilename)
