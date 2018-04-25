import sqlite3
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

	def getTableData(self,table,where,returnAccountDict=True):
		c = self.conn.cursor()
		data = []
		for column in c.execute("SELECT * FROM {} WHERE {}".format(table,where)):
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
		print("Data returned {}".format(data))
		return data
	def close(self):
		self.conn.close()
		print("DISCONNECTED FROM {}".format(self.fileLocation))

#Testing
#dbManage = Manage("database.db")
#dbManage.connect()
#dbManage.update("accounts","password='gjergji.12345'","id=1")
#acc = dbManage.getTableData("accounts","id=2")
#print(acc["Birthday"])
#acc = dbManage.getAccounts("accounts")
#print(acc)

#nautilus