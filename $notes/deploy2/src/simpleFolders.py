from src import util, paths

simpleFolders = [
	'defaultconfigs',
	'scripts'
]

def deploySimpleFolders():
	deployInsts = [paths.modsSrc] + paths.otherInsts + paths.servers
	for simpleFolder in simpleFolders:
		print(f'## Deploying {simpleFolder} ...')
		util.simpleDeploy(
			paths.configSrc,
			deployInsts,
			simpleFolder
		)
