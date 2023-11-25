from src import util
import config
import os

resourcesNames = [
	"xali's Enchanted Books"
]

resourceFolderName = 'resourcepacks'

def deployResourcepacks():
	print('## Deploy Resourcepacks ... ')
	copyClients()
	copyServers()

def copyClients():
	print('# Updating clients')
	deployInsts = config.otherInsts + [config.configSrc]
	for deployInst in deployInsts:
		util.copyFolderRecur(
			os.path.join(config.modsSrc, resourceFolderName),
			deployInst
		)

def copyServers():
	print('# Updating servers')
	for deployInst in config.servers:
		util.copyFolderRecur(
			os.path.join(config.modsSrc, resourceFolderName),
			deployInst,
			denySubStrList=resourcesNames
		)