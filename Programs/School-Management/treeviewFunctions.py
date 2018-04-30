import tkinter as tk
from tkinter import ttk
import database as db
import widgetsFunctions as widgetsF

def createTreeView(tab,table,columns):
	tree = ttk.Treeview(tab,columns=columns) #height=18
	scrollb = ttk.Scrollbar(tab, orient="vertical", command=tree.yview)
	tree.configure(yscrollcommand=scrollb.set)
	tree['show'] = 'headings'

	for column in tree["columns"]:
		if column == "ID":
			tree.column("{}".format(column),minwidth=500/len(tree["columns"]),width=750/len(tree["columns"]))
		else:
			tree.column("{}".format(column),minwidth=500/len(tree["columns"]),width=750/len(tree["columns"]))

	for column in tree["columns"]:
		tree.heading("{}".format(column),text=column)

	dbManager = db.Manage("database.db")
	dbManager.connect()

	for row in dbManager.getTableData(table,"id=id"):
		tree.insert("" , 0,    text="", values=(row))

	dbManager.close()

	scrollb.place(x=880,y=10,height=300)
	tree.place(x=10,y=10,width=880,height=300)
	return tree

def delete(treeView,table,dashboardData):
	selected = treeView.focus()
	ID = treeView.item(selected)["values"][0]
	print(ID)
	dbManager = db.Manage("database.db")
	dbManager.connect()
	dbManager.delete(table,"id={}".format(ID),debug=True)
	dbManager.close()
	treeView.delete(selected)
	#updateTreeView(treeView,table)
	widgetsF.updateStats(dashboardData)

"""def updateTreeView(treeView,table):
	treeView.delete(*treeView.get_children())

	treeView['show'] = 'headings'

	for column in treeView["columns"]:
		if column == "ID":
			treeView.column("{}".format(column),minwidth=500/len(treeView["columns"]),width=750/len(treeView["columns"]))
		else:
			treeView.column("{}".format(column),minwidth=500/len(treeView["columns"]),width=750/len(treeView["columns"]))

	for column in treeView["columns"]:
		treeView.heading("{}".format(column),text=column)

	dbManager = db.Manage("database.db")
	dbManager.connect()

	for row in dbManager.getTableData(table,"id=id"):
		treeView.insert("" , 0,    text="", values=(row))

	dbManager.close()

	treeView.place(x=10,y=10,width=890)
	dbManager.close()"""