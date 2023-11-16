from lib import ftbQuest
import random
from input import mileageRewardCollectionQuests as mrc
import math
from src import const
import os

def genMileageRewardProgramQuests():
	filename = "collection_achievements"
	random.seed(123)
	fileDir = os.path.join(const.ftbChapters(), f"{filename}.snbt")
	with open(fileDir, "w") as f:
		f.write(ftbQuest.questFileContent(
			"kubejs:miles_ticket",
			filename,
			"Collection Achievements",
			getQuestContent(),
		))

def getQuestContent():
	questContent = ""
	numRequiredStarts = [2, 5]
	startIncrement = 5
	incrementIncreaseRate = 5

	for y, collection in enumerate(mrc.collections):
		numRequired = numRequiredStarts[0]
		finalTicketValue = collection[mrc.finalTicketValueKey]
		collectionQuestIds = collection[mrc.questIdsKey]
		totalNumQuests = len(collectionQuestIds)
		increment = startIncrement
		x = 0
		print(collection[mrc.nameKey])
		while numRequired + increment < totalNumQuests:
			if x == 0:
				numUnpaidQuests = numRequired
			elif x < len(numRequiredStarts):
				numRequired = numRequiredStarts[x]
				numUnpaidQuests = numRequiredStarts[x] - numRequiredStarts[x - 1]
			ticketPerQuest = float(numRequired)/float(totalNumQuests) * finalTicketValue
			ticketValue = math.ceil(ticketPerQuest * numUnpaidQuests)

			# title strings
			action = collection[mrc.actionKey]
			itemName = collection[mrc.nameKey] + collection[mrc.pluralKey]

			seed(collection[mrc.iconKey], numRequired)
			questContent += ftbQuest.mileageRewardQuestContent(
				collection[mrc.iconKey],
				ticketValue,
				collectionQuestIds,
				numRequired=numRequired,
				title=f'{action} {numRequired} Unique {itemName}!',
				x=x,
				y=y
			)
			print(numRequired)

			# end values
			if numRequired + increment + increment < totalNumQuests:
				numUnpaidQuests = increment
			else:
				numUnpaidQuests = totalNumQuests - numRequired

			# update values outside of the first few quests
			if x >= len(numRequiredStarts) - 1:
				numRequired += increment
				increment += incrementIncreaseRate

			x += 1

		# final completion quest
		seed(collection[mrc.iconKey], -1)
		questContent += ftbQuest.mileageRewardQuestContent(
			collection[mrc.iconKey],
			numUnpaidQuests * finalTicketValue,
			collectionQuestIds,
			title=f'{collection[mrc.collectionKey]} Completion!',
			x=x,
			y=y,
			lastQuestItem=collection[mrc.lastQuestItemKey]
		)
		print(totalNumQuests)
	return questContent

def seed(icon, numRequired):
	seedStr = f"{icon}{numRequired}"
	random.seed(seedStr)

if __name__ == "__main__":
	genMileageRewardProgramQuests()