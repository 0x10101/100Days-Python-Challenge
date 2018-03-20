import sqlite3

def register():
    print("""
    /login to create an account if you don't have one already
    """)
    while True:
        print("Register an account!")
        username = input("Create Username: ").lower()
        if username == "/login":
            login()
        password = input("Create Password: ").lower()
        if password == "/login":
            login()
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""INSERT INTO accounts(username,password)
                   VALUES(?,?)""", (username,password))
        conn.commit()
        for account in c.execute("SELECT * from accounts"):
            for value in account:
                print(value)
        conn.close()
        print("Account successfully registered. Please log in!")
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
        password = input("Password: ").lower()
        if password == "/register":
            register()
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        access = [False,0,"","",0]
        for account in c.execute("SELECT * from accounts"):
            #Prints username and password for every row in account table
            #print(account[1],account[2])
            if username == account[1] and password == account[2]:
                #accounts[3] is the score
                print(account[3])
                access = [True,account[0],account[1],account[2],account[3]]
        if access[0]:
            print("Logged in successfully!")
            break
        else:
            print("Username or Password is wrong!")
        conn.close() #Closes the database connection
    print(access)
    return access

def accountInfo(ID,username,password,score):
    print("""
    ID : {}
    Username : {}
    Password : {}
    Score : {}
    """.format(ID,username,password,score))

