import sqlite3

def generateLevel():
	level = []
	plus = 250
	for lv in range(1,51):
		level.append([lv,500+plus])
		plus += 150
	return level

