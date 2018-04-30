import sqlite3
import widgetsFunctions as widgetsF
import treeviewFunctions as treeviewF
#name,lastname,username,password,birthday
#name,lname,usern,passw,birthday

def numberColumns(columns,split):
	if split:
		columnsList = columns.split(",")
	else:
		columnsList = columns
	nValues = 0
	for columns in columnsList:
		nValues += 1
	print("?" + ",?" * (nValues-1))
	return "?" + ",?" * (nValues-1)


class Manage:
	def __init__(self,fileLocation):
		self.fileLocation = fileLocation

	def connect(self):
		self.conn = sqlite3.connect(self.fileLocation)
		print("CONNECTED to {}".format(self.fileLocation))

	def create_table(self,table,columns):
		c = self.conn.cursor()
		print("""CREATE TABLE IF NOT EXISTS {}(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			{})
				""".format(table,columns))
		c.execute("""CREATE TABLE IF NOT EXISTS {}(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			{})
				""".format(table,columns))
		self.conn.commit()
		print("{} table is/was created on {}".format(table,self.fileLocation))
	def insert(self,table,columns,values,split=True):
		c = self.conn.cursor()
		try:
			nValues = numberColumns(columns,split=True) 
		except:
			nValues = numberColumns(columns,split=False) 
		print("""INSERT INTO {}({})
		 	Values({})""".format(table,columns,nValues),values)
		c.execute("""INSERT INTO {}({})
		 	Values({})""".format(table,columns,nValues),values)
		self.conn.commit()
		print("""In {}({}) was inserted
							{}""".format(table,columns,values))
	def update(self,table,columns,values):
		c = self.conn.cursor()
		
		nValues = numberColumns(columns,split=True)
		c.execute("UPDATE {} SET {} WHERE {}".format(table,columns,values))
		self.conn.commit() 
		print("""In  table {}
				Columns changed {}
				Where values {}""".format(table,columns,values))

	def getTableData(self,table,where,returnAccountDict=True,debug=False):
		c = self.conn.cursor()
		data = []
		for column in c.execute("SELECT * FROM {} WHERE {}".format(table,where)):
			if debug:
				print(column)
			data.append(column)
		if table == "accounts" and data and returnAccountDict:
			data = {
				"ID":"{}".format(data[0][0]),
				"First Name":"{}".format(data[0][1]),
				"Last Name":"{}".format(data[0][2]),
				"Username":"{}".format(data[0][3]),
				"Password":"{}".format(data[0][4]),
				"Birthday":"{}".format(data[0][5])
			}
		if debug:
			print("Data returned {}".format(data))
		return data
	def delete(self,table,where,debug=False):
		c = self.conn.cursor()
		c.execute("DELETE FROM {} WHERE {}".format(table,where))
		self.conn.commit()
		if debug:
			print("DELETE FROM {} WHERE {}".format(table,where))
	def close(self):
		self.conn.close()
		print("DISCONNECTED FROM {}".format(self.fileLocation))

def insertValues(toplevel,table,columns,entries,treeView,messageText,messagebox,dashboardData):
	insert = True
	dbManager = Manage("database.db")
	dbManager.connect()
	entries[1] = [entry for entry in tuple(entries)]
	entries_get = []
	for entry in entries[0]:
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
		treeView.insert("", 0, text="", values=dbManager.getTableData(table,"id=id")[-1])
		#treeviewF.updateTreeView(treeView,table)
	else:
		messagebox.showerror("Error","15 Characters is the limit!")
	dbManager.close()
	widgetsF.updateStats(dashboardData)

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
			hours INTEGER,
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
classes_columnsList = "name,subject,hours,students,instructor,price"
subjects_columnList = "subject"
students_columnsList = "firstName,lastName,birthday,phone,address"
employees_columnsList = "firstName,lastName,birthday,phone,address,role,classes,wage"

"""dbManager = Manage("database.db")
dbManager.connect()
account = dbManager.getTableData("accounts","username='{}' and password='{}'".format("gjergjk71","gjergji.123"))"""


#Testing
#dbManage = Manage("database.db")
#dbManage.connect()
#dbManage.update("accounts","password='gjergji.12345'","id=1")
#acc = dbManage.getTableData("accounts","id=2")
#print(acc["Birthday"])
#acc = dbManage.getAccounts("accounts")
#print(acc)
#tilus