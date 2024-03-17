from input import tipsInput
from src import const
import json
import os
from lib import util

def genTips():
	folder = os.path.join(const.assets(), "fc_tips", "tips")
	util.removeFiles(folder)
	for i, tip in enumerate(tipsInput.tips):
		json.dump({
			"tip": {
				"text": tip
			}
		}, open(
			os.path.join(folder, f'tip_{i}.json'), "w"
		))
