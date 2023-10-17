import os

def configSrc():
	return 'D:\\Lee\\Minecraft\\MultiMC\\instances\\Farming Crossing 4\\.minecraft'

def modsSrc():
	return 'D:\\Lee\\Minecraft\\Twitch\\Instances\\1.20.1_FarmingCrossing4'

def otherInsts():
	return [
	]
def questUpdateServer():
	return None

def servers():
	return [
	]

def enableMods():
	return [
	]

def deleteRelativeUrls():
	return [
		'config\\defaultoptions\\options.txt',
		'config\\defaultoptions\\optionsof.txt',
		'config\\defaultoptions\\servers.dat',
		'config\\brb.toml',
		'config\\effortlessbuilding-client.toml',
		'config\\chimes-client.toml'
	]

def deleteConfigFolders():
	return [
		'config\\controllable'
	]

def mods(location):
	return os.path.join(location, 'mods')

def modsAdd(location):
	return os.path.join(location, 'mods_add')

def configFolder(location):
	return os.path.join(location, 'config')

def questFolder(location):
	return os.path.join(configFolder(location), 'ftbquests', 'quests')

def savedQuestFolder(location):
	return os.path.join(location, 'local', 'ftbquests', 'saved')

def allSubFolders():
	return configFolders() + [
		'global_packs'
	]

def configFolders():
	return reloadWhileRunningFolders() + [
		'config'
	]

def reloadWhileRunningFolders():
	return [
		'defaultconfigs',
		'kubejs',
		'scripts'
	]

def clientSideModNames():
	return [
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
		'controllable'
	]