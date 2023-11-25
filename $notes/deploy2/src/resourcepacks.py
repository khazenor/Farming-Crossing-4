from src import util, paths
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
	print(' # Updating clients')
	deployInsts = paths.otherInsts + [paths.configSrc]
	for deployInst in deployInsts:
		util.copyFolderRecur(
			os.path.join(paths.modsSrc, resourceFolderName),
			deployInst
		)

def copyServers():
	print(' # Updating servers')
	for deployInst in paths.servers:
		util.copyFolderRecur(
			os.path.join(paths.modsSrc, resourceFolderName),
			deployInst,
			denySubStrList=resourcesNames
		)