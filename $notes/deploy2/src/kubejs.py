from src import util
import config
import os

kubejsFolderName = 'kubejs'
clientFolders = [
	'assets',
	'client_scripts'
]
def deployKubejs():
	print('## Deploying Kubejs ...')
	clientInsts = [ config.modsSrc ] + config.otherInsts
	for folder in os.listdir(os.path.join(config.configSrc, kubejsFolderName)):
		print(f'# Copying {folder}')
		if folder in clientFolders:
			deployInsts = clientInsts
		else:
			deployInsts = clientInsts + config.servers
		util.simpleDeploy(
			config.configSrc,
			deployInsts,
			os.path.join(kubejsFolderName, folder)
		)