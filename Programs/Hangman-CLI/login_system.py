"""
Version 1.1
Changes:
    -accountInfo() shows level 
    -register() and login() use console.checkOption to see if user
       entered a cmd option

"""

import sqlite3, json, console
from database import insertAccount

def register():
    print("""
    /login to create an account if you don't have one already
    """)
    while True:
        print("Register an account!")
        username = input("Create Username: ").lower()
        if username == "/login":
            login()
        elif username != "/login":
            console.checkOption(False,username,"",0)
        password = input("Create Password: ").lower()
        if password == "/login":
            login()
        elif password !="/login":
            console.checkOption(False,password,"",0)
        
        #If the account was inserted then it returns True
        created = insertAccount(username,password,"",0)
        
        if created:
            login()
            break

def login():
    print("""
    /register to create an account if you don't have one already
    """)
    while True:
        username = input("Username: ").lower()
        if username == "/register":
            register()
        elif username != "/register":
            console.checkOption(False,username,"",0)
        password = input("Password: ").lower()
        if password == "/register":
            register()
        elif password != "/register":
            console.checkOption(False,password,"",0)
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        access = [False,0,"","",0]
        for account in cursor.execute("SELECT * from accounts"):
            #Prints username and password for every row in account table
            #print(account[1],account[2])
            if username == account[1] and password == account[2]:
                #accounts[3] is the score
                print(account[3])
                access = [True,account[0],account[1],account[2],account[3],account[4]]
                with open("data","w") as outfile:
                    json.dump(access,outfile)
        if access[0]:
            print("Logged in successfully!")
            break
        else:
            print("Username or Password is wrong!")
        db.close() #Closes the database connection
    print(access)
    return access

def accountInfo(ID,username,password,score,level):
    print("""
    ID : {}
    Username : {}
    Password : {}
    Score : {}
    Level : {}
    """.format(ID,username,password,score,level))

