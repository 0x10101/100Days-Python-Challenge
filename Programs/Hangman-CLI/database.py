"""
Version 1.1
Changes:
        -Created showScoreboard() function
        -Created deleteAccount(ID) function

Version 1.2
Changes:
        -added level INTEGER DEFAULT 1 on createDatabase() 

"""

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
                level	INTEGER	DEFAULT 1,
                PRIMARY KEY(`ID`)) """)
        db.commit()

def get_accountInfo():
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    for account in cursor.execute("SELECT * from accounts"):
        #Prints username and password for every row in account table
        #print(account[1],account[2])
        if username == account[1] and password == account[2]:
            #accounts[3] is the score
            print(account[3])
            access = [True,account[0],account[1],account[2],account[3],account[4]]
    db.commit()
    db.close()
    return access


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

def deleteAccount(ID):
        while True:
                perm = input("Are you sure you want to delete this account!? Y/n :")
                perm = perm.lower().strip()
                if perm == "y":
                        break
                elif perm == "n":
                        break
        if perm == "y":
                db = sqlite3.connect("database.db")
                cursor = db.cursor()
                cursor.execute("DELETE from accounts WHERE rowid=?", (ID,))
                print("Account deleted..!")
                db.commit()
                db.close()
                logged_in = False
                return logged_in

def addScore(currentScore,addScore):
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        cursor.execute("""
            UPDATE accounts SET score = ?
            WHERE username = ? """, (currentScore,addScore))
        db.commit()
        db.close()

def showScoreboard():
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        for account in cursor.execute("SELECT * from accounts"):
                print("{} Score --> {}".format(account[1],account[3]))
        db.commit()
        db.close()


def upgradeLevel(currentLevel):
    db = sqlite3.connect("database.db")
    ID = get_accountInfo()[1]
    cursor = db.cursor()
    cursor.execute("INSERT INTO accounts(level) where rowid=?", (ID,))
    db.commit()
    db.close()
    print("You upgraded to level {}".format(ID))

print(get_accountInfo()[1])

#deleteAccount(4)
