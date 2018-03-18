#Handwritten code made out of complete boredom in class :P

import sys
    

def login():
    user = input("Username: ")
    passw = input("Password: ")

    for key, value in accounts.items():
        print(key,value)
        if key == user and value == passw:
            print("Logged in")
            sys.exit()

accounts = {}

while True:
    username = input("Create Username: ")
    password = input("Create Password: ")

    accounts[username] = password
    print("Account registered")
    ask = input("Do you want to login? Y,n : ")
    if ask.lower() == "y":
        login()
        
