#Version 0.2

import tkinter as tk
import database as db

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

def showRegister():
	#Removing login widgets
	l1.place_forget() # Sign in
	l2.place_forget() # Username 
	l3.place_forget() # Password 
	l4.place_forget() # The message that is shown when user/pw is wrong

	e1.place_forget() # Entry for username
	e2.place_forget() # Entry for password

	b1.place_forget() # Button for login 
	b2.place_forget() # Button for show register

	#Showing register widgets
	l5.place(x=30,y=30) # Sign up
	l6.place(x=200,y=150) # First name
	l7.place(x=200,y=190) # Last name
	l8.place(x=200,y=230) # Username
	l9.place(x=200,y=270) # Password
	l10.place(x=200,y=310) # Birthday

	e3.place(x=370,y=150) # First name
	e4.place(x=370,y=190) # Last name
	e5.place(x=370,y=230) # Username
	e6.place(x=370,y=270) # Password
	e7.place(x=370,y=310) # Birthday

	b3.place(x=300,y=350,height=50) # Register 
	b4.place(x=500,y=350,height=50) # Show Login


def showLogin():
	#Removing register widgets
	l5.place_forget() # Sign up
	l6.place_forget() # First name
	l7.place_forget() # Last name
	l8.place_forget() # Username
	l9.place_forget() # Password
	l10.place_forget() # Birthday
	l11.place_forget() # Error message

	e3.place_forget() # First name
	e4.place_forget() # Last name
	e5.place_forget() # Username
	e6.place_forget() # Password
	e7.place_forget() # Birthday

	b3.place_forget() # Register 
	b4.place_forget() # Show Login

	#Showing login widgets
	l1.place(x=30,y=30) # Sign in
	l2.place(x=130,y=180) # Username 
	l3.place(x=135,y=250) # Password 

	e1.place(x=360,y=180,width=300,height=55) # Entry for username
	e2.place(x=360,y=250,width=300,height=55) # Entry for password

	b1.place(x=300,y=330,width=150,height=50) # Button for login 
	b2.place(x=470,y=330,width=160,height=50) # Button for show register

def loginAttempt(event=None):
	access = False
	dbManager = db.Manage("database.db") #fileLocation
	dbManager.connect()
	dbManager.create_table("accounts")
	c = dbManager.conn.cursor()
	for account in c.execute("SELECT * FROM accounts"):
		if account[3] == e1.get() and account[4] == e2.get():
			access = True
			print("username or password found in database")
			break
	if not access:
		l4.place(x=200,y=380)
		print("username or password not found in database")
	else:
		l4.place_forget()
	dbManager.close()
	return access

def createAccount(event=None):
	dbManager = db.Manage("database.db")
	dbManager.connect()
	dbManager.create_table("accounts")
	if e3.get() and e4.get() and e5.get() and e6.get() and e7.get():
		if not hasNumbers(e3.get()) and not hasNumbers(e4.get()):
			try:
				dbManager.insert("accounts",e3.get(),e4.get(),e5.get(),e6.get(),e7.get())
				l11.place_forget()
			except:
				errorMessage.set("Username is already taken!")
				l11.place(x=270,y=400)
		else:
			errorMessage.set("First Name/Last Name can't contain numbers!")
			l11.place(x=150,y=400)
	dbManager.close()


root = tk.Tk()
root.title("School Management")
root.geometry("{}x{}".format(900,500))

#Login widgets

l1 = tk.Label(root,text="Sign in",font=("",50))

l2 = tk.Label(root,text="Username: ",font=("",30))

e1 = tk.Entry(root,font=("",20))
e1.bind("<Return>", loginAttempt)

l3 = tk.Label(root,text="Password:",font=("",30))

e2 = tk.Entry(root,font=("",20),show="*")
e2.bind("<Return>", loginAttempt)

l4 = tk.Label(root,text="Username or Password is wrond!",font=("",20))

b1 = tk.Button(root,text="Login",font=("",28),command=loginAttempt)
b2 = tk.Button(root,text="Register",font=("",28),command=showRegister)

#Register widgets

l5 = tk.Label(root,text="Sign up",font=("",50))

l6 = tk.Label(root,text="First Name: ",font=("",20))

l7 = tk.Label(root,text="Last Name: ",font=("",20))

l8 = tk.Label(root,text="Username: ",font=("",20))

l9 = tk.Label(root,text="Password: ",font=("",20))

l10 = tk.Label(root,text="Birthday: ",font=("",20))

errorMessage = tk.StringVar()
l11 = tk.Label(root,textvariable=errorMessage,font=("",20))

e3 = tk.Entry(root,font=("",20))
e3.bind("<Return>", createAccount)
 
e4 = tk.Entry(root,font=("",20))
e4.bind("<Return>", createAccount)

e5 = tk.Entry(root,font=("",20))
e5.bind("<Return>", createAccount)

e6 = tk.Entry(root,font=("",20),show="*")
e6.bind("<Return>", createAccount)

e7 = tk.Entry(root,font=("",20))
e7.bind("<Return>", createAccount)

b3 = tk.Button(root,text="Register",font=("",28),command=createAccount)

b4 = tk.Button(root,text="Login",font=("",28),command=showLogin)

showLogin()


root.mainloop()