import util
import config

def copyServerQuests():
	print('copying server quest to main config instance...')
	src = config.questFolder(config.questUpdateServer())
	dest = config.questFolder(config.configSrc())
	util.copyFolder(src, dest)

if __name__ == '__main__':
	copyServerQuests()
	input('press enter to continue')
