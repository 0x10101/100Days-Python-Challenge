#Version 0.2
import tkinter as tk
from tkinter import ttk, messagebox
try:
	import Tix as tix
except:
	import tix as tix
import database as db
import login_system as ls
import Pmw, string
import topLevel as topL
import time #, pygubu
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

matplotlib.use("TkAgg")


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

	showEntries = [e3,e4,e5,e6]
	ypos = 150
	for entry in showEntries:
		entry.place(x=370,y=ypos)
		ypos += 40

	ypos += 10
	spinBoxDay.place(x=370,y=ypos,height=20,width=50)
	spinBoxMonth.place(x=430,y=ypos,height=20,width=50)
	spinBoxYear.place(x=490,y=ypos,height=20,width=50)

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
	
	updateStats()
	showStats()

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
	cancelEditWidgets = [b7,b8,e8,e9,e10,e11,b8,spinBoxDay,spinBoxMonth,spinBoxYear]
	for widget in cancelEditWidgets:
		widget.place_forget()

	#Shows account info
	dbManager.connect()
	account = dbManager.getTableData("accounts","username='{}' and password='{}'".format(e1.get(),e2.get()))
	dbManager.close()
	tabAccountWidgets(ls.LoginSystem().login(account["Username"],account["Password"]))

def saveAccountInfo(event=None):
	birthday_date = "{}/{}/{}".format(spinBoxDay_data.get(),spinBoxMonth_data.get(),spinBoxYear_data.get())
	dbManager.connect()
	dbManager.update("accounts","""
							name='{}',
							lastname='{}',
							username='{}',
							password='{}',
							birthday='{}'""".format(e8.get(),e9.get(),e10.get(),e11.get(),birthday_date),
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

	entries = [e8,e9,e10,e11]
	ypos = 100
	for entry in entries:
		entry.place(x=275,y=ypos,width=200,height=40)
		ypos += 40

	accountBirthday = str.split(account["Birthday"],"/")
	spinBoxDay_data.set(accountBirthday[0])
	spinBoxMonth_data.set(accountBirthday[1])
	spinBoxYear_data.set(accountBirthday[2])

	ypos += 25
	spinBoxDay.place(x=275,y=ypos,height=30,width=60)
	spinBoxMonth.place(x=275+60,y=ypos,height=30,width=60)
	spinBoxYear.place(x=275+60+60,y=ypos,height=30,width=60)


def tabAccountWidgets(accountInf):
	l13_data.set("First Name: {}".format(accountInf["First Name"].title()))
	l14_data.set("Last Name: {}".format(accountInf["Last Name"].title()))
	l15_data.set("Username: {}".format(accountInf["Username"]))
	l16_data.set("Password: {}".format("*"*(len(accountInf["Password"])-1)))
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
	birthday_date = "{}/{}/{}".format(spinBoxDay_data.get(),spinBoxMonth_data.get(),spinBoxYear_data.get())
	#Testing
	#dbManager.insert("accounts",accounts_columnsList,values)
	if e3.get() and e4.get() and e5.get() and e6.get() and birthday_date:
		if not hasNumbers(e3.get()) and not hasNumbers(e4.get()):
			try:
				values = e3.get(),e4.get(),e5.get(),e6.get(),birthday_date	
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

def refreshSt(scrolledText,table):
	time.sleep(0.5)
	scrolledText.clear()
	dbManager.connect()
	scrolledText.configure(
            text_state = 'normal',
            Header_state = 'normal',
        )
	lastData = []
	data = dbManager.getTableData(table,"id=id")
	for column in data:
		for i in range(len(column)):
			if i != 0:
				scrolledText.insert('end',str(column[i]) + " "*(15 - len(column[i])) +  "|")
		if column == data[-1]:
			lastData = data[-1]
		scrolledText.insert("end","\n")
	scrolledText.component('rowheader').insert('end', lastData[0])
	scrolledText.component('rowheader').insert("end","\n")

	scrolledText.configure(
	            text_state = 'disabled',
	            Header_state = 'disabled',
	        )
	dbManager.close()
          
def fillSt(scrolledText,table,table_columns):
	columns = str.split(table_columns,",")
	columns.reverse()

	# Create the header for the row headers
	scrolledText.component('rowcolumnheader').insert('end', 'ID')

	# Create the column headers
	for column in columns:
		scrolledText.component('columnheader').insert('0.0', "{}".format(column.title()) + " "*(15 - len(column)) + "|")

	dbManager.connect()
	dbManager.create_table(table,table_columns)
	allData = dbManager.getTableData(table,"id=id")
	for data in allData:
		for x in range(len(data)):
			if x != 0:
				scrolledText.insert('end',str(data[x]) + " "*(15 - len(data[x])) +  "|")

		scrolledText.insert("end","\n")
		scrolledText.component('rowheader').insert('end', data[0])
		scrolledText.component('rowheader').insert("end","\n")

	scrolledText.configure(
	            text_state = 'disabled',
	            Header_state = 'disabled',
	        )
def getAddEntries(frame,entriesNeeded):
	e13 = tk.Entry(frame,font=("",20))
	e14 = tk.Entry(frame,font=("",20))
	e15 = tk.Entry(frame,font=("",20))
	e16 = tk.Entry(frame,font=("",20))
	e17 = tk.Entry(frame,font=("",20))
	e18 = tk.Entry(frame,font=("",20))
	e19 = tk.Entry(frame,font=("",20))
	e20 = tk.Entry(frame,font=("",20))

	entries_classesAdd = [e13,e14,e15,e16,e17,e18,e19,e20]
	entries_returned = []
	for i in range(entriesNeeded):
		entries_returned.append(entries_classesAdd[i])
	return entries_returned

def insertValues(toplevel,scrolledText,table,entries,columns,messageText):
	insert = True
	dbManager.connect()
	entries = [entry for entry in tuple(entries)]
	entries_get = []
	for entry in entries:
		entries_get.append(entry.get())
	values = ""
	x = 0
	for entry_get in entries_get:
		if len(entry_get) >= 15:
			insert = False
		if x != 0:
			values += "," + entry_get
		else:
			values += entry_get
		x += 1
	if insert:
		dbManager.insert(table,columns,tuple(str.split(values,",")))
		toplevel.destroy()
		messagebox.showinfo("Successful",messageText)
		refreshSt(scrolledText,table)
	else:
		messagebox.showerror("Error","15 Characters is the limit!")
	dbManager.close()



def addClass(scrolledText,table,columns,titleText,messageText):
	x = 0
	for column in columns:
		if column == "hoursWeek":
			columns[x] = "Hours"
		x += 1
	create = topL.Create()
	top = create.top(root,titleText,h=600)
	entries_classesAdd = getAddEntries(top,len(columns))
	create.title(top,titleText)
	labels = create.top_labels(top,columns,xpos=50)
	create.top_entries(top,labels,entries_classesAdd,columns)
	button = create.top_button(top,lambda: insertValues(top,scrolledText,table,entries_classesAdd,classes_columnsList,messageText),150)
	create.changeGeometry(top)

def updateStats():
	students = dbManager.getTableData("students","id=id")
	studentsNr = 0
	for student in students:
		studentsNr += 1

	classes = dbManager.getTableData("classes","id=id")
	classesNr = 0
	for class_ in classes:
		classesNr += 1

	employees = dbManager.getTableData("employees","id=id")
	employeesNr = 0
	for employee in employees:
		employeesNr += 1

	classTypes = dbManager.getTableData("classTypes","id=id")
	classTypesNr = 0
	for classType in classTypes:
		classTypesNr += 1

	studentsStats.set("Students: {}".format(studentsNr))
	classesStats.set("Classes: {}".format(classesNr))
	employeesStats.set("Employees: {}".format(employeesNr))
	classTypesStats.set("Class Types: {}".format(classTypesNr))

def showStats():
	ypos = 100
	for label in dashboardStats:
		label.configure(font=("",20))
		label.place(x=100,y=ypos)
		ypos += 50



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
			instructor TEXT,
			price INTEGER"""

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
			wage INTEGER CHECK
"""

accounts_columnsList = "name,lastname,username,password,birthday"
classTypes_columnsList = "subject,difficulty,duration"
classes_columnsList = "name,subject,hoursWeek,students,instructor,price"
subjects_columnList = "subject"
students_columnsList = "firstName,lastName,birthday,phone,address"
employees_columnsList = "firstName,lastName,birthday,phone,address,role,classes,wage"

dbManager = db.Manage("database.db")
dbManager.connect()
dbManager.create_table("accounts",accounts_columns)
dbManager.close()


root = tix.Tk()

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


#builder = pygubu.Builder()
#builder.add_from_file("LabelFrame_2.ui")

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

b3 = tk.Button(root,text="Register",font=("",28),command=createAccount)

b4 = tk.Button(root,text="Login",font=("",28),command=showLogin)

spinBoxDay_data = tk.StringVar()
spinBoxDay = tk.Spinbox(root,from_=01, to=31, increment=1, textvariable=spinBoxDay_data,
            validate='all')

spinBoxMonth_data = tk.StringVar()
spinBoxMonth = tk.Spinbox(root,from_=01, to=12, increment=1, textvariable=spinBoxMonth_data,
            validate='all')

spinBoxYear_data = tk.StringVar()
spinBoxYear = tk.Spinbox(root,from_=1980, to=2018, increment=1, textvariable=spinBoxYear_data,
            validate='all')


registerWidgets = [l5,l6,l7,l8,l9,l10,l11,e3,e4,e5,e6,b3,b4,spinBoxDay,spinBoxMonth,spinBoxYear]

showLogin()

####Logged in widgets

##Dashboard 


l18 = tk.Label(tabDashboard,text="Statistics",font=("",30))
l18.place(x=50,y=10)

studentsStats = tk.StringVar()
l19 = tk.Label(tabDashboard,textvariable=studentsStats)

classesStats = tk.StringVar()
l20 = tk.Label(tabDashboard,textvariable=classesStats)

employeesStats = tk.StringVar()
l21 = tk.Label(tabDashboard,textvariable=employeesStats)

classTypesStats = tk.StringVar()
l22 = tk.Label(tabDashboard,textvariable=classTypesStats)

dashboardStats = [l19,l20,l21,l22]

##



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



e8.bind("<Return>", saveAccountInfo)

b6 = tk.Button(tabAccount,text="Edit",command=editAccountInfo)
b7 = tk.Button(tabAccount,text="Save",command=saveAccountInfo)
b8 = tk.Button(tabAccount,text="Cancel",command=cancelEdit)

accountsWidgets = [l12,l13,l14,l15,l16,l17,e8,e9,e10,e11,b6,b7,b8,spinBoxDay,spinBoxMonth,spinBoxYear]


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
columns = 'Subject/Difficulty/Duration/Price'

fillSt(st1,"ClassTypes",classTypes_columnsList)

b9 = tk.Button(tabClassTypes,text="ADD",width=20,height=3,command=lambda: addClass(st1,"ClassTypes",str.split(classTypes_columnsList,","),"Add class type","Successfully added class type!"),)
b9.place(x=100,y=410)

b10 = tk.Button(tabClassTypes,text="EDIT",width=20,height=3)
b10.place(x=350,y=410)

b11 = tk.Button(tabClassTypes,text="DELETE",width=20,height=3)
b11.place(x=600,y=410)

##Classes


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
 

fillSt(st2,"Classes",classes_columnsList)

b12 = tk.Button(tabClasses,text="ADD",width=20,height=3,command=lambda: addClass(st2,"Classes",str.split(classes_columnsList,","),"Add class","Successfully added class!"))
b12.place(x=100,y=410)

b13 = tk.Button(tabClasses,text="EDIT",width=20,height=3)
b13.place(x=350,y=410)

b14 = tk.Button(tabClasses,text="DELETE",width=20,height=3)
b14.place(x=600,y=410)

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
 
fillSt(st3,"Students",students_columnsList)

b15 = tk.Button(tabStudents,text="ADD",width=20,height=3,command=lambda: addClass(st3,"Students",str.split(students_columnsList,","),"Add student","Successfully added student!"))
b15.place(x=100,y=410)

b16 = tk.Button(tabStudents,text="EDIT",width=20,height=3)
b16.place(x=350,y=410)

b17 = tk.Button(tabStudents,text="DELETE",width=20,height=3)
b17.place(x=600,y=410)


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
 

fillSt(st4,"employees",employees_columnsList)

b15 = tk.Button(tabStaff,text="ADD",width=20,height=3,command=lambda: addClass(st4,"employees",str.split(employees_columnsList,","),"Add employee","Successfully added employee!"))
b15.place(x=100,y=410)

b16 = tk.Button(tabStaff,text="EDIT",width=20,height=3)
b16.place(x=350,y=410)

b17 = tk.Button(tabStaff,text="DELETE",width=20,height=3)
b17.place(x=600,y=410)


root.mainloop()