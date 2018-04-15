import database as db

class LoginSystem():
	def __init__(self):
		pass
	def login(self,usern,passw):
		dbManager = db.Manage("database.db")
		dbManager.connect()
		acc = dbManager.getTableData("accounts","username='{}' and password='{}'".format(usern,passw))
		account = {
				"ID":"{}".format(acc[0][0]),
				"First Name":"{}".format(acc[0][1]),
				"Last Name":"{}".format(acc[0][2]),
				"Username":"{}".format(acc[0][3]),
				"Password":"{}".format(acc[0][4]),
				"Birthday":"{}".format(acc[0][5])
		}
		print(account)
		dbManager.close()
		if account:
			return account
		else:
			return False

access = LoginSystem().login("gjergjk71","gjergji.123")
print(access["First Name"])