#Version 0.2

import tkinter as tk
from tkinter import ttk, messagebox
import database as db
import login_system as ls
import Pmw, string
import topLevel as topL
import time


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

def insertClassType(classT):
	dbManager.connect()
	dbManager.insert("ClassTypes",classTypes_columns,("Python","Begginer","6"))
	dbManager.create_table("ClassTypes",classTypes_columns)
	st.configure(
	            text_state = 'normal',
	            Header_state = 'normal',
	        )
	#Testing
	#dbManager.insert("ClassTypes",classTypes_columns,("Python","Begginer","6"))
	for x in range(len(classT)):
		if x == 3:
			st.insert('end', "             " + str(classT[x]) + " Months")
		elif x != 0:
			st.insert('end', "             " + str(classT[x]))

		st.insert("end","\n")
		st.component('rowheader').insert('end', classT[0])
		st.component('rowheader').insert("end","\n")

	st.configure(
	            text_state = 'disabled',
	            Header_state = 'disabled',
	        )
	dbManager.close()



accounts_columns = """			
			name TEXT,
			lastname TEXT,
			username TEXT UNIQUE,
			password TEXT,
			birthday TEXT """

classTypes_columns = """ 
			subject TEXT UNIQUE,
			difficulty TEXT,
			duration INTEGER """

classes_columns = """
			name TEXT UNIQUE,
			subject TEXT,
			hoursWeek INTEGER,
			students INTEGER,
			instructor TEXT"""

subjects_column = "subject TEXT UNIQUE"

students_columns = """
			firstName TEXT,
			lastName TEXT,
			birthday TEXT,
			phone INTEGER,
			address TEXT
"""

employees_columns = """
			firstName TEXT,
			lastName TEXT,
			birthday TEXT,
			phone INTEGER,
			address TEXT,
			role TEXT,
			classes INTEGER,
			wage INTEGER
"""

accounts_columnsList = "name,lastname,username,password,birthday"
classTypes_columnsList = "subject,difficulty,duration"
classes_columnsList = "name,subject,hoursWeek,students,instructor"
subjects_columnList = "subject"
students_columnsList = "firstName,lastName,birthday,phone,address"
employees = "firstName,lastName,birthday,phone,address,role,classes,wage"

dbManager = db.Manage("database.db")
dbManager.connect()
dbManager.create_table("accounts",accounts_columns)
dbManager.close()


root = tk.Tk()
root.title("School Management")
w = 900 # width for the Tk root
h = 500 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

s = ttk.Style()

dbManager = db.Manage("database.db")
createTop = topL.Create()

entriesList = []

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
st1 = Pmw.ScrolledText(tabClassTypes,
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
st1.place(x=50,y=10)
columns = 'Subject Difficulty Duration'
columns = str.split(columns)

# Create the header for the row headers
st1.component('rowcolumnheader').insert('end', 'ID')

# Create the column headers
st1.component('columnheader').insert('0.0', "     {}     {}     {}".format(columns[0],columns[1],columns[2]))

dbManager.connect()
dbManager.create_table("ClassTypes",classTypes_columns)
#Testing
#dbManager.insert("ClassTypes",classTypes_columns,("Python","Begginer","6"))
for classType in dbManager.getTableData("ClassTypes","id=id"):
	for x in range(len(classType)):
		if x == 3:
			st1.insert('end', "     " + str(classType[x]) + " Months")
		elif x != 0:
			st1.insert('end', "     " + str(classType[x]))

	st1.insert("end","\n")
	st1.component('rowheader').insert('end', classType[0])
	st1.component('rowheader').insert("end","\n")

st1.configure(
            text_state = 'disabled',
            Header_state = 'disabled',
        )


b9 = tk.Button(tabClassTypes,text="ADD",width=20,height=3,command=lambda: addTop.top_labels(addTop))
b9.place(x=100,y=410)

b10 = tk.Button(tabClassTypes,text="EDIT",width=20,height=3)
b10.place(x=350,y=410)

b11 = tk.Button(tabClassTypes,text="DELETE",width=20,height=3)
b11.place(x=600,y=410)



###Classes widgets

# Classes add toplevel widgets

## Entries that are not used in main.py
def getAddEntries(frame):
	e13 = tk.Entry(frame,font=("",20))
	e14 = tk.Entry(frame,font=("",20))
	e15 = tk.Entry(frame,font=("",20))
	e16 = tk.Entry(frame,font=("",20))
	e17 = tk.Entry(frame,font=("",20))
	entries_classesAdd = [e13,e14,e15,e16,e17]
	return entries_classesAdd
####




##


def insertValues(table,entries):
	dbManager.connect()

	dbManager.insert(table,classes_columnsList,(entries[0].get(),entries[1].get(),entries[2].get(),
														entries[3].get(),entries[4].get()))
	dbManager.close()
	refreshSt2()


def addClass(columns):
	x = 0
	for column in columns:
		if column == "hoursWeek":
			columns[x] = "Hours"
		x += 1
	print(columns)
	create = topL.Create()
	top = create.top(root,"Add Class",h=600)
	entries_classesAdd = getAddEntries(top)
	create.title(top,"Add Class")
	create.top_labels(top,columns,xpos=50)
	print(entries_classesAdd)
	create.top_entries(top,entries_classesAdd,columns)
	x = 0
	columnsText = ""
	for column in columns:
		if column == "Hours":
			columns[x] = "hoursWeek"
		if x != 0:
			columnsText += "," + column
		else:
			columnsText += column
		x += 1
	columns = columnsText

	button = create.top_button(top,lambda: insertValues("Classes",entries_classesAdd),400,400)



st2 = Pmw.ScrolledText(tabClasses,
        # borderframe = 1,
        labelpos = 'n',
        label_text='Classes',
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
st2.place(x=50,y=10)
 
columns2 = 'Name/Subject/Hours per Week/Students/Instructor Name'
columns2 = str.split(columns2,"/")
print(columns2)

st2.component('rowcolumnheader').insert('end', 'ID')
#st2.component('columnheader').insert("0.0","             {}             {}             {}".format(columns2[0],columns2[1],columns2[2]))
for item in columns2:
	st2.component('columnheader').insert("0.0","{}     ".format(item))

dbManager.connect()
dbManager.create_table("Classes",classes_columns)

#Testing
#dbManager.insert("Classes",classes_columnsList,("CL-13","Java","25"))
for Class in dbManager.getTableData("Classes","id=id"):
	for x in range(len(Class)):
		if x != 0:
			st2.insert('end', "     {}".format(str(Class[x])))
	st2.insert("end","\n")
	st2.component('rowheader').insert('end', Class[0])
	st2.component('rowheader').insert("end","\n")

st2.configure(
            text_state = 'disabled',
            Header_state = 'disabled',
        )

b12 = tk.Button(tabClasses,text="ADD",width=20,height=3,command=lambda: addClass(str.split(classes_columnsList,",")))
b12.place(x=100,y=410)

b13 = tk.Button(tabClasses,text="EDIT",width=20,height=3)
b13.place(x=350,y=410)

b14 = tk.Button(tabClasses,text="DELETE",width=20,height=3)
b14.place(x=600,y=410)

def refreshSt2():
	time.sleep(1)
	st2.clear()
	dbManager.connect()
	st2.configure(
            text_state = 'normal',
            Header_state = 'normal',
        )
	lastClass = []
	classes = dbManager.getTableData("Classes","id=id")
	for Class in classes:
		for data in range(len(Class)):
			if data != 0:
				st2.insert('end', "     {}".format(str(Class[data])))
		if Class == classes[-1]:
			lastClass = Class
		st2.insert("end","\n")

	st2.component('rowheader').insert('end', lastClass[0])
	st2.component('rowheader').insert("end","\n")

	st2.configure(
	            text_state = 'disabled',
	            Header_state = 'disabled',
	        )
	dbManager.close()

def refreshSt3():
	pass
### Students widgets

st3 = Pmw.ScrolledText(tabStudents,
        # borderframe = 1,
        labelpos = 'n',
        label_text='Students',
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
st3.place(x=50,y=10)
 
columns3 = 'First Name/Last Name/Birthday/Phone/Address'
columns3 = str.split(columns3,"/")
print(columns3)

st3.component('rowcolumnheader').insert('end', 'ID')
#st2.component('columnheader').insert("0.0","             {}             {}             {}".format(columns2[0],columns2[1],columns2[2]))
for item in columns3:
	st3.component('columnheader').insert("0.0","{}     ".format(item))

dbManager.connect()
dbManager.create_table("Students",students_columns)

#Testing
#dbManager.insert("Classes",classes_columnsList,("CL-13","Java","25"))
for student in dbManager.getTableData("Students","id=id"):
	for x in range(len(student)):
		if x != 0:
			st2.insert('end', "     {}".format(str(student[x])))
	st3.insert("end","\n")
	st3.component('rowheader').insert('end', student[0])
	st3.component('rowheader').insert("end","\n")

st3.configure(
            text_state = 'disabled',
            Header_state = 'disabled',
        )

b15 = tk.Button(tabStudents,text="ADD",width=20,height=3)
b15.place(x=100,y=410)

b16 = tk.Button(tabStudents,text="EDIT",width=20,height=3)
b16.place(x=350,y=410)

b17 = tk.Button(tabStudents,text="DELETE",width=20,height=3)
b17.place(x=600,y=410)
dbManager.close()
### Staff Management

st4 = Pmw.ScrolledText(tabStaff,
        # borderframe = 1,
        labelpos = 'n',
        label_text='Employees',
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
st4.place(x=50,y=10)
 
columns4 = 'First Name/Last Name/Birthday/Phone/Address'
columns4 = str.split(columns4,"/")
print(columns4)

st4.component('rowcolumnheader').insert('end', 'ID')
#st2.component('columnheader').insert("0.0","             {}             {}             {}".format(columns2[0],columns2[1],columns2[2]))
for item in columns4:
	st4.component('columnheader').insert("0.0","{}     ".format(item))

dbManager.connect()
dbManager.create_table("employees",employees_columns)

#Testing
#dbManager.insert("Classes",classes_columnsList,("CL-13","Java","25"))
for employee in dbManager.getTableData("employees","id=id"):
	for x in range(len(employee)):
		if x != 0:
			st2.insert('end', "     {}".format(str(employee[x])))
	st4.insert("end","\n")
	st4.component('rowheader').insert('end', employee[0])
	st4.component('rowheader').insert("end","\n")

st4.configure(
            text_state = 'disabled',
            Header_state = 'disabled',
        )

b15 = tk.Button(tabStaff,text="ADD",width=20,height=3)
b15.place(x=100,y=410)

b16 = tk.Button(tabStaff,text="EDIT",width=20,height=3)
b16.place(x=350,y=410)

b17 = tk.Button(tabStaff,text="DELETE",width=20,height=3)
b17.place(x=600,y=410)


dbManager.close()
root.mainloop()