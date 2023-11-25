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
			clientInst
		)

def deployToServers():
	for serverInst in config.servers:
		print(f' - server: {serverInst}')
		serverModsFolder = instMods(serverInst)
		util.removeExtraFilesRecur(
			modsSrc(),
			serverModsFolder
		)
		util.copyFolderRecur(
			modsSrc(),
			serverInst,
			denySubStrList=clientSideModNames
		)

def writeModlists():
	writeMods(modlistFile, os.listdir(modsSrc()))

	exportServerMods = os.listdir(instMods(config.servers[0]))
	writeMods(serverModlistFile, exportServerMods)

def writeMods(filename, mods):
	with open(os.path.join(config.configSrc, filename), "w") as f:
		for mod in mods:
			f.write(f"{mod}\n")

def modsSrc():
	return instMods(config.modsSrc)

def instMods(inst):
	return os.path.join(inst, modsFolder)
