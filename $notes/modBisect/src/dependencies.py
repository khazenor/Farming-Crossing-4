import zipfile
import os
import re

modConfigDir = "META-INF/mods.toml"

dependenciesRegex = 'dependencies\.[\w\d_]*'
modRegex = 'modId="[\w\d]*'
mandatoryRegex = 'mandatory=\w*'
modConfigRegex = f'{dependenciesRegex}\]\]\\\\r\\\\n    {modRegex}"\\\\r\\\\n    {mandatoryRegex}'

modFilenameKey = 'modFilename'
dependenciesKey = 'dependencies'
def getDependencies(modFolder, ignoreDependencies):
	dependenciesInfo = {}
	for modZipName in os.listdir(modFolder):
		modZip = zipfile.ZipFile(os.path.join(modFolder, modZipName))
		if modConfigDir in modZip.namelist():
			with modZip.open(modConfigDir) as configFile:
				configFileContent = str(configFile.read())
				for dependConfigSnippet in re.findall(modConfigRegex, configFileContent):
					modName = findField(dependenciesRegex, '\.', dependConfigSnippet)
					if modName not in dependenciesInfo:
						dependenciesInfo[modName] = {
							modFilenameKey: modZipName,
							dependenciesKey: []
						}
					dependencyInfo = dependenciesInfo[modName]

					dependency = findField(modRegex, '="', dependConfigSnippet)
					isMandatory = findField(mandatoryRegex, '=', dependConfigSnippet).lower() == 'true'

					if isMandatory:
						if dependency not in ignoreDependencies:
							if dependenciesKey in dependenciesInfo:
								dependencyInfo[dependenciesKey].append(dependency)
	return dependenciesInfo

def findField(regex, delimRegex, snippet):
	fieldWithName = re.search(regex, snippet).group(0)
	fieldWithDelim = re.search(f'{delimRegex}.*', fieldWithName).group(0)
	field = re.sub(delimRegex, "", fieldWithDelim)
	return field



