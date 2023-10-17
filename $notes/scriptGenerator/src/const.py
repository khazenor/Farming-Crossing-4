import os

priceItem = "kubejs:miles_ticket"

def serverScripts():
	return os.path.join(kubejs(), 'server_scripts')

def clientScripts():
	return os.path.join(kubejs(), 'client_scripts')

def farmersDelightCooking():
	return os.path.join(farmersDelightRecipes(), 'cooking')

def farmersDelightRecipes():
	return os.path.join(farmersDelight(), "recipes")

def farmersDelight():
	return os.path.join(data(), 'farmersdelight')

def data():
	return os.path.join(kubejs(), 'data')

def farmingForBlockheads():
	return os.path.join(data(), 'farmingforblockheads', 'farmingforblockheads_compat')

def kubejs():
	return '../../kubejs'

def config():
	return '../../config'

def ftbquests():
	return os.path.join(config(), "ftbquests")

def ftbChapters():
	return os.path.join(ftbquests(), "quests", "chapters")