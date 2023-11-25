from src import mods
from src import configFolder
from src import simpleFolders
from src import globalPacks
from src import kubejs
from src import resourcepacks
from src import shaderpacks

def deployModpack():
	mods.deployMods()
	configFolder.deployConfigs()
	simpleFolders.deploySimpleFolders()
	globalPacks.deployGlobalPacks()
	kubejs.deployKubejs()
	resourcepacks.deployResourcepacks()
	shaderpacks.deployShaderpacks()

if __name__ == '__main__':
	deployModpack()
