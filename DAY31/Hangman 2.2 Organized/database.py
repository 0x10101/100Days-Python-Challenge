import sqlite3


def createDatabase():		
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
                ID	INTEGER,
                username	TEXT	UNIQUE,
                password	TEXT,
                score	INTEGER DEFAULT 0,
                PRIMARY KEY(`ID`)) """)
        db.commit()

def insertAccount(user,passw):
        userTaken = False
        try:
                db = sqlite3.connect("database.db")
                cursor = db.cursor()
                cursor.execute("""INSERT INTO accounts(username,password)
                                VALUES(?,?)""", (user,passw))
                db.commit()
                for account in cursor.execute("SELECT * from accounts"):
                        for value in account:
                                print(value)
                db.close()
        except sqlite3.IntegrityError:
                userTaken = True
                print("Username is already taken!")
        if not userTaken:
                print("Account successfully registered. Please log in!")
        return userTaken

def addScore(currentScore,addScore):
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        cursor.execute("""
            UPDATE accounts SET score = ?
            WHERE username = ? """, (currentScore,addScore))
        db.commit()
        db.close()
                

