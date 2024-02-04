from src import mods
from src import configFolder
from src import simpleFolders
from src import globalPacks
from src import kubejs
from src import resourcepacks
from src import shaderpacks
from src import selfDeploy
from src import customFilesFolder
from src import curseforgeInstanceFile

def deployModpack():
	curseforgeInstanceFile.deployCurseforgeFile()
	mods.deployMods()
	configFolder.deployConfigs()
	simpleFolders.deploySimpleFolders()
	globalPacks.deployGlobalPacks()
	kubejs.deployKubejs()
	resourcepacks.deployResourcepacks()
	shaderpacks.deployShaderpacks()
	selfDeploy.deploySelf()
	customFilesFolder.deployCustomFilesFolder()
