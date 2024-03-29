from input import tipsInput
from src import const
import json
import os
from lib import util
from lib import ftbQuest

def genTips():
	folder = os.path.join(const.assets(), "fc_tips", "tips")
	util.removeFiles(folder)

	for tip in tipsInput.tips:
		json.dump({
			"tip": {
				"text": tip
			}
		}, open(
			os.path.join(folder, f'tip_{ftbQuest.randomId(tip).lower()}.json'), "w"
		))
