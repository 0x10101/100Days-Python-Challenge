username = ""
password = ""

if not username:
    print("Please create an account!")
    username = input("Create Username: ")
if not password:
    password = input("Create password: ")

if username and password:
    print("You have successfully registered!")

logged_in = False

while not logged_in:
    ask_user = input("Username: ")
    ask_password = input("Password: ")
    if ask_user == username and ask_password == password:
        print("Logged in successfully!")
        logged_in = True
    else:
        print("Username or Password is wrong!")
        
#Class version
