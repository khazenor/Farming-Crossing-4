from list import collectionQuests as cqlist
from lib import kubejs

def genFloraTags():
	kubejs.generateSimpleTags(cqlist.allFlora, 'forge:flora_quest_items', 'fauna_quest_tag')
