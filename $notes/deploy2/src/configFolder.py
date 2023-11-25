import config
from src import util
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
	print('## Deploying Configs ...')
	deployInsts = [ config.modsSrc ] + config.otherInsts + config.servers
	for deployInst in deployInsts:
		deleteExtraConfigs(deployInst)
		util.copyFolderRecur(
			os.path.join(config.configSrc, configFolderName),
			deployInst,
			denySubStrList=personalConfigs
		)

def deleteExtraConfigs(deployInst):
	for deleteFolder in foldersToDeleteExtrasFrom:
		util.removeExtraFilesRecur(
			os.path.join(config.configSrc, configFolderName, deleteFolder),
			os.path.join(deployInst, configFolderName, deleteFolder)
		)

