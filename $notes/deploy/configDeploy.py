import config
import util
import os
import shutil

def deployConfigs():
	updateConfigs(config.configFolders())
	deleteExtraDefaultConfigs()

def configUpdateLocations():
	updatingLocs = config.otherInsts()
	updatingLocs += config.servers()
	updatingLocs.append(config.modsSrc())
	return updatingLocs

def updateConfigs(subfolders):
	updatingLocs = configUpdateLocations()

	for location in updatingLocs:
		print(f'updating configs to {location}')
		srcFolders = util.subFolders(
			config.configSrc(),
			subfolders
		)
		destFolders = util.subFolders(location, subfolders)
		for i in range(len(srcFolders)):
			print(f'  - copying {subfolders[i]} ...')
			srcFolder = srcFolders[i]
			destFolder = destFolders[i]
			util.copyFolder(srcFolder, destFolder)


def deleteExtraDefaultConfigs():
	updatingLocs = configUpdateLocations()
	for location in updatingLocs:
		print(f'deleting extra configs from {location}')
		for relativePath in config.deleteRelativeUrls():
			delPath = os.path.join(location, relativePath)
			if os.path.exists(delPath):
				os.remove(delPath)
		for configFolder in config.deleteConfigFolders():
			delPath = os.path.join(location, configFolder)
			if os.path.exists(delPath):
				shutil.rmtree(delPath)

		# remove client configs
		configFolder = config.configFolder(location)
		for configFilename in os.listdir(configFolder):
			if '-client.toml' in configFilename:
				os.remove(os.path.join(configFolder, configFilename))

if __name__ == '__main__':
	updateConfigs(config.reloadWhileRunningFolders())
	input('press enter to exit...')
