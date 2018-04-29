#Version 0.2
import tkinter as tk
from tkinter import ttk, messagebox
#try:
#	import Tix as tix
#except:
#	import tix as tix
import database as db
import login_system as ls
import Pmw, string
import topLevel as topL
import matplotlib
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure
import widgetsFunctions as widgetsF
import accountSystem as accountS


def login(event=None):
	loginS = ls.LoginSystem()
	account = loginS.login(e1.get(),e2.get())
	if account:
			widgetsF.tabAccountWidgets(accountsWidgets,accountsData,account)
			widgetsF.hideLoginRegister(registerWidgets,loginWidgets)
			widgetsF.logged_in(tabControl,tabs,b5,s,e1.get(),dashboardData,dashboardStats)
	if not account:
		l4.place(x=200,y=380)
		print("username or password not found in database")
	else:
		l4.place_forget()
		
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

tabs = {
			"tabDashboard":tabDashboard,
			"tabStaff":tabStaff,
			"tabClassTypes":tabClassTypes,
			"tabClasses":tabClasses,
			"tabStudents":tabStudents,
			"tabAccount":tabAccount,
}

#tabDashboard.bind("<<NotebookTabChanged>>", 
 #      lambda event: event.widget.winfo_children()[event.widget.index("current")].update())

#Login widgets

l1 = tk.Label(root,text="Sign in",font=("",50))

l2 = tk.Label(root,text="Username: ",font=("",30))

e1_text = tk.StringVar()
e1 = tk.Entry(root,textvariable=e1_text,font=("",20))
e1.bind("<Return>", login)

l3 = tk.Label(root,text="Password:",font=("",30))

e2_text = tk.StringVar()
e2 = tk.Entry(root,textvariable=e2_text,font=("",20),show="*")
e2.bind("<Return>", login)

l4 = tk.Label(root,text="Username or Password is wrong!",font=("",20))

b1 = tk.Button(root,text="Login",font=("",28),command=login)
b2 = tk.Button(root,text="Register",font=("",28),command=lambda: widgetsF.showRegister(loginWidgets,registerWidgets))

loginWidgets = {"label1":l1,
				"label2":l2,
				"label3":l3,
				"label4":l4,
				"entry1":e1,
				"entry1text":e1_text,
				"entry2":e2,
				"entry2text":e2_text,
				"button1":b1,
				"button2":b2}

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
e3.bind("<Return>", accountS.createAccount)
 
e4 = tk.Entry(root,font=("",20))
e4.bind("<Return>", accountS.createAccount)

e5 = tk.Entry(root,font=("",20))
e5.bind("<Return>", accountS.createAccount)

e6 = tk.Entry(root,font=("",20),show="*")
e6.bind("<Return>", accountS.createAccount)

b3 = tk.Button(root,text="Register",font=("",28),command=lambda: accountS.createAccount(loginWidgets,registerWidgets,registerData,messagebox))

b4 = tk.Button(root,text="Login",font=("",28),command=lambda: widgetsF.showLogin(registerWidgets,loginWidgets))

spinBoxDay_data = tk.StringVar()
spinBoxDay = tk.Spinbox(root,from_=01, to=31, increment=1, textvariable=spinBoxDay_data,
            validate='all')

spinBoxMonth_data = tk.StringVar()
spinBoxMonth = tk.Spinbox(root,from_=01, to=12, increment=1, textvariable=spinBoxMonth_data,
            validate='all')

spinBoxYear_data = tk.StringVar()

spinBoxYear = tk.Spinbox(root,from_=1980, to=2018, increment=1, textvariable=spinBoxYear_data,
            validate='all')

registerWidgets = {"label5":l5,
				   "label6":l6,
				   "label7":l7,
				   "label8":l8,
				   "label9":l9,
				   "label10":l10,
				   "label11":l11,
				   "entry3":e3,
				   "entry4":e4,
				   "entry5":e5,
				   "entry6":e6,
				   "button3":b3,
				   "button4":b4,
				   "spinBoxDay":spinBoxDay,
				   "spinBoxMonth":spinBoxMonth,
				   "spinBoxYear":spinBoxYear}
registerData = {
				   "errorMessage":errorMessage,
				   "spinBoxDay_data":spinBoxDay_data,
				   "spinBoxMonth_data":spinBoxMonth_data,
				   "spinBoxYear_data":spinBoxYear_data
				   }

widgetsF.showLogin(registerWidgets,loginWidgets)

####Logged in widgets

##Dashboard 


l18 = tk.Label(tabDashboard,text="Statistics",font=("",30))
l18.place(x=50,y=10)

studentsStats = tk.StringVar()
l19 = tk.Label(tabDashboard,textvariable=studentsStats,font=("",20))

classesStats = tk.StringVar()
l20 = tk.Label(tabDashboard,textvariable=classesStats,font=("",20))

employeesStats = tk.StringVar()
l21 = tk.Label(tabDashboard,textvariable=employeesStats,font=("",20))

classTypesStats = tk.StringVar()
l22 = tk.Label(tabDashboard,textvariable=classTypesStats,font=("",20))

income = tk.StringVar()
l23 = tk.Label(tabDashboard,textvariable=income,font=("",20))

outcome = tk.StringVar()
l24 = tk.Label(tabDashboard,textvariable=outcome,font=("",20))

profit = tk.StringVar()
l25 = tk.Label(tabDashboard,textvariable=profit,font=("",20))


dashboardStats = {"label19":l19,
				  "label21":l21,
				  "label20":l20,
				  "label22":l22,
				  "label23":l23,
				  "label24":l24,
				  "label25":l25}
dashboardData = {
				  "studentsStats":studentsStats,
				  "classesStats":classesStats,
				  "employeesStats":employeesStats,
				  "classTypesStats":classTypesStats,
				  "income":income,
				  "outcome":outcome,
				  "profit":profit,
}

##


tabsList = [tabDashboard,tabClasses,tabAccount,tabStudents,tabStaff,tabClassTypes]
# Buttons near notebook widgets
b5 = tk.Button(root,text="Log out!",command=lambda: widgetsF.logged_out(tabControl,tabsList,b5,s,registerWidgets,loginWidgets))

#b6_user = tk.StringVar()
#b6 = tk.Button(root,textvariable=b6_user,command=showAccountInfo)

#Accounts widgets
l12 = tk.Label(tabAccount,text="Account Information",font=("",30))

l13_data = tk.StringVar()
l13 = tk.Label(tabAccount,textvariable=l13_data,font=("",20))
e8_text = tk.StringVar()
e8 = tk.Entry(tabAccount,textvariable=e8_text,font=("",20))
e8.bind("<Return>", accountS.saveAccountInfo)



l14_data = tk.StringVar()
l14 = tk.Label(tabAccount,textvariable=l14_data,font=("",20))
e9_text = tk.StringVar()
e9 = tk.Entry(tabAccount,textvariable=e9_text,font=("",20))
e9.bind("<Return>", accountS.saveAccountInfo)

l15_data = tk.StringVar()
l15 = tk.Label(tabAccount,textvariable=l15_data,font=("",20))
e10_text = tk.StringVar()
e10 = tk.Entry(tabAccount,textvariable=e10_text,font=("",20))
e10.bind("<Return>", accountS.saveAccountInfo)

l16_data = tk.StringVar()
l16 = tk.Label(tabAccount,textvariable=l16_data,font=("",20))
e11_text = tk.StringVar()
e11 = tk.Entry(tabAccount,textvariable=e11_text,font=("",20))
e11.bind("<Return>", accountS.saveAccountInfo)

l17_data = tk.StringVar()
l17 = tk.Label(tabAccount,textvariable=l17_data,font=("",20))


accountsData = {
				   "l13_data":l13_data,
				   "e8_text":e8_text,
				   "l14_data":l14_data,
				   "e9_text":e9_text,
				   "l15_data":l15_data,
				   "e10_text":e10_text,
				   "e11_text":e10_text,
				   "l16_data":l16_data,
				   "l17_data":l17_data,
				   "spinBoxDay_data":spinBoxDay_data,
				   "spinBoxMonth_data":spinBoxMonth_data,
				   "spinBoxYear_data":spinBoxYear_data
}

b6 = tk.Button(tabAccount,text="Edit",command=lambda : accountS.editAccountInfo(accountsData,accountsWidgets,e1,e2))
b7 = tk.Button(tabAccount,text="Save",command=lambda: accountS.saveAccountInfo(tabControl,tabAccount,accountsWidgets,accountsData,e1,e1_text,e2,e2_text,messagebox))
b8 = tk.Button(tabAccount,text="Cancel",command=lambda: accountS.cancelEdit(accountsWidgets,accountsData,e1,e2))

accountsWidgets = {"label12":l12,
				   "label13":l13,
				   "label14":l14,
				   "label15":l15,
				   "label16":l16,
				   "label17":l17,
				   "entry8":e8,
				   "entry9":e9,
				   "entry10":e10,
				   "entry11":e11,
				   "button6":b6,
				   "button7":b7,
				   "button8":b8,
				   "spinBoxDay":spinBoxDay,
				   "spinBoxMonth":spinBoxMonth,
				   "spinBoxYear":spinBoxYear}

###Class types widgets



fixedFont = Pmw.logicalfont('Fixed')

treeClassType = widgetsF.createTreeView(tabClassTypes,"ClassTypes",["ID"] + str.split(db.classTypes_columnsList,","))
#widgetsF.fillSt(st1,"ClassTypes",db.classTypes_columnsList)


b9 = tk.Button(tabClassTypes,text="ADD",width=20,height=3,command=lambda: widgetsF.addToplevel(root,treeClassType,"ClassTypes",str.split(db.classTypes_columnsList,","),"Add class type","Successfully added class type!",dashboardData,tabDashboard,messagebox))
b9.place(x=100,y=410)

b10 = tk.Button(tabClassTypes,text="EDIT",width=20,height=3)
b10.place(x=350,y=410)

b11 = tk.Button(tabClassTypes,text="DELETE",width=20,height=3)
b11.place(x=600,y=410)

##Classes

 
treeClasses = widgetsF.createTreeView(tabClasses,"Classes",["ID"] + str.split(db.classes_columnsList,","))



b12 = tk.Button(tabClasses,text="ADD",width=20,height=3,command=lambda: widgetsF.addToplevel(root,treeClasses,"Classes",str.split(db.classes_columnsList,","),"Add class","Successfully added class!",dashboardData,tabDashboard,messagebox))
b12.place(x=100,y=410)

b13 = tk.Button(tabClasses,text="EDIT",width=20,height=3)
b13.place(x=350,y=410)

b14 = tk.Button(tabClasses,text="DELETE",width=20,height=3)
b14.place(x=600,y=410)

### Students widgets

treeStudents = widgetsF.createTreeView(tabStudents,"Students",["ID"] + str.split(db.students_columnsList,","))


b15 = tk.Button(tabStudents,text="ADD",width=20,height=3,command=lambda: widgetsF.addToplevel(root,treeStudents,"Students",str.split(db.students_columnsList,","),"Add student","Successfully added student!",dashboardData,tabDashboard,messagebox))
b15.place(x=100,y=410)

b16 = tk.Button(tabStudents,text="EDIT",width=20,height=3)
b16.place(x=350,y=410)

b17 = tk.Button(tabStudents,text="DELETE",width=20,height=3)
b17.place(x=600,y=410)


### Staff Management

treeStaff = widgetsF.createTreeView(tabStaff,"employees",["ID"] + str.split(db.employees_columnsList,","))

b15 = tk.Button(tabStaff,text="ADD",width=20,height=3,command=lambda: widgetsF.addToplevel(root,treeStaff,"employees",str.split(db.employees_columnsList,","),"Add employee","Successfully added employee!",dashboardData,tabDashboard,messagebox))
b15.place(x=100,y=410)

b16 = tk.Button(tabStaff,text="EDIT",width=20,height=3)
b16.place(x=350,y=410)

b17 = tk.Button(tabStaff,text="DELETE",width=20,height=3)
b17.place(x=600,y=410)

#tabDashboard.after_idle(updateStats)
root.mainloop()