"""

Developer : Gjergj Kadriu
Version : 1.3
26.02.2018

Changes:
    -Passed arguments to login() function to remove global variables
    

"""

import sys

username = ""
password = ""
ask_user = ""
ask_password = ""
logged_in = False


def register():
    print("Please create an account!")
    while not False:
        username = input("Create Username: ")
        if username:
            break
        else:
            print("Please type a valid us!")
            continue
        # put a boolean value in 'pasw' variable to make a while not pasw loop
        # use it for making the expression true :P
        # I used the while loop and if's to not let password be blank and get repeated
        # until the user inputs a valid data for the password variable
    while not False:
        password = input("Create password: ")
        if password:
            break
        else:
            print("Please type a valid Password!")
            continue
                
    #Just for debugging purposes
    #print("------ Username : " + username + "---- Password " + password)
    if username and password:
        print("You have successfully registered!")
        login(username,password)
    else:
        print("Some issues occured, please type a valid Username and Password!")


def login(user,passw):
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
    #If the input of the user for ask_user is the same as for username and ask_password
    #Is the same ass password then the expression is true and logged_in is set True
    if ask_user == user and ask_password == passw:
        print("Logged in successfully!")
        logged_in = True
        sys.exit()
    else:
        print("Username or Password is wrong!")
        #Just for debugging purposes
        #print("------ Username : " + username + "---- Password " + password)

    


while not logged_in and not username or not password:
    register()
