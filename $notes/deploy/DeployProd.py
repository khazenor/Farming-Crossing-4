from src import paths
from src import deploy
from src import log

if __name__ == "__main__":
	log.init()
	paths.configSrc = "D:\\Lee\\Minecraft\\Twitch\\Instances\\Farming Crossing 4"
	paths.modsSrc = paths.configSrc

	paths.otherInsts = [
		'D:\\Lee\\Minecraft\\MultiMC\\instances\\Farming Crossing 4 Prod\\.minecraft',
		'D:\\Lee\\Dropbox\\Share\\FarmingCrossing4\\publicServerVersion'
	]

	deploy.deployModpack()
