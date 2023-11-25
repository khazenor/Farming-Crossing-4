from src import util, paths
import os

kubejsFolderName = 'kubejs'
clientFolders = [
	'assets',
	'client_scripts'
]
def deployKubejs():
	print('## Deploying Kubejs ...')
	clientInsts = [paths.modsSrc] + paths.otherInsts
	for folder in os.listdir(os.path.join(paths.configSrc, kubejsFolderName)):
		print(f' # Copying {folder}')
		if folder in clientFolders:
			deployInsts = clientInsts
		else:
			deployInsts = clientInsts + paths.servers
		util.simpleDeploy(
			paths.configSrc,
			deployInsts,
			os.path.join(kubejsFolderName, folder)
		)