from src import util, paths
import os

globalPacksFolderName = 'global_packs'
requiredDataFolderName = 'required_data'
requiredResourceFolderName = 'required_resources'

def deployGlobalPacks():
	print('## Deploying Global Packs')
	copyDatapacks()
	copyResources()

def copyDatapacks():
	print(' # Copying Global Datapacks')
	deployInsts = [paths.modsSrc] + paths.otherInsts + paths.servers
	util.simpleDeploy(
		paths.configSrc,
		deployInsts,
		os.path.join(globalPacksFolderName, requiredDataFolderName)
	)

def copyResources():
	print(' # Copying Global Resources')
	deployInsts = [paths.modsSrc] + paths.otherInsts
	util.simpleDeploy(
		paths.configSrc,
		deployInsts,
		os.path.join(globalPacksFolderName, requiredResourceFolderName)
	)