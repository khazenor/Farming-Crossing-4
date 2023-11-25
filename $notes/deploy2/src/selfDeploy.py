import os
from src import paths
from src import util

srcFolderName = 'src'

def deploySelf():
	print('## Deploy Self ...')
	if paths.dropboxDeployScriptLoc != "":
		util.copyFolder(
			srcFolderName,
			paths.dropboxDeployScriptLoc
		)
