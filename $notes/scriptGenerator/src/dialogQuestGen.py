from lib import ftbQuest
from lib import stringCleaning
from input import dialog
import random
from src import const
import os

speakerCount = {}

def deployDialogQuests():
	questContent = ""
	for dialogInst in dialog.dialogs:
		questContent += villagerDialogQuestContent(
			addBlankLines(dialogInst[dialog.textsKey]),
			dialogInst[dialog.nameKey],
			curSpeakerIdx(dialogInst[dialog.speakerKey]),
			dialog.speakers.index(dialogInst[dialog.speakerKey]),
			dialogInst[dialog.questIdKey]
		)
	ftbQuest.writeQuestChapter(
		"villager_dialogs",
		questFileContent(questContent)
	)

def curSpeakerIdx(speaker):
	if speaker in speakerCount:
		count = speakerCount[speaker]
		speakerCount[speaker] += 1
		return count
	else:
		speakerCount[speaker] = 1
		return 0
def addBlankLines(strList):
	newList = []
	for i in range(len(strList)):
		if i > 0:
			newList.append("")
		newList.append(strList[i])
	return newList

def villagerDialogQuestContent(dialogs, title, x, y, dependencyId):
	random.seed(title)
	outStr = '	{\n'
	outStr += f'		dependencies: ["{dependencyId}"]\n'
	outStr += '		disable_toast: true\n'
	outStr += '		hide: true\n'
	outStr += '		description: [\n'
	for dialog in dialogs:
		outStr += f'			"{dialog}"\n'
	outStr += '		]\n'
	outStr += '		icon: "minecraft:flower_banner_pattern"\n'
	outStr += f'		id: "{ftbQuest.randomId()}"\n'
	outStr += '		rewards: [{\n'
	outStr += '			auto: "invisible"\n'
	outStr += f'			command: "/function farming_crossing:{stringCleaning.cleanedNameStr(title)}"\n'
	outStr += '			elevate_perms: true\n'
	outStr += f'			id: "{ftbQuest.randomId()}"\n'
	outStr += '			silent: true\n'
	outStr += '			type: "command"\n'
	outStr += '		}]\n'
	outStr += '		tasks: [{\n'
	outStr += '			icon: "minecraft:glass"\n'
	outStr += f'			id: "{ftbQuest.randomId()}"\n'
	outStr += '			stat: "minecraft:walk_one_cm"\n'
	outStr += '			title: "Free Task"\n'
	outStr += '			type: "stat"\n'
	outStr += '			value: 1\n'
	outStr += '		}]\n'
	outStr += f'		title: "{title}"\n'
	outStr += f'		x: {x}.0d\n'
	outStr += f'		y: {y}.0d\n'
	outStr += '	}\n'
	return outStr

def questFileContent(questContent):
	outStr = '{\n'
	outStr += '	default_hide_dependency_lines: false\n'
	outStr += '	default_quest_shape: ""\n'
	outStr += '	filename: "villager_dialogs"\n'
	outStr += '	group: ""\n'
	outStr += '	icon: "minecraft:flower_banner_pattern"\n'
	outStr += '	id: "1F022BB35ADA735D"\n'
	outStr += '	order_index: 3\n'
	outStr += '	quest_links: [ ]\n'
	outStr += '	quests: [\n'
	outStr += questContent
	outStr += '	]\n'
	outStr += '	title: "Villager Dialogs"\n'
	outStr += '}\n'
	return outStr
