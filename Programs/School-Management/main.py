#Version 0.1

import tkinter as tk
from tkinter import ttk
from database import Manage

def loginAttempt():
	access = False
	dbManager = Manage("database.db") #fileLocation
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
	return access

def showRegister():
	#Removing login widgets
	l1.place_forget() # Sign in
	l2.place_forget() # Username 
	l3.place_forget() # Password 
	l4.place_forget() # The message that is shown when user/pw is wrong

	e1.place_forget() # Entry for username
	e2.place_forget() # Entry for password

	b1.place_forget() # Button for login 
	b2.place_forget() # Button for register

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

	b3.place(x=300,y=350,height=50)
	b4.place(x=500,y=350,height=50)

root = tk.Tk()
root.title("School Management")
root.geometry("{}x{}".format(900,500))

#root.grid_columnconfigure(1, weight=1)
#root.grid_columnconfigure(1, weight=1)


#Login widgets

l1 = tk.Label(root,text="Sign in",font=("",50))
l1.place(x=30,y=30)

l2 = tk.Label(root,text="Username: ",font=("",30))
l2.place(x=130,y=180)

e1 = tk.Entry(root,font=("",20))
e1.place(x=360,y=180,width=300,height=55)

l3 = tk.Label(root,text="Password:",font=("",30))
l3.place(x=135,y=250)

e2 = tk.Entry(root,font=("",20),show="*")
e2.place(x=360,y=250,width=300,height=55)

l4 = tk.Label(root,text="Username or Password is wrond!",font=("",20))

b1 = tk.Button(root,text="Login",font=("",28),command=loginAttempt)
b1.place(x=300,y=330,width=150,height=50)

b2 = tk.Button(root,text="Register",font=("",28),command=showRegister)
b2.place(x=470,y=330,width=160,height=50)

#Register widgets

l5 = tk.Label(root,text="Sign up",font=("",50))

l6 = tk.Label(root,text="First Name: ",font=("",20))

l7 = tk.Label(root,text="Last Name: ",font=("",20))

l8 = tk.Label(root,text="Username: ",font=("",20))

l9 = tk.Label(root,text="Password: ",font=("",20))

l10 = tk.Label(root,text="Birthday: ",font=("",20))

e3 = tk.Entry(root,font=("",20))

e4 = tk.Entry(root,font=("",20))

e5 = tk.Entry(root,font=("",20))

e6 = tk.Entry(root,font=("",20),show="*")

e7 = tk.Entry(root,font=("",20))

b3 = tk.Button(root,text="Register",font=("",28))

b4 = tk.Button(root,text="Login",font=("",28))



root.mainloop()