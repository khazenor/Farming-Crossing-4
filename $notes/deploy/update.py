import shutil
import os
from pathlib import Path

updateLocation = "C:\\Users\\skim2\\Dropbox\\Share\\FarmingCrossing4\\install"

def copyFolder(src, dest):
	destParent = Path(dest).parents[0]
	copyFolderRecur(src, destParent)
	removeExtraFilesRecur(src, dest)

def copyFolderRecur(src, destFolder):
	if os.path.exists(src) and os.path.exists(destFolder):
		srcName = Path(src).name
		if os.path.isfile(src):
			existingDestFilePath = os.path.join(destFolder, srcName)
			if Path(existingDestFilePath).is_file():
				if os.stat(src).st_mtime - os.stat(existingDestFilePath).st_mtime > 0:
					shutil.copy2(src, destFolder)
			else:
				shutil.copy2(src, destFolder)
		else:
			newDestFolder = os.path.join(destFolder, srcName)
			if not os.path.exists(newDestFolder):
				os.makedirs(newDestFolder)
			itemsToCopy = os.listdir(src)
			for itemToCopy in itemsToCopy:
				copyFolderRecur(os.path.join(src, itemToCopy), newDestFolder)
			pass

def removeExtraFilesRecur(src, dest):
	if Path(dest).is_dir() and Path(src).is_dir():
		for item in os.listdir(dest):
			destItemPath = os.path.join(dest, item)
			srcItemPath = os.path.join(src, item)
			if Path(destItemPath).is_file():
				if not os.path.exists(srcItemPath):
					os.remove(destItemPath)
			elif Path(destItemPath).is_dir():
				removeExtraFilesRecur(srcItemPath, destItemPath)

if __name__ == "__main__":
	for folder in os.listdir(updateLocation):
		print(f"Updating the {folder} folder ...")
		srcFolder = os.path.join(updateLocation, folder)
		copyFolder(srcFolder, folder)

