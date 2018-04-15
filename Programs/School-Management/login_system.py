import database as db

class LoginSystem():
	def __init__(self):
		pass
	def loginAttempt(self,usern,passw):
		dbManager = db.Manage("database.db")
		dbManager.connect()
		account = dbManager.getTableData("accounts","username='{}' and password='{}'".format(usern,passw))
		if account:
			return True
		else:
			return False

access = LoginSystem().loginAttempt("gjergjk71","gjergji.123")
print(access)