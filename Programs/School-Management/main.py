#Version 0.1

import tkinter as tk
from tkinter import ttk
from database import Manage

def loginAttempt():
	access = False
	dbManager = Manage("database.db") #fileLocation
	dbManager.connect()
	dbManager.create_table("accounts")
	c = dbManager.conn.cursor()
	for account in c.execute("SELECT * FROM accounts"):
		if account[3] == e1.get() and account[4] == e2.get():
			access = True
			break
	if not access:
		l3.place(x=200,y=380)
	else:
		l3.place_forget()
	print(access)
	return access

def showRegister():
	pass

root = tk.Tk()
root.title("School Management")
root.geometry("{}x{}".format(900,500))

root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

l1 = tk.Label(root,text="Sign in",font=("",70))
l1.place(x=50,y=50)

l2 = tk.Label(root,text="Username: ",font=("",30))
l2.place(x=130,y=180)

#e2_content = 
e1 = tk.Entry(root,font=("",20))
e1.place(x=360,y=180,width=300,height=55)

l3 = tk.Label(root,text="Password:",font=("",30))
l3.place(x=135,y=250)

e2 = tk.Entry(root,font=("",20),show="*")
e2.place(x=360,y=250,width=300,height=55)

l3 = tk.Label(root,text="Username or Password is wrond!",font=("",20))

b1 = tk.Button(root,text="Login",font=("",28),command=loginAttempt)
b1.place(x=300,y=330,width=150,height=50)

b2 = tk.Button(root,text="Register",font=("",28),command=showRegister)
b2.place(x=470,y=330,width=160,height=50)



root.mainloop()