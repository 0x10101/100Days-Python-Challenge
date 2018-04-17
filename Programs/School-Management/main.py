#Version 0.2

import tkinter as tk
from tkinter import ttk, messagebox
import database as db
import login_system as ls
import Pmw, string

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

def showRegister():
	#Removing login widgets
	for widget in loginWidgets:
		widget.place_forget()

	#Showing register widgets
	l5.place(x=30,y=30) # Sign up

	showLabels = [l6,l7,l8,l9,l10]
	ypos = 150
	for label in showLabels:
		label.place(x=200,y=ypos)
		ypos += 40

	showEntries = [e3,e4,e5,e6,e7]
	ypos = 150
	for entry in showEntries:
		entry.place(x=370,y=ypos)
		ypos += 40

	b3.place(x=300,y=350,height=50) # Register 
	b4.place(x=500,y=350,height=50) # Show Login




def showLogin():
	#Removing register widgets

	for widget in registerWidgets:
		widget.place_forget()

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

	for widget in loginWidgets:
		widget.place_forget()
	
	#Removing register widgets

	for widget in registerWidgets:
		widget.place_forget()

def logged_in():
	tabControl.add(tabDashboard,text='Dashboard')
	tabControl.add(tabStaff,text='Staff Management')
	tabControl.add(tabClassTypes,text='Class Types')
	tabControl.add(tabClasses,text='Classes')
	tabControl.add(tabStudents,text='Students')
	tabControl.add(tabAccount,text=e1.get())
	tabControl.pack(expand=1,fill='both')

	b5.place(x=700,y=0,width=200,height=20)
	s.configure("TNotebook", borderwidth=1)


def logged_out():
	tabControl.hide(tabDashboard)
	tabControl.hide(tabStaff)
	tabControl.hide(tabClassTypes)
	tabControl.hide(tabClasses)
	tabControl.hide(tabStudents)
	tabControl.hide(tabAccount)
	b5.place_forget()
	s.configure("TNotebook", borderwidth=0)
	showLogin()

def cancelEdit():
	#Removing edit widgets
	cancelEditWidgets = [b7,b8,e8,e9,e10,e11,e12,b8]
	for widget in cancelEditWidgets:
		widget.place_forget()

	#Shows account info
	dbManager.connect()
	account = dbManager.getTableData("accounts","username='{}' and password='{}'".format(e1.get(),e2.get()))
	dbManager.close()
	print(account)
	print(account["Username"],account["Password"])
	tabAccountWidgets(ls.LoginSystem().login(account["Username"],account["Password"]))

def saveAccountInfo(event=None):
	dbManager.connect()
	dbManager.update("accounts","""
							name='{}',
							lastname='{}',
							username='{}',
							password='{}',
							birthday='{}'""".format(e8.get(),e9.get(),e10.get(),e11.get(),e12.get()),
								"username='{}' and password='{}'".format(e1.get(),e2.get()))
	messagebox.showinfo("Successful","Account info have been changed successfully")
	e1_text.set(e10.get())
	e2_text.set(e11.get())
	tabControl.add(tabAccount,text=e1.get())
	cancelEdit()
	dbManager.close()


def editAccountInfo():
	labels_data = [l13_data,l14_data,l15_data,l16_data,l17_data]
	texts = ["First Name:","Last Name:","Username:","Password:","Birthday:"]
	item = 0
	for label_data in labels_data:
		label_data.set(texts[item])
		item += 1


	b6.place_forget()
	b7.place(x=600,y=180,width=100,height=40)
	b8.place(x=500,y=180,width=100,height=40)

	dbManager.connect()

	account = dbManager.getTableData("accounts","username='{}' and password='{}'".format(e1.get(),e2.get()))
	dbManager.close()
	e8_text.set(account["First Name"])
	e9_text.set(account["Last Name"])
	e10_text.set(account["Username"])
	e11_text.set(account["Password"])
	e12_text.set(account["Birthday"])

	entries = [e8,e9,e10,e11,e12]
	ypos = 100
	for entry in entries:
		entry.place(x=275,y=ypos,width=200,height=40)
		ypos += 40


def tabAccountWidgets(accountInf):
	l13_data.set("First Name: {}".format(accountInf["First Name"]))
	l14_data.set("Last Name: {}".format(accountInf["Last Name"]))
	l15_data.set("Username: {}".format(accountInf["Username"]))
	l16_data.set("Password: {}".format(accountInf["Password"]))
	l17_data.set("Birthday: {}".format(accountInf["Birthday"]))

	l12.place(x=15,y=30) 

	#Placing labels dynamically
	labels = [l13,l14,l15,l16,l17]
	ypos = 100
	for label in labels:
		label.place(x=100,y=ypos)
		ypos += 40

	b6.place(x=500,y=180,width=100,height=40)

def loginAttempt(event=None):
	loginSystem = ls.LoginSystem()
	account = loginSystem.login(e1.get(),e2.get())
	if account:
			tabAccountWidgets(account)
			hideLoginRegister()
			logged_in()
	if not account:
		l4.place(x=200,y=380)
		print("username or password not found in database")
	else:
		l4.place_forget()

def createAccount(event=None):
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
				messagebox.showinfo("Successful!","You have successfully signed up!")
				showLogin()
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


accounts_columns = """			
			name TEXT,
			lastname TEXT,
			username TEXT UNIQUE,
			password TEXT,
			birthday TEXT """

classTypes_columns = """ 
			module TEXT UNIQUE,
			difficulty TEXT,
			duration INTEGER """

accounts_columnsList = "name,lastname,username,password,birthday"
classTypes_columns = "module,difficulty,duration"

root = tk.Tk()
root.title("School Management")
root.geometry("{}x{}".format(900,500))

s = ttk.Style()

dbManager = db.Manage("database.db")

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

loginWidgets = [l1,l2,l3,l4,e1,e2,b1,b2]

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

registerWidgets = [l5,l6,l7,l8,l9,l10,l11,e3,e4,e5,e6,e7,b3,b4]

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
e8_text = tk.StringVar()
e8 = tk.Entry(tabAccount,textvariable=e8_text,font=("",20))
e8.bind("<Return>", saveAccountInfo)



l14_data = tk.StringVar()
l14 = tk.Label(tabAccount,textvariable=l14_data,font=("",20))
e9_text = tk.StringVar()
e9 = tk.Entry(tabAccount,textvariable=e9_text,font=("",20))
e9.bind("<Return>", saveAccountInfo)

l15_data = tk.StringVar()
l15 = tk.Label(tabAccount,textvariable=l15_data,font=("",20))
e10_text = tk.StringVar()
e10 = tk.Entry(tabAccount,textvariable=e10_text,font=("",20))
e10.bind("<Return>", saveAccountInfo)

l16_data = tk.StringVar()
l16 = tk.Label(tabAccount,textvariable=l16_data,font=("",20))
e11_text = tk.StringVar()
e11 = tk.Entry(tabAccount,textvariable=e11_text,font=("",20))
e11.bind("<Return>", saveAccountInfo)

l17_data = tk.StringVar()
l17 = tk.Label(tabAccount,textvariable=l17_data,font=("",20))
e12_text = tk.StringVar()
e12 = tk.Entry(tabAccount,textvariable=e12_text,font=("",20))
e8.bind("<Return>", saveAccountInfo)

b6 = tk.Button(tabAccount,text="Edit",command=editAccountInfo)
b7 = tk.Button(tabAccount,text="Save",command=saveAccountInfo)
b8 = tk.Button(tabAccount,text="Cancel",command=cancelEdit)

accountsWidgets = [l12,l13,l14,l15,l16,l17,e8,e9,e10,e11,e12,b6,b7,b8]

###Class types widgets

fixedFont = Pmw.logicalfont('Fixed')
st = Pmw.ScrolledText(tabClassTypes,
        # borderframe = 1,
        labelpos = 'n',
        label_text='Class Types',
        columnheader = 1,
        rowheader = 1,
        rowcolumnheader = 1,
        usehullsize = 1,
        hull_width = 800,
        hull_height = 400,
        text_wrap='none',
	    text_font = fixedFont,
	    Header_font = fixedFont,
	    Header_foreground = 'blue',
	    rowheader_width = 3,
	    rowcolumnheader_width = 3,
        text_padx = 4,
        text_pady = 4,
        Header_padx = 4,
        rowheader_pady = 4,
      )
st.place(x=50,y=10)
columns = 'Module Difficulty Duration'
columns = str.split(columns)

# Create the header for the row headers
st.component('rowcolumnheader').insert('end', 'ID')

# Create the column headers
st.component('columnheader').insert('0.0', "             {}             {}             {}".format(columns[0],columns[1],columns[2]))

dbManager.connect()
dbManager.create_table("ClassTypes",classTypes_columns)
#Testing
#dbManager.insert("ClassTypes",classTypes_columns,("Python","Begginer","6"))
for account in dbManager.getTableData("ClassTypes","module=module"):
	for x in range(len(account)):
		if x == 3:
			st.insert('end', "             " + str(account[x]) + " Months")
		elif x != 0:
			st.insert('end', "             " + str(account[x]))

	st.insert("end","\n")
	st.component('rowheader').insert('end', account[0])
	st.component('rowheader').insert("end","\n")

st.configure(
            text_state = 'disabled',
            Header_state = 'disabled',
        )

dbManager.close()
root.mainloop()