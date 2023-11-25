import config
import os
from src import util
simpleFolders = [
	'defaultconfigs',
	'scripts'
]

def deploySimpleFolders():
	deployInsts = [ config.modsSrc ] + config.otherInsts + config.servers
	for simpleFolder in simpleFolders:
		print(f'## Deploying {simpleFolder} ...')
		util.simpleDeploy(
			config.configSrc,
			deployInsts,
			simpleFolder
		)
