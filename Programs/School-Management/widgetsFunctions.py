import database as db
import topLevel as topL
import tkinter as tk
from tkinter import ttk
import time 

def showRegister(loginWidgets,registerWidgets):
	#Removing login widgets
	for widget in loginWidgets:
		try:
			loginWidgets[widget].place_forget()
		except:
			print("{} is not a widget".format(loginWidgets[widget]))

	#Showing register widgets
	registerWidgets["label5"].place(x=30,y=30) # Sign up

	showLabels = [registerWidgets["label6"],registerWidgets["label7"],
					registerWidgets["label8"],registerWidgets["label9"],
						registerWidgets["label10"]]
	ypos = 150
	for label in showLabels:
		label.place(x=200,y=ypos)
		ypos += 40

	showEntries = [registerWidgets["entry3"],registerWidgets["entry4"],
					registerWidgets["entry5"],registerWidgets["entry6"]]
	ypos = 150
	for entry in showEntries:
		entry.place(x=370,y=ypos)
		ypos += 40

	ypos += 10
	registerWidgets["spinBoxDay"].place(x=370,y=ypos,height=20,width=50)
	registerWidgets["spinBoxMonth"].place(x=430,y=ypos,height=20,width=50)
	registerWidgets["spinBoxYear"].place(x=490,y=ypos,height=20,width=50)

	registerWidgets["button3"].place(x=300,y=350,height=50) # Register 
	registerWidgets["button4"].place(x=500,y=350,height=50) # Show Login




def showLogin(registerWidgets,loginWidgets):
	#Removing register widgets
	for key in registerWidgets:
		try:
			registerWidgets[key].place_forget()
		except:
			print("{} is not a widget".format(registerWidgets[key]))
	#Showing login widgets
	loginWidgets["label1"].place(x=30,y=30) # Sign in
	loginWidgets["label2"].place(x=130,y=180) # Username 
	loginWidgets["label3"].place(x=135,y=250) # Password 

	loginWidgets["entry1text"].set("")
	loginWidgets["entry2text"].set("")
	loginWidgets["entry1"].place(x=360,y=180,width=300,height=55) # Entry for username
	loginWidgets["entry2"].place(x=360,y=250,width=300,height=55) # Entry for password

	loginWidgets["button1"].place(x=300,y=330,width=150,height=50) # Button for login 
	loginWidgets["button2"].place(x=470,y=330,width=160,height=50) # Button for show register

def hideLoginRegister(registerWidgets,loginWidgets):
	#Removing login widgets

	for widget in loginWidgets:
		try:
			loginWidgets[widget].place_forget()
		except:
			print("{} isn't a widget".format(widget))
	
	#Removing register widgets

	for widget in registerWidgets:
		try:
			registerWidgets[widget].place_forget()
		except:
			print("{} isn't a widget".format(widget))

def logged_in(tabControl,tabs,b5,s,username,dashboardData,dashboardStats):
	tabControl.add(tabs["tabDashboard"],text='Dashboard')
	tabControl.add(tabs["tabStaff"],text='Staff Management')
	tabControl.add(tabs["tabClassTypes"],text='Class Types')
	tabControl.add(tabs["tabClasses"],text='Classes')
	tabControl.add(tabs["tabStudents"],text='Students')
	tabControl.add(tabs["tabAccount"],text=username)
	tabControl.pack(expand=1,fill='both')

	updateStats(dashboardData)
	showStats(dashboardStats)

	b5.place(x=700,y=0,width=200,height=20)
	s.configure("TNotebook", borderwidth=1)


def logged_out(tabC,tabs,button5,style,registerWidgets,loginWidgets):
	for tab in tabs:
		tabC.hide(tab)
	button5.place_forget()
	style.configure("TNotebook", borderwidth=0)
	showLogin(registerWidgets,loginWidgets)

def getAddEntries(frame,entriesNeeded):
	e13_data = tk.StringVar()
	e13 = tk.Entry(frame,font=("",20),textvariable=e13_data)

	e14_data = tk.StringVar()
	e14 = tk.Entry(frame,font=("",20),textvariable=e14_data)

	e15_data = tk.StringVar()
	e15 = tk.Entry(frame,font=("",20),textvariable=e15_data)

	e16_data = tk.StringVar()
	e16 = tk.Entry(frame,font=("",20),textvariable=e16_data)

	e17_data = tk.StringVar()
	e17 = tk.Entry(frame,font=("",20),textvariable=e17_data)

	e18_data = tk.StringVar()
	e18 = tk.Entry(frame,font=("",20),textvariable=e18_data)

	e19_data = tk.StringVar()
	e19 = tk.Entry(frame,font=("",20),textvariable=e19_data)

	e20_data = tk.StringVar()
	e20 = tk.Entry(frame,font=("",20),textvariable=e20_data)

	entries_classesAdd = [e13,e14,e15,e16,e17,e18,e19,e20]
	entries_textvariable = [e13_data,e14_data,e15_data,e16_data,e17_data,e18_data,
										e19_data,e20_data]
	entries_returned = []
	entries_textvariablesReturned = []
	for i in range(entriesNeeded):
		entries_returned.append(entries_classesAdd[i])
		entries_textvariablesReturned.append(entries_textvariable[i])
	
	return [entries_returned,entries_textvariablesReturned]


def tabAccountWidgets(accountsWidgets,accountsData,accountInf):
	accountsData["l13_data"].set("First Name: {}".format(accountInf["First Name"].title()))
	accountsData["l14_data"].set("Last Name: {}".format(accountInf["Last Name"].title()))
	accountsData["l15_data"].set("Username: {}".format(accountInf["Username"]))
	accountsData["l16_data"].set("Password: {}".format("*"*(len(accountInf["Password"])-1)))
	accountsData["l17_data"].set("Birthday: {}".format(accountInf["Birthday"]))

	accountsWidgets["label12"].place(x=15,y=30) 

	#Placing labels dynamically
	labels = [accountsWidgets["label13"],
			  accountsWidgets["label14"],
			  accountsWidgets["label15"],
			  accountsWidgets["label16"],
			  accountsWidgets["label17"]]
	ypos = 100
	for label in labels:
		label.place(x=100,y=ypos)
		ypos += 40

	accountsWidgets["button6"].place(x=500,y=180,width=100,height=40)


def showStats(labels):
	labels["label19"].place(x=100,y=100)
	labels["label21"].place(x=100,y=150)
	labels["label20"].place(x=100,y=200)
	labels["label22"].place(x=100,y=250)
	labels["label23"].place(x=350,y=300/2-30)
	labels["label24"].place(x=350,y=300/2+10)
	labels["label25"].place(x=350,y=300/2+50)

def updateStats(data):
	dbManager = db.Manage("database.db")
	dbManager.connect()

	students = dbManager.getTableData("Students","id=id")
	classes = dbManager.getTableData("Classes","id=id")
	employees = dbManager.getTableData("employees","id=id")
	classTypes = dbManager.getTableData("ClassTypes","id=id")

	dbManager.close()


	incomeCalc = 0
	for class_ in classes:
		try:
			incomeCalc += int(class_[6])
		except:
			print("{} isn't integer/float".format(class_[6]))

	outcomeCalc = 0
	for employee in employees:
		try:
			outcomeCalc += int(employee[8])
		except:
			print("{} isn't integer/float".format(employee[8]))



	
	data["studentsStats"].set("Students: {}".format(len(students)))
	data["classesStats"].set("Classes: {}".format(len(classes)))
	data["employeesStats"].set("Employees: {}".format(len(employees)))
	data["classTypesStats"].set("Class Types: {}".format(len(classTypes)))
	data["income"].set("Income: +{}$".format(incomeCalc))
	data["outcome"].set("Outcome: -{}$".format(outcomeCalc))
	data["profit"].set("Profit: {}$".format(incomeCalc - outcomeCalc))


def addToplevel(frame,treeView,table,columns,titleText,messageText,dashboardData,tabDashboard,messagebox):
	x = 0
	print(columns)
	create = topL.Create()	
	top = create.top(frame,titleText,h=600)
	entries_classesAdd = getAddEntries(top,len(columns))
	create.title(top,titleText)
	labels = create.top_labels(top,columns,xpos=50)
	create.top_entries(top,labels,entries_classesAdd,columns)

	x = 0
	columnsText = ""
	for column in columns:
		if x != 0:
			columnsText += "," + column
		else:
			columnsText += column
		x += 1
	columns = columnsText

	button_func = lambda: db.insertValues(top,table,columns,
					entries_classesAdd,treeView,messageText,messagebox,dashboardData)
	button = create.top_button(top,button_func,150)
	create.changeGeometry(top)
	updateStats(dashboardData)
	#logged_in()
	tabDashboard.update()

