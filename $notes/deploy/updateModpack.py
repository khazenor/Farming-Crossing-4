import os
import configDeploy
import shutil

folderWUpdateInfo = ""

updateFolders = ['mod', 'config', 'kubejs']

def deploy():
	print('UPDATING MODS')
	updateMods()
	print('UPDATING CONFIGS')
	configDeploy.deployConfigs()


def updateMods():
	for folder in updateFolders:
		copyFolder(folder, os.path.join(folderWUpdateInfo, folder))

def copyFolder(src, dest):
	if os.path.exists(dest):
		shutil.rmtree(dest)
	shutil.copytree(src, dest)

if __name__ == "__main__":
	deploy()
	input("press enter to exit.")
