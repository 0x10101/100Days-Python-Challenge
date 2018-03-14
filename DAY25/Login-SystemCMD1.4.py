"""

Developer : Gjergj Kadriu
Version : 1.4

Changes:
    -Create username,password,ID files if they don't exist
    -After register() username,password,ID are stored outside the program
    

toDo:
    -Make the code actually work :P
    -Be able to have/register more than just 1 account
    -Search for username,password inside a dictionary

"""

import sys


try:
    with open("username","x") as file:
        pass
except FileExistsError:
    pass

try:
    with open("password","x") as file:
        pass
except FileExistsError:
    pass

try:
    with open("ID","x") as file:
        pass
except FileExistsError:
    pass

accounts = {}

username = "gjergj"
password = "gjergj"
ask_user = ""
ask_password = ""
logged_in = False


def accountsUpdate(acc):
    fileID = open("ID","r")
    fileUser = open("username","r")
    filePass = open("password","r")
    IDlist = []
    userList = []
    passList = []
    for ID in fileID.readlines():
        IDlist.append(ID)
    for user in fileUser.readlines():
        userList.append(user)
    for passw in filePass.readlines():
        passList.append(passw)
    print(IDlist,userList,passList)
    for ID in IDlist:
        accounts[ID] = userList[ID], passList[ID]
    print(acc)
                
    

def register():
    print("Please create an account!")
    while True:
        username = input("Create Username: ")
        if username:
            with open("username","a") as file:
                file.write(username + "\n")
            break
        else:
            print("Please type a valid us!")
            continue
    while True:
        password = input("Create password: ")
        if password:
            with open("password","a") as file:
                file.write(password + "\n")
            break
        else:
            print("Please type a valid Password!")
            continue
                
    #Just for debugging purposes
    #print("------ Username : " + username + "---- Password " + password)
    if username and password:
        with open("ID","r") as file:
            lastID = file.readlines()[:-1]
        with open("ID","a") as file:  
            file.write(str(lastID) + "\n") #Update ID
        print("You have successfully registered!")
        #login(username,password)
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




#while not logged_in and not username or not password:
while True:
    accountsUpdate(accounts)
    register()
