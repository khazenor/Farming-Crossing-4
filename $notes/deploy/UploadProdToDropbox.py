from src import paths
from src import deploy
from src import log

if __name__ == "__main__":
	log.init()
	paths.configSrc = 'D:\\Lee\\Minecraft\\MultiMC\\instances\\Farming Crossing 4 Prod\\.minecraft'
	paths.modsSrc = paths.configSrc

	paths.otherInsts = [
		'D:\\Lee\\Dropbox\\Share\\FarmingCrossing4\\publicServerVersion'
	]

	deploy.deployModpack()
