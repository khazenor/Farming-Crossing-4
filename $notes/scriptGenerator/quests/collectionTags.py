from list import collectionQuests as cqlist
from input import collectionQuestsInput as cqin
from lib import kubejs

def genTags():
	kubejs.generateSimpleTags(cqlist.allFlora, 'forge:flora_quest_items', 'fauna_quest_tag')
	kubejs.generateSimpleTags(cqlist.allMinerals, 'forge:minerals', 'mineral_quest_tag')
	kubejs.generateSimpleTags(cqlist.allHats, 'forge:hats', 'hat_quest_tag')
	kubejs.generateSimpleTags(cqlist.allCosm, 'forge:clothes', 'clothes_quest_tag')
	genEntityTags()

def genEntityTags():
	entities = []
	for questline in cqin.questlines:
		if questline[cqin.filenameKey] == 'animal_watching':
			for questionGroup in questline[cqin.questGroupsKey]:
				for task in questionGroup[cqin.tasksKey]:
					entities.append(task[cqin.observeKey])
	entities.sort()
	kubejs.writeServerFile(
		kubejs.tagsContent(
			kubejs.eventAddItemToList(
				'kubejs:all_animals', entities
			),
			tagType='entity_type'
		),
		'entity_tags'
	)
