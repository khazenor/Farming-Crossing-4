from src import util
import config
import os

globalPacksFolderName = 'global_packs'
requiredDataFolderName = 'required_data'
requiredResourceFolderName = 'required_resources'

def deployGlobalPacks():
	print('## Deploying Global Packs')
	copyDatapacks()
	copyResources()

def copyDatapacks():
	print('# Copying Global Datapacks')
	deployInsts = [config.modsSrc] + config.otherInsts + config.servers
	util.simpleDeploy(
		config.configSrc,
		deployInsts,
		os.path.join(globalPacksFolderName, requiredDataFolderName)
	)

def copyResources():
	print('# Copying Global Resources')
	deployInsts = [config.modsSrc] + config.otherInsts
	util.simpleDeploy(
		config.configSrc,
		deployInsts,
		os.path.join(globalPacksFolderName, requiredResourceFolderName)
	)