import os
import shutil

def copyFolder(src, dest):
	if os.path.exists(src):
		if os.path.exists(dest):
			shutil.rmtree(dest)
		shutil.copytree(src, dest)

def subFolders(location, folderArray):
	paths = []
	for folder in folderArray:
		paths.append(os.path.join(location, folder))
	return paths
