"""

Developer : Gjergj Kadriu
Version : 1.2
26.02.2018

Changes -
    -Renamed username and password to USERNAME and PASSWORD to follow standard style
    -The user can't leave blank any of the inputs like in version 1.0 and 1.1 and
     it will ask for the input until valid one is given!
    

"""

USERNAME = ""
PASSWORD = ""
ask_user = ""
ask_password = ""
logged_in = False


def register():
    print("Please create an account!")
    global USERNAME
    global PASSWORD
    while not False:
        USERNAME = input("Create Username: ")
        if not USERNAME:
            print("Please type a valid Username!")
            continue
        else:
            break
        # put a boolean value in 'pasw' variable to make a while not pasw loop
        # use it for making the expression true :P
        # I used the while loop and if's to not let password be blank and get repeated
        # until the user inputs a valid data for the PASSWORD variable
    pasw = False
    while not pasw:
        PASSWORD = input("Create password: ")
        if not PASSWORD:
            print("Please type a valid Password!")
            continue
        elif PASSWORD:
            pasw = True
        else:
            print("Some issues occured, please come again later")
            pasw = True
                
    #Just for debugging purposes
    #print("------ Username : " + USERNAME + "---- Password " + PASSWORD)
    if USERNAME and PASSWORD:
        print("You have successfully registered!")
        login()
    else:
        print("Some issues occured, please type a valid Username and Password!")


def login():
    while True:
        ask_user = input("Username: ")
        if not ask_user:
            print("Please type a valid Username!")
            continue
        ask_p = False
        # put a boolean value in 'ask_p' variable to make a while not ask_p loop
        # use it for making the expression true :P
        # I used the while loop and if's to not let ask_password be blank and get repeated
        # until the user inputs a valid data for the ask_password variable
        while not ask_p:
            ask_password = input("Password: ")
            if not ask_password:
                print("Please type a valid Password!")
            else:
                break
        break
    #If the input of the user for ask_user is the same as for USERNAME and ask_password
    #Is the same ass PASSWORD then the expression is true and logged_in is set True
    if ask_user == USERNAME and ask_password == PASSWORD:
        print("Logged in successfully!")
        logged_in = True
    else:
        print("Username or Password is wrong!")
        #Just for debugging purposes
        #print("------ Username : " + username + "---- Password " + password)

    


while not logged_in and not USERNAME or not PASSWORD:
    register()
