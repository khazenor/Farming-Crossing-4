from src import util, paths, log
import os

clientConfigsToCopy = [
	"bettertitlescreen-client.toml"
]

foldersToDeleteExtrasFrom = [
	"ftbquests"
]

personalConfigs = [
	'-client.toml',
	'config\\defaultoptions\\options.txt',
	'config\\defaultoptions\\optionsof.txt',
	'config\\defaultoptions\\servers.dat',
	'config\\brb.toml',
	'config\\xaerominimap.txt',
	'config\\xaeropatreon.txt',
	'config\\xaeroworldmap.txt'
]

configFolderName = 'config'

def deployConfigs():
	log.log('## Deploying Configs ...')
	deployInsts = [paths.modsSrc] + paths.otherInsts + paths.servers
	for deployInst in deployInsts:
		deleteExtraConfigs(deployInst)
		util.copyFolderRecur(
			os.path.join(paths.configSrc, configFolderName),
			deployInst,
			allowSubStrList=clientConfigsToCopy,
			denySubStrList=personalConfigs
		)

def deleteExtraConfigs(deployInst):
	for deleteFolder in foldersToDeleteExtrasFrom:
		util.removeExtraFilesRecur(
			os.path.join(paths.configSrc, configFolderName, deleteFolder),
			os.path.join(deployInst, configFolderName, deleteFolder)
		)

