
def invertDict(parentToChild):
	childToParent = {}
	for parent in parentToChild:
		child = parentToChild[parent]
		if isinstance(child, list):
			addItems = child
		else:
			addItems = [child]

		for addItem in addItems:
			if addItem in childToParent.keys():
				childToParent[addItem].append(parent)
			else:
				childToParent[addItem] = [parent]
	return childToParent

def addToDictList(dictList, key, value):
	if key in dictList.keys():
		dictList[key].append(value)
	else:
		dictList[key] = [value]

def appendToSetList(setList, item):
	if item not in setList:
		setList.append(item)

