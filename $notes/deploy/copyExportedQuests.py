import config
import util
import os
from pathlib import Path
import shutil

def copyServerQuests():
	print('copying quest back to config source')
	savedQuestPath = config.savedQuestFolder(config.configSrc())
	savedQuestFolders = os.listdir(savedQuestPath)
	savedQuestFolders.sort()
	latestSavedName = savedQuestFolders[len(savedQuestFolders) - 1]
	questSrc = os.path.join(savedQuestPath, latestSavedName)
	questDest = config.questFolder(config.configSrc())
	for item in os.listdir(questSrc):
		itemPath = os.path.join(questSrc, item)
		if Path(itemPath).is_dir():
			util.copyFolder(itemPath, os.path.join(questDest, item))
		else:
			shutil.copy2(itemPath, questDest)

if __name__ == '__main__':
	copyServerQuests()
	input('press enter to conginue...')