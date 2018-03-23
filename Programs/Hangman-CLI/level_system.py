import sqlite3, database

def generateLevel():
	level = []
	plus = 0
	for lv in range(1,51):
		level.append([lv,500+plus])
		plus += 500
	return level

def checkLevel(score):
	levels = generateLevel()
	currentLevel = 1
	for lv, lvScore in levels:
		#print("KEY: {} \n VALUE {}".format(key,value))
		if lvScore < score:
			currentLevel = lv
	return currentLevel

def updateLevel(pastLv,currentLv):
	if pastLv < currentLv:
		print("You are now in LV{}!".format(currentLv))
		database.upgradeLevel(currentLv)
	return currentLv

#checkLevel(2500)