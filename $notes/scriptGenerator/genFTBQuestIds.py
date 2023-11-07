import random
parentStr = "0123456789ABCDEF"
stringLength = 15

def randomId():
	idStr = random.choice("01234567")
	for idx in range(stringLength):
		idStr += random.choice(parentStr)
	return idStr

if __name__ == "__main__":
	with open("output/ids.txt", "w") as f:
		for i in range(10000):
			f.write(f"id: \"{randomId()}\"\n")
