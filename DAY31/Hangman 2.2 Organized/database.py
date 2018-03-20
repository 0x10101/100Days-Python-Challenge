import sqlite3


def createDatabase():
	try:
		
		db = sqlite3.connect("database.db")
		cursor = db.cursor()
		cursor.execute("""
		CREATE TABLE accounts (
			ID	INTEGER,
			username	TEXT	UNIQUE,
			password	TEXT,
			score	INTEGER DEFAULT 0,
			PRIMARY KEY(`ID`)) """)
		db.commit()
	except sqlite3.OperationalError:
		pass
	
def insertAccount(user,passw):
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	userTaken = False
	try:
		cursor.execute("""INSERT INTO accounts(username,password)
				VALUES(?,?)""", (user,passw))
	except sqlite3.IntegrityError:
		userTaken = True
		print("Username is already taken!")
	db.commit()
	for account in cursor.execute("SELECT * from accounts"):
		for value in account:
			print(value)
	db.close()
	if not userTaken:
		print("Account successfully registered. Please log in!")
	return userTaken

