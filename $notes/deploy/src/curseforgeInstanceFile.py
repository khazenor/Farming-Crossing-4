from src import paths
import shutil
from src import log
import json
import os

def deployCurseforgeFile():
	if paths.modsSrc != paths.configSrc:
		log.log(' # Deploy Curseforge Instance file')
		instanceFileUrl = os.path.join(paths.modsSrc, 'minecraftinstance.json')
		fileJson = json.load(open(instanceFileUrl, 'r', encoding="utf-8"))
		copyUrl = os.path.join(paths.configSrc, 'curseforge_instance.json')
		json.dump(fileJson, open(copyUrl, 'w', encoding="utf-8"), indent=2)
