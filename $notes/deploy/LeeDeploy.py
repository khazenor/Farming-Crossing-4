from src import paths
from src import deploy
from src import log

if __name__ == "__main__":
	log.init()

	paths.configSrc = 'D:\\Lee\\Minecraft\\MultiMC\\instances\\Farming Crossing 4\\.minecraft'

	paths.modsSrc = 'D:\\Lee\\Minecraft\\Twitch\\Instances\\1.20.1_FarmingCrossing4'

	paths.otherInsts = [
		'D:\\Lee\\Dropbox\\Share\\FarmingCrossing4\\install',
		'D:\\Lee\\Minecraft\\MultiMC\\instances\\Farming Crossing 4 Dupe\\.minecraft'
	]

	paths.servers = [
		'D:\\Lee\\Minecraft\\MultiMC\\instances\\Farming Crossing 4\\.minecraft\\$notes\\server\\Farming Crossing 4 Server',
		'D:\\Lee\\Minecraft\\MultiMC\\instances\\Farming Crossing 4\\.minecraft\\$notes\\server\\TestingServer',
		'D:\\Lee\\Minecraft\\MultiMC\\instances\\Farming Crossing 4\\.minecraft\\$notes\\server\\WilsonServer'
	]

	paths.dropboxDeployScriptLoc = 'D:\\Lee\\Dropbox\\Share\\FarmingCrossing4\\deployScript'
	deploy.deployModpack()
	input('press enter to exit...')
