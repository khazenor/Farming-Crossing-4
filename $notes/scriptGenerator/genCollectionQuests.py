from quests import questFunctions
from quests import collectionQuests
from quests import achievementQuestGen
from quests import collectionTooltips
from quests import floraTags

if __name__ == "__main__":
	questFunctions.genQuestFunctions()
	questIdsByFilename = collectionQuests.genQuestLines()
	achievementQuestGen.genMileageRewardProgramQuests(questIdsByFilename)
	collectionTooltips.genCollectionTooltips()
	floraTags.genFloraTags()
