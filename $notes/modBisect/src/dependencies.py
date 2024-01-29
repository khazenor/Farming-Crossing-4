import zipfile
import os
import re

modConfigDir = "META-INF/mods.toml"

modIdRegexHeader = 'modId *= *[\'"]?'

modFilenameKey = 'modFilename'
dependenciesKey = 'dependencies'
def getDependencies(modFolder, ignoreDependencies):
	dependenciesInfo = {}
	for modZipName in os.listdir(modFolder):
		modZip = zipfile.ZipFile(os.path.join(modFolder, modZipName))
		if modConfigDir in modZip.namelist():
			with modZip.open(modConfigDir) as configFile:
				configFileContent = str(configFile.read())
				modName = findModName(configFileContent)
				dependencies = findAndFilterDependencies(configFileContent, ignoreDependencies)
				dependenciesInfo[modName] = {
					modFilenameKey: modZipName,
					dependenciesKey: dependencies
				}
	return dependenciesInfo

def findModName(configFileContent):
	search = re.search(f'{modIdRegexHeader}[\w\d]*', configFileContent).group(0)
	modName = re.sub(modIdRegexHeader, '', search)
	return modName

def findAndFilterDependencies(configFileContent, ignoreDependencies):
	filteredDependencies = []
	dependencies = findDependencies(configFileContent)
	mandatories = findMandatories(configFileContent)

	for i in range(len(mandatories)):
		isMandatory = mandatories[i]
		if isMandatory:
			dependency = dependencies[i]
			if dependency not in ignoreDependencies:
				filteredDependencies.append(dependency)
	return filteredDependencies

def findDependencies(configFileContent):
	matches = re.findall(f'{modIdRegexHeader}[\w\d]*', configFileContent)
	mods = []
	for i in range(1, len(matches)):
		match = matches[i]
		mods.append(re.sub(f'{modIdRegexHeader}', '', match))
	return mods

def findMandatories(configFileContent):
	matches = re.findall('mandatory=\w*', configFileContent)
	mandatories = []
	for match in matches:
		mandatories.append(match.replace('mandatory=', '').lower() == 'true')
	return mandatories
