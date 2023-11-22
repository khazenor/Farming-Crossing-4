import os
import config
import util
import configDeploy
import shutil

def deploy():
	print('UPDATING MODS:')
	updateMods()
	updateModList()
	# enableMods()
	print('UPDATING CONFIGS')
	configDeploy.deployConfigs()


def updateMods():
	updatingLocs = config.otherInsts()
	updatingLocs += config.servers()
	updatingLocs.append(config.configSrc())

	for location in updatingLocs:
		print(f'copying mods to {location}')
		util.copyFolder(config.mods(config.modsSrc()), config.mods(location))
		addExtraMods(location)

	for server in config.servers():
		print(f'deleting client side mods from {server}')
		serverModDir = config.mods(server)
		serverMods = os.listdir(serverModDir)
		for serverMod in serverMods:
			modname = serverMod.split('-')[0]
			if util.strContainsStrFromSubStrList(modname, config.clientSideModNames()):
				os.remove(os.path.join(config.mods(server), serverMod))

		print(f'deleting client side folders from {server}')
		for clientFolder in config.clientSideFolders():
			shutil.rmtree(os.path.join(server, clientFolder))

def addExtraMods(location):
	addModFolder = config.modsAdd(location)
	if os.path.exists(addModFolder):
		for addMod in os.listdir(addModFolder):
			modPath = os.path.join(addModFolder, addMod)
			shutil.copy(modPath, config.mods(location))

def enableMods():
	updatingLocs = [config.configSrc()]

	for location in updatingLocs:
		for modName in config.enableMods():
			print(f'enabling mods for {location}')
			srcDir = os.path.join(config.mods(location), modName)
			destDir = os.path.join(config.mods(location), modName.replace('.disabled', ''))
			os.rename(srcDir, destDir)

def updateModList():
	srcModList = os.listdir(config.mods(config.configSrc()))
	with open(os.path.join(config.configSrc(), 'modlist.txt'), 'w') as f:
		for file in srcModList:
			f.write(file + '\n')

if __name__ == "__main__":
	deploy()
	input("press enter to exit.")
