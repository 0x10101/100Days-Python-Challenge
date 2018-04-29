import database as db
import widgetsFunctions as widgetsF
from login_system import LoginSystem
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

def cancelEdit(accountsWidgets,accountsData,user,passw):
	#Removing edit widgets
	cancelEditWidgets = [accountsWidgets["button7"],accountsWidgets["button8"],
						accountsWidgets["entry8"],accountsWidgets["entry9"],
						accountsWidgets["entry10"],accountsWidgets["entry11"],
						accountsWidgets["button8"],accountsWidgets["spinBoxDay"],
						accountsWidgets["spinBoxMonth"],accountsWidgets["spinBoxYear"]]
	for widget in cancelEditWidgets:
		widget.place_forget()
	dbManager = db.Manage("database.db")
	#Shows account info
	dbManager.connect()
	account = dbManager.getTableData("accounts","username='{}' and password='{}'".format(user.get(),passw.get()))
	dbManager.close()
	widgetsF.tabAccountWidgets(accountsWidgets,accountsData,account) #LoginSystem().login(account["Username"],account["Password"])

def saveAccountInfo(tabControl,tabAcc,accountsWidgets,accountsData,e1,e1text,e2,e2text,messagebox,event=None):
	dbManager = db.Manage("database.db")
	birthday_date = "{}/{}/{}".format(accountsData["spinBoxDay_data"].get(),accountsData["spinBoxMonth_data"].get(),
									  		accountsData["spinBoxYear_data"].get())
	dbManager.connect()
	dbManager.update("accounts","""
							name='{}',
							lastname='{}',
							username='{}',
							password='{}',
							birthday='{}'""".format(accountsWidgets["entry8"].get(),accountsWidgets["entry9"].get(),
													accountsWidgets["entry10"].get(),accountsWidgets["entry11"].get(),birthday_date),
								"username='{}' and password='{}'".format(e1.get(),e2.get()))
	messagebox.showinfo("Successful","Account info have been changed successfully")
	e1text.set(accountsWidgets["entry10"].get())
	e2text.set(accountsWidgets["entry11"].get())
	tabControl.add(tabAcc,text=e1.get())
	cancelEdit(accountsWidgets,accountsData,e1,e2)
	dbManager.close()


def editAccountInfo(data,accountsWidgets,user,passw):
	labels_data = [data["l13_data"],data["l14_data"],
					data["l15_data"],data["l16_data"],data["l17_data"]]
	texts = ["First Name:","Last Name:","Username:","Password:","Birthday:"]
	item = 0
	for label_data in labels_data:
		label_data.set(texts[item])
		item += 1


	accountsWidgets["button6"].place_forget()
	accountsWidgets["button7"].place(x=600,y=180,width=100,height=40)
	accountsWidgets["button8"].place(x=500,y=180,width=100,height=40)

	dbManager = db.Manage("database.db")
	dbManager.connect()

	account = dbManager.getTableData("accounts","username='{}' and password='{}'".format(user.get(),passw.get()))
	dbManager.close()
	print(data["e10_text"].get())
	data["e8_text"].set(account["First Name"])
	data["e9_text"].set(account["Last Name"])
	data["e10_text"].set(account["Username"])
	data["e11_text"].set(account["Password"])

	entries = [accountsWidgets["entry8"],accountsWidgets["entry9"],
				accountsWidgets["entry10"],accountsWidgets["entry11"]]
	ypos = 100
	for entry in entries:
		entry.place(x=275,y=ypos,width=200,height=40)
		ypos += 40

	accountBirthday = str.split(account["Birthday"],"/")
	data["spinBoxDay_data"].set(accountBirthday[0])
	data["spinBoxMonth_data"].set(accountBirthday[1])
	data["spinBoxYear_data"].set(accountBirthday[2])

	ypos += 25
	accountsWidgets["spinBoxDay"].place(x=275,y=ypos,height=30,width=60)
	accountsWidgets["spinBoxMonth"].place(x=275+60,y=ypos,height=30,width=60)
	accountsWidgets["spinBoxYear"].place(x=275+60+60,y=ypos,height=30,width=60)

def createAccount(loginWidgets,registerWidgets,registerData,messagebox,event=None):
	dbManager = db.Manage("database.db")
	dbManager.connect()
	dbManager.create_table("accounts",db.accounts_columns)
	birthday_date = "{}/{}/{}".format(registerData["spinBoxDay_data"].get(),registerData["spinBoxMonth_data"].get(),
				registerData["spinBoxYear_data"].get())
	#Testing
	#dbManager.insert("accounts",accounts_columnsList,values)
	if registerWidgets["entry3"].get() and registerWidgets["entry4"].get() and registerWidgets["entry5"].get() and registerWidgets["entry6"].get() and birthday_date:
		if not hasNumbers(registerWidgets["entry3"].get()) and not hasNumbers(registerWidgets["entry4"].get()):
			try:
				values = registerWidgets["entry3"].get(),registerWidgets["entry4"].get(),registerWidgets["entry5"].get(),registerWidgets["entry6"].get(),birthday_date	
				dbManager.insert("accounts",db.accounts_columnsList,values)
				registerWidgets["label11"].place_forget()
				messagebox.showinfo("Successful!","You have successfully signed up!")
				widgetsF.showLogin(registerWidgets,loginWidgets)
			except:
				registerData["errorMessage"].set("Username is already taken!")
				registerWidgets["label11"].place(x=270,y=400)
				raise
		else:
			registerData["errorMessage"].set("First Name/Last Name can't contain numbers!")
			registerWidgets["label11"].place(x=150,y=400)
	else:
		registerData["errorMessage"].set("Please complete all the fields!")
		registerWidgets["label11"].place(x=260,y=400)
	dbManager.close()