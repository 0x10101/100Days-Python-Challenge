import sqlite3
#name,lastname,username,password,birthday
#name,lname,usern,passw,birthday

def numberColumns(columns):
	columnsList = columns.split(",")
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
		c.execute("""CREATE TABLE IF NOT EXISTS {}(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			{})
				""".format(table,columns))
		self.conn.commit()
		print("{} table is/was created on {}".format(table,self.fileLocation))
	def insert(self,table,columns,values):
		c = self.conn.cursor()
		nValues = numberColumns(columns) 
		c.execute("""INSERT INTO {}({})
		 Values({})""".format(table,columns,nValues),values)
		#c.execute('INSERT INTO students Values(?,?,?,?,?)', (ID,name,lname,usern,passw))
		#c.execute("INSERT INTO {} Values({},{},{},{},{})".format(table,ID,name,lname,usern,passw))
		self.conn.commit()
		print("""In {}({}) was inserted
							{}""".format(table,columns,values))
	def getAccounts(self,table):
		c = self.conn.cursor()
		accounts = []
		accInfo = []
		for account in c.execute("SELECT * FROM {}".format(table)):
			print(account)
			for item in range(4):
				accInfo.append(account[item])
			accounts.append(accInfo)
			accInfo = []
		return accounts
	def close(self):
		self.conn.close()
		print("DISCONNECTED FROM {}".format(self.fileLocation))

#Testing
#dbManage = Manage("database-tes")
#dbManage.connect()
#dbManage.create_table("students1")
#dbManage.insert("students1","0","gjergj12","1232123311","gjergjk71")
#acc = dbManage.getAccounts("accounts")
#print(acc)

#nautilus