import os
from src import const
from lib import stringCleaning

def writeFunction(name, content):
	with open(os.path.join(functionFolder(), f"{stringCleaning.cleanedNameStr(name)}.mcfunction"), 'w', encoding='utf-8') as f:
		f.write(content)

def functionFolder():
	return os.path.join(const.data(), 'farming_crossing', 'functions')
