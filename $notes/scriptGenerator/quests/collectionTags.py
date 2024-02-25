from list import collectionQuests as cqlist
from lib import kubejs

def genTags():
	kubejs.generateSimpleTags(cqlist.allFlora, 'forge:flora_quest_items', 'fauna_quest_tag')
	kubejs.generateSimpleTags(cqlist.allMinerals, 'forge:minerals', 'mineral_quest_tag')
	kubejs.generateSimpleTags(cqlist.allHats, 'forge:hats', 'hat_quest_tag')
	kubejs.generateSimpleTags(cqlist.allCosm, 'forge:clothes', 'clothes_quest_tag')
