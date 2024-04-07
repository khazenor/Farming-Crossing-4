from src import util, paths, log
import os

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
	'Xaeros_Minimap',
	'realcamera',
	'Tips',
	'l2library'
]

modsFolder = 'mods'
modlistFile = 'modlist.txt'
serverModlistFile = 'serverModlist.txt'

def deployMods():
	log.log('## Deploying Mods...')
	deployToClients()
	deployToServers()
	writeModlists()

def deployToClients():
	log.log(' # Deploy Clients')
	clientInsts = paths.otherInsts + [paths.configSrc]
	for clientInst in clientInsts:
		util.copyFolder(
			modsSrc(),
			clientInst
		)

def deployToServers():
	log.log(' # Deploy Servers')
	for serverInst in paths.servers:
		serverModsFolder = instMods(serverInst)
		util.removeExtraFilesRecur(
			modsSrc(),
			serverModsFolder,
			removeSubStrList=clientSideModNames
		)
		util.copyFolderRecur(
			modsSrc(),
			serverInst,
			denySubStrList=clientSideModNames
		)

def writeModlists():
	if len(paths.servers) > 0:
		writeMods(modlistFile, os.listdir(modsSrc()))

		exportServerMods = os.listdir(instMods(paths.servers[0]))
		writeMods(serverModlistFile, exportServerMods)

def writeMods(filename, mods):
	with open(os.path.join(paths.configSrc, filename), "w") as f:
		for mod in mods:
			f.write(f"{mod}\n")

def modsSrc():
	return instMods(paths.modsSrc)

def instMods(inst):
	return os.path.join(inst, modsFolder)
