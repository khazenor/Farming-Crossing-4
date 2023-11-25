from src import util
import config
import os
import shutil

clientSideModNames = [
	'badpackets',
	'brb',
	'Controlling',
	"DrawersTooltip",
	'entityculling',
	'extreamesoundmuffler',
	'farsight',
	'NekosEnchantedBooks',
	'wthit',
	'oculus',
	'rubidium',
	'wthitharvestability',
	'RubidiumExtra',
	'light-overlay',
	'MoreCosmetics',
	'guicompass',
	'betterf3',
	'betterf3plus',
	'BetterAdvancements',
	'controllable',
	'entity_model_features_forge_1.20.1',
	'entity_texture_features_forge_1.20.1',
	'InventoryProfilesNext',
	'citresewn',
	'tagtooltips',
	'World Stripper',
	'embeddium',
	'tagtooltips',
	'XaeroPlus',
	'XaerosWorldMap',
	'Xaeros_Minimap'
]

modsFolder = 'mods'
modlistFile = 'modlist.txt'
serverModlistFile = 'serverModlist.txt'

def deployMods():
	print('## Deploying Mods...')
	deployToClients()
	deployToServers()
	writeModlists()

def deployToClients():
	clientInsts = config.otherInsts + [config.configSrc]
	for clientInst in clientInsts:
		print(f' - {clientInst}')
		util.copyFolder(
			modsSrc(),
			instMods(clientInst)
		)

def deployToServers():
	for serverInst in config.servers:
		print(f' - server: {serverInst}')
		deleteExtraMods(serverInst)
		copyOverMods(serverInst)

def deleteExtraMods(serverInst):
	serverModsCache = serverMods()
	serverModsFolder = instMods(serverInst)
	for mod in os.listdir(serverModsFolder):
		if mod not in serverModsCache:
			os.remove(os.path.join(
				serverModsFolder, mod
			))

def copyOverMods(serverInst):
	for mod in serverMods():
		shutil.copy2(
			os.path.join(modsSrc(), mod),
			instMods(serverInst)
		)

def serverMods():
	mods = []
	for mod in modsSrcMods():
		if not util.strContainsStrFromSubStrList(mod, clientSideModNames):
			mods.append(mod)
	return mods

def writeModlists():
	writeMods(modlistFile, modsSrcMods())

	exportServerMods = os.listdir(instMods(config.servers[0]))
	writeMods(serverModlistFile, exportServerMods)

def writeMods(filename, mods):
	with open(os.path.join(config.configSrc, filename), "w") as f:
		for mod in mods:
			f.write(f"{mod}\n")

def modsSrcMods():
	return os.listdir(modsSrc())
def modsSrc():
	return instMods(config.modsSrc)

def instMods(inst):
	return os.path.join(inst, modsFolder)
