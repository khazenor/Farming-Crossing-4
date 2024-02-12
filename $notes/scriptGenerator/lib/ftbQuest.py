import random
import os
from src import const
parentStr = "0123456789ABCDEF"
stringLength = 15
ticketId = 'kubejs:miles_ticket'

def questFileContent(icon, filename, title, questContent, orderIndex=1, questGroupId=''):
	outStr = ""
	outStr += f'{{\n'
	outStr += f'	default_hide_dependency_lines: false\n'
	outStr += f'	default_quest_shape: ""\n'
	outStr += f'	filename: "{filename}"\n'
	outStr += f'	group: "{questGroupId}"\n'
	outStr += f'	icon: "{icon}"\n'
	outStr += f'	id: "{randomId(filename)}"\n'
	outStr += f'	order_index: {orderIndex}\n'
	outStr += f'	quest_links: []\n'
	outStr += f'	quests: [\n'
	outStr += questContent
	outStr += f'	]\n'
	outStr += f'	title: "{title}"'
	outStr += f'}}\n'
	return outStr

def observationQuestContent(questId, icon, name, observe, command, dependency, x=0, y=0):
	return questContent(
		questId,
		commandRewardContent(command),
		observationTaskContent(icon, name, observe),
		x=x,
		y=y,
		dependencies=[dependency],
		disableToast=True
	)

def collectionQuestContent(questId, itemId, command, dependency, x=0, y=0):
	return questContent(
		questId,
		commandRewardContent(command),
		simpleItemContent(itemId),
		x=x,
		y=y,
		dependencies=[dependency],
		disableToast=True
	)

def collectionSubQuestContent(dependencies, title, icon, ticketReward, additionalRewards, x=0, y=0):
	rewardContent = simpleItemContent(ticketId, ticketReward)
	for additionalReward in additionalRewards:
		rewardContent += simpleItemContent(additionalReward)
	return questContent(
		randomId(),
		rewardContent,
		freeTaskContent(),
		dependencies=dependencies,
		title=title,
		icon=icon,
		x=x,
		y=y,
		hide=False
	)

def mileageRewardQuestContent(icon, numTickets, dependents, numRequired=0, title=None, x=0, y=0, lastQuestItem=None):
	rewardContent = simpleItemContent(itemId=ticketId, count=numTickets)
	if lastQuestItem:
		rewardContent += simpleItemContent(itemId=lastQuestItem)
	return questContent(
		randomId(),
		rewardContent,
		freeTaskContent(),
		title=title,
		icon=icon,
		x=x,
		y=y,
		dependencies=dependents,
		numRequired=numRequired
	)

def questContent(
	id, rewardContent, taskContent,
	title='', icon='', x=0, y=0, dependencies=[],
	disableToast=False, hide=True, numRequired=0
):
	outStr = ''
	outStr += '		{\n'
	if len(dependencies) > 0:
		outStr += '			dependencies: [\n'
		outStr += arrToStringContent(dependencies, 4)
		outStr += '			]\n'
	if icon:
		outStr += f'			icon: "{icon}"\n'
	if disableToast:
		outStr += '			disable_toast: true\n'
	if hide:
		outStr += '			hide: true\n'
	outStr += f'			id: "{id}"\n'
	if numRequired:
		outStr += f'			min_required_dependencies: {numRequired}\n'

	outStr += '			rewards: [\n'
	outStr += rewardContent
	outStr += '			]\n'

	outStr += '			tasks: [\n'
	outStr += taskContent
	outStr += '			]\n'
	outStr += f'			x: {float(x)}d\n'
	outStr += f'			y: {float(y)}d\n'
	if len(title) > 0:
		outStr += f'			title: "{title}"\n'
	outStr += '		}\n'

	return outStr

def simpleItemContent(itemId, count=1):
	outStr = ''
	outStr += f'		{{\n'
	if count > 1:
		outStr += f'			count: {count}\n'
	outStr += f'			id: "{randomId(itemId)}"\n'
	outStr += f'			item: "{itemId}"\n'
	outStr += f'			type: "item"\n'
	outStr += f'		}}\n'
	return outStr

def observationTaskContent(icon, title, observation):
	outStr = ''
	outStr += '				{'
	outStr += f'					icon: "{icon}"'
	outStr += f'					id: "{randomId()}"'
	outStr += '					observe_type: 5'
	outStr += '					timer: 0L'
	outStr += f'					title: "{title}"'
	outStr += f'					to_observe: "{observation}"'
	outStr += '					type: "observation"'
	outStr += '				}'
	return outStr

def freeTaskContent():
	outStr = ''
	outStr += '				{\n'
	outStr += '					icon: "minecraft:glass"\n'
	outStr += f'					id: "{randomId()}"\n'
	outStr += '					stat: "minecraft:walk_one_cm"\n'
	outStr += '					title: "Free Task"\n'
	outStr += '					type: "stat"\n'
	outStr += '					value: 1\n'
	outStr += '				}\n'
	return outStr

def commandRewardContent(command, title='', icon='', silent=True):
	outStr = ''
	outStr += '				{\n'
	outStr += f'					command: "/{command}"\n'
	outStr += '					elevate_perms: true\n'
	outStr += '					auto: "invisible"\n'
	outStr += '					exclude_from_claim_all: true\n'
	if len(icon) > 0:
		outStr += f'					icon: "{icon}"\n'
	outStr += f'					id: "{randomId(command)}"\n'
	outStr += '					silent: true\n'
	if len(title) > 0:
		outStr += f'					title: "{title}"\n'
	outStr += '					type: "command"\n'
	outStr += '				}\n'
	return outStr

def arrToStringContent(array, tabs=0):
	outStr = ""
	for item in array:
		for i in range(tabs):
			outStr += "\t"
		outStr += f'"{item}"\n'
	return outStr

def randomId(seed=''):
	if (len(seed) > 0):
		random.seed(seed)
	idStr = random.choice("01234567")
	for idx in range(stringLength):
		idStr += random.choice(parentStr)
	return idStr

def writeQuestChapter(chapterName, content):
	with open(
			os.path.join(const.ftbChapters(), f"{chapterName}.snbt"),
			'w',
			encoding='utf-8'
		) as f:
		f.write(content)
