import os
import math
import re
import shutil
import json
from lib import ffprobe
from lib import kubejs
from src import const
from pathlib import Path


diskAndArtLocation = "D:\\Lee\\Minecraft\\MultiMC\\instances\\Farming Crossing 4\\.minecraft\\$notes\\usedSongs\\records"
categoryName = 'farming_crossing_records'

categoryFolder = os.path.join(const.assets(), categoryName)
soundFolder = os.path.join(categoryFolder, 'sounds', 'records')
textureFolder = os.path.join(categoryFolder, 'textures', 'item')

def deployMusicDiscs():
	musicDiscTagItems = []
	soundRegistryContent = ""
	itemRegistryContent = ""
	soundJsonDict = {}
	langJsonDict = {}

	for filename in os.listdir(diskAndArtLocation):
		if ".ogg" in filename:
			copyFiles(filename)
			addJsonDictEntry(filename, soundJsonDict)
			soundRegistryContent += kubejs.createSimple(soundId(filename))
			itemRegistryContent += itemRegistry(filename)
			musicDiscTagItems.append(itemId(filename))
			langJsonDict[f"item.kubejs.{cleanedFilename(filename)}.desc"] = noExt(filename)

		with open(os.path.join(const.startupScripts(), 'music_disc_registry.js'), 'w') as f:
			f.write(
				kubejs.registryFileContent('sound_event', soundRegistryContent) + "\n\n" +
				kubejs.registryFileContent('item', itemRegistryContent)
			)
		smartDump(soundJsonDict, os.path.join(categoryFolder, 'sounds.json'))
		smartDump(langJsonDict, os.path.join(categoryFolder, 'lang', 'en_us.json'))
		kubejs.generateSimpleTags(musicDiscTagItems, 'minecraft:music_discs', 'music_disc_tags')


def smartDump(jsonDict, fileDir):
	os.makedirs(Path(fileDir).parent, exist_ok=True)
	json.dump(jsonDict, open(fileDir, 'w'), indent=2)


def copyFiles(filename):
	textureFilename = filename.replace('.ogg', '.png')
	copyFile(diskAndArtLocation, textureFolder, textureFilename, f"{cleanedFilename(filename)}.png")
	copyFile(diskAndArtLocation, soundFolder, filename, f"{cleanedFilename(filename)}.ogg")

def copyFile(fromFolder, toFolder, fromFile, toFile):
	toFileDir = os.path.join(toFolder, toFile)
	if not os.path.exists(toFileDir):
		os.makedirs(toFolder, exist_ok=True)
		shutil.copy2(os.path.join(fromFolder, fromFile), toFileDir)

def addJsonDictEntry(filename, jsonDict):
	jsonDict[cleanedFilename(filename)] = {
		"category": "record",
		"sounds": [{
			"name": soundPath(filename),
			"stream": True
		}]
	}

def itemRegistry(filename):
	musicLength = math.ceil(
		ffprobe.getLength(os.path.join(diskAndArtLocation, filename))
	)
	itemTitle = noExt(filename)

	return kubejs.createMusicDisc(itemId(filename), soundId(filename), musicLength, itemPath(filename), itemTitle)

def itemId(filename):
	return f"kubejs:{cleanedFilename(filename)}"

def soundId(filename):
	return f"{categoryName}:{cleanedFilename(filename)}"

def soundPath(filename):
	return f"{categoryName}:records/{cleanedFilename(filename)}"

def itemPath(filename):
	return f"{categoryName}:item/{cleanedFilename(filename)}"

def cleanedFilename(filename):
	return cleanedNameStr(noExt(filename))

def cleanedNameStr(nameStr):
	newStr = re.sub('[^a-zA-Z ]+','', nameStr)
	newStr = re.sub(' +', '_', newStr)
	newStr = newStr.lower()
	return newStr

def noExt(fileStr):
	return fileStr.split('.')[0]