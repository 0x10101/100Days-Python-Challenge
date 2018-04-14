#Version 0.2

import tkinter as tk
from tkinter import ttk
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

	e1_text.set("")
	e2_text.set("")
	e1.place(x=360,y=180,width=300,height=55) # Entry for username
	e2.place(x=360,y=250,width=300,height=55) # Entry for password

	b1.place(x=300,y=330,width=150,height=50) # Button for login 
	b2.place(x=470,y=330,width=160,height=50) # Button for show register

def hideLoginRegister():
	#Removing login widgets
	l1.place_forget() # Sign in
	l2.place_forget() # Username 
	l3.place_forget() # Password 
	l4.place_forget() # The message that is shown when user/pw is wrong

	e1.place_forget() # Entry for username
	e2.place_forget() # Entry for password

	b1.place_forget() # Button for login 
	b2.place_forget() # Button for show register
	
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

def logged_in():
	tabControl.add(tabDashboard,text='Dashboard')
	tabControl.add(tabStaff,text='Staff Management')
	tabControl.add(tabClassTypes,text='Class Types')
	tabControl.add(tabClasses,text='Classes')
	tabControl.add(tabStudents,text='Students')
	tabControl.add(tabAccount,text=e1.get())
	tabControl.pack(expand=1,fill='both')

	b5.place(x=700,y=0,width=200,height=20)
	#b6.place(x=500,y=0,width=200,height=20)
	s.configure("TNotebook", borderwidth=1)


def logged_out():
	tabControl.hide(tabDashboard)
	tabControl.hide(tabStaff)
	tabControl.hide(tabClassTypes)
	tabControl.hide(tabClasses)
	tabControl.hide(tabStudents)
	tabControl.hide(tabAccount)
	b5.place_forget()
	#b6.place_forget()
	s.configure("TNotebook", borderwidth=0)
	showLogin()

def loginAttempt(event=None):
	access = False
	dbManager = db.Manage("database.db") #fileLocation
	dbManager.connect()
	dbManager.create_table("accounts",accounts_columns)
	c = dbManager.conn.cursor()
	for account in c.execute("SELECT * FROM accounts"):
		if account[3] == e1.get() and account[4] == e2.get():
			access = True
			accountInfo = {"ID":account[0],
							"First Name":account[1],
							"Last Name":account[2],
							"Username":account[3],
							"Password":account[4],
							"Birthday":account[5]}
			print("username or password found in database")
			print(accountInfo)
			tabAccountWidgets(accountInfo)
			#b6_user.set(e1.get())

			hideLoginRegister()
			logged_in()
			break
	if not access:
		l4.place(x=200,y=380)
		print("username or password not found in database")
	else:
		l4.place_forget()
	dbManager.close()
	return accountInfo

def createAccount(event=None):
	dbManager = db.Manage("database.db")
	dbManager.connect()
	dbManager.create_table("accounts",accounts_columns)
	#Testing
	#values = e3.get(),e4.get(),e5.get(),e6.get(),e7.get()	
	#dbManager.insert("accounts",accounts_columnsList,values)
	if e3.get() and e4.get() and e5.get() and e6.get() and e7.get():
		if not hasNumbers(e3.get()) and not hasNumbers(e4.get()):
			try:
				values = e3.get(),e4.get(),e5.get(),e6.get(),e7.get()	
				dbManager.insert("accounts",accounts_columnsList,values)
				l11.place_forget()
			except:
				errorMessage.set("Username is already taken!")
				l11.place(x=270,y=400)
		else:
			errorMessage.set("First Name/Last Name can't contain numbers!")
			l11.place(x=150,y=400)
	else:
		errorMessage.set("Please complete all the fields!")
		l11.place(x=260,y=400)
	dbManager.close()

def saveAccountInfo():
	pass

def editAccountInfo():
	l13_data.set("First Name:")
	l14_data.set("Last Name:")
	l15_data.set("Username:")
	l16_data.set("Password:")
	l17_data.set("Birthday:")

	b7.place(x=600,y=180,width=100,height=40)

	e8.place(x=275,y=100,width=200,height=40)
	e9.place(x=275,y=140,width=200,height=40)
	e10.place(x=275,y=180,width=200,height=40)
	e11.place(x=275,y=220,width=200,height=40)
	e12.place(x=275,y=260,width=200,height=40)


def tabAccountWidgets(accountInf):
	l13_data.set("First Name: {}".format(accountInf["First Name"]))
	l14_data.set("Last Name: {}".format(accountInf["Last Name"]))
	l15_data.set("Username: {}".format(accountInf["Username"]))
	l16_data.set("Password: {}".format(accountInf["Password"]))
	l17_data.set("Birthday: {}".format(accountInf["Birthday"]))

	l12.place(x=15,y=30)

	l13.place(x=100,y=100)

	l14.place(x=100,y=140)

	l15.place(x=100,y=180)

	l16.place(x=100,y=220)

	l17.place(x=100,y=260)

	b6.place(x=500,y=180,width=100,height=40)

accounts_columns = """			
			name TEXT,
			lastname TEXT,
			username TEXT UNIQUE,
			password TEXT,
			birthday TEXT """

accounts_columnsList = "name,lastname,username,password,birthday"

root = tk.Tk()
root.title("School Management")
root.geometry("{}x{}".format(900,500))

s = ttk.Style()

tabControl = ttk.Notebook(root)
tabDashboard = ttk.Frame(tabControl)
tabStaff = ttk.Frame(tabControl)
tabClassTypes = ttk.Frame(tabControl)
tabClasses = ttk.Frame(tabControl)
tabStudents = ttk.Frame(tabControl)
tabAccount = ttk.Frame(tabControl)

#Login widgets

l1 = tk.Label(root,text="Sign in",font=("",50))

l2 = tk.Label(root,text="Username: ",font=("",30))

e1_text = tk.StringVar()
e1 = tk.Entry(root,textvariable=e1_text,font=("",20))
e1.bind("<Return>", loginAttempt)

l3 = tk.Label(root,text="Password:",font=("",30))

e2_text = tk.StringVar()
e2 = tk.Entry(root,textvariable=e2_text,font=("",20),show="*")
e2.bind("<Return>", loginAttempt)

l4 = tk.Label(root,text="Username or Password is wrong!",font=("",20))

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

###Logged in widgets

# Buttons near notebook widgets
b5 = tk.Button(root,text="Log out!",command=logged_out)

#b6_user = tk.StringVar()
#b6 = tk.Button(root,textvariable=b6_user,command=showAccountInfo)

#Accounts widgets

l12 = tk.Label(tabAccount,text="Account Information",font=("",30))

l13_data = tk.StringVar()
l13 = tk.Label(tabAccount,textvariable=l13_data,font=("",20))
e8 = tk.Entry(tabAccount,font=("",20))


l14_data = tk.StringVar()
l14 = tk.Label(tabAccount,textvariable=l14_data,font=("",20))
e9 = tk.Entry(tabAccount,font=("",20))

l15_data = tk.StringVar()
l15 = tk.Label(tabAccount,textvariable=l15_data,font=("",20))
e10 = tk.Entry(tabAccount,font=("",20))

l16_data = tk.StringVar()
l16 = tk.Label(tabAccount,textvariable=l16_data,font=("",20))
e11 = tk.Entry(tabAccount,font=("",20))

l17_data = tk.StringVar()
l17 = tk.Label(tabAccount,textvariable=l17_data,font=("",20))
e12 = tk.Entry(tabAccount,font=("",20))

b6 = tk.Button(tabAccount,text="Edit",command=editAccountInfo)
b7 = tk.Button(tabAccount,text="Save",command=saveAccountInfo)

root.mainloop()