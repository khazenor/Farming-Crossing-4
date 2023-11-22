import os
import util

updateLocation = "C:\\Users\\skim2\\Dropbox\\Share\\FarmingCrossing4\\install"

keepExtraFiles = [
	'config'
]

if __name__ == "__main__":
	for folder in os.listdir(updateLocation):
		print(f"Updating the {folder} folder ...")
		srcFolder = os.path.join(updateLocation, folder)
		doKeepExtraFiles = folder in keepExtraFiles
		util.copyFolder(srcFolder, folder, doKeepExtraFiles)

