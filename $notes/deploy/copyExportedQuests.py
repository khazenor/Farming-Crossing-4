import config
import util
import os

def copyServerQuests():
	print('copying quest back to config source')
	savedQuestPath = config.savedQuestFolder(config.configSrc())
	savedQuestFolders = os.listdir(savedQuestPath)
	savedQuestFolders.sort()
	latestSavedName = savedQuestFolders[len(savedQuestFolders) - 1]
	questSrc = os.path.join(savedQuestPath, latestSavedName)
	questDest = config.questFolder(config.configSrc())
	util.copyFolder(questSrc, questDest)


if __name__ == '__main__':
	copyServerQuests()
	input('press enter to conginue...')