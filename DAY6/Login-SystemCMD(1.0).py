"""

Developer : Gjergj Kadriu
Version : 1.1

"""

username = ""
password = ""
ask_user = ""
ask_password = ""
logged_in = False

def register():
    print("Please create an account!")
    global username
    global password
    username = input("Create Username: ")
    password = input("Create password: ")
    #Just for debugging purposes
    #print("------ Username : " + username + "---- Password " + password)
    if username and password:
        print("You have successfully registered!")
        login()
    else:
        print("Some issues occured, please come back later!")

def login():
    ask_user = input("Username: ")
    ask_password = input("Password: ")
    if ask_user == username and ask_password == password:
        print("Logged in successfully!")
        logged_in = True
    else:
        print("Username or Password is wrong!")
        #Just for debugging purposes
        #print("------ Username : " + username + "---- Password " + password)

    


while not logged_in and not username or not password:
    register()
