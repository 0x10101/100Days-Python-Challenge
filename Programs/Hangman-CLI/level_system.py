import sqlite3

def generateLevel():
	level = []
	plus = 250
	for lv in range(1,51):
		level.append([lv,500+plus])
		plus += 150
	return level

def checkLevel(score):
	levels = generateLevel()
	print(levels)
	currentLevel = 1
	for key, value in levels:
		#print("KEY: {} \n VALUE {}".format(key,value))
		if value < score:
			currentLevel = key
	return currentLevel

def updateLevel(pastLevel,currentLevel):
	if pastLevel < currentLevel:
		print("You are now in LV{}!".format(currentLevel))
		database.upgradeLevel(currentLevel)

#checkLevel(2500)