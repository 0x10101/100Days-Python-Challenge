from database import Manage
import widgetsFunctions as widgetsF

class LoginSystem():
	def __init__(self):
		pass
	def login(self,usern,passw):
		self.usern = usern
		self.passw = passw
		dbManager = Manage("database.db")
		dbManager.connect()
		acc = dbManager.getTableData("accounts","username='{}' and password='{}'".format(usern,passw))
		dbManager.close()
		if acc:
			return acc
			print("Logged in")
		else:
			print("Wrong us/pw")
			return False


#LoginSystem().loginAttempt()


#access = LoginSystem().login("gjergjk71","gjergji.123")
#print(access["First Name"])