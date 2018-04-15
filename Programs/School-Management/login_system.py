import database as db

class LoginSystem():
	def __init__(self):
		pass
	def login(self,usern,passw):
		dbManager = db.Manage("database.db")
		dbManager.connect()
		acc = dbManager.getTableData("accounts","username='{}' and password='{}'".format(usern,passw))
		dbManager.close()
		if acc:
			return acc
		else:
			return False

#access = LoginSystem().login("gjergjk71","gjergji.123")
#print(access["First Name"])