import random
import os
from src import const
parentStr = "0123456789ABCDEF"
stringLength = 15

def randomId():
	idStr = random.choice("01234567")
	for idx in range(stringLength):
		idStr += random.choice(parentStr)
	return idStr

def questFileContent(icon, filename, title, questContent):
	outStr = ""
	outStr += f'{{\n'
	outStr += f'	default_hide_dependency_lines: false\n'
	outStr += f'	default_quest_shape: ""\n'
	outStr += f'	filename: "{filename}"\n'
	outStr += f'	group: ""\n'
	outStr += f'	icon: "{icon}"\n'
	outStr += f'	id: "{randomId()}"\n'
	outStr += f'	order_index: 1\n'
	outStr += f'	quest_links: []\n'
	outStr += f'	quests: [\n'
	outStr += questContent
	outStr += f'	]\n'
	outStr += f'	title: "{title}"'
	outStr += f'}}\n'
	return outStr

def mileageRewardQuestContent(icon, numTickets, dependents, numRequired=0, title=None, x=0, y=0, lastQuestItem=None):
	outStr = ""
	outStr += f'{{\n'
	outStr += f'	dependencies: [\n'
	outStr += arrToStringContent(dependents, 4)
	outStr += f'	]\n'
	outStr += f'	icon: "{icon}"\n'
	outStr += f'	id: "{randomId()}"\n'
	if numRequired:
		outStr += f'	min_required_dependencies: {numRequired}\n'
	outStr += f'	rewards: [\n'
	if lastQuestItem:
		outStr += f'		{{\n'
		outStr += f'			id: "{randomId()}"\n'
		outStr += f'			item: "{lastQuestItem}"\n'
		outStr += f'			type: "item"\n'
		outStr += f'		}}\n'
	outStr += f'		{{\n'
	outStr += f'			count: {numTickets}\n'
	outStr += f'			id: "{randomId()}"\n'
	outStr += f'			item: "kubejs:miles_ticket"\n'
	outStr += f'			type: "item"\n'
	outStr += f'		}}\n'
	outStr += f'	]\n'
	outStr += f'	tasks: [{{\n'
	outStr += f'		id: "{randomId()}"\n'
	outStr += f'		type: "item"\n'
	outStr += f'	}}]\n'
	if title:
		outStr += f'	title: "{title}"\n'
	outStr += f'	x: {float(x)}d\n'
	outStr += f'	y: {float(y)}d\n'
	outStr += f'}}\n'

	return outStr

def arrToStringContent(array, tabs=0):
	outStr = ""
	for item in array:
		for i in range(tabs):
			outStr += "\t"
		outStr += f'"{item}"\n'
	return outStr

def writeQuestChapter(chapterName, content):
	with open(
			os.path.join(const.ftbChapters(), f"{chapterName}.snbt"),
			'w',
			encoding='utf-8'
		) as f:
		f.write(content)