import tkinter as tk
from tkinter import ttk
import database as db
import widgetsFunctions as widgetsF

def createTreeView(tab,table,columns):
	tree = ttk.Treeview(tab,columns=columns) #height=18
	tree['show'] = 'headings'

	for column in tree["columns"]:
		if column == "ID":
			tree.column("{}".format(column),minwidth=0,width=30)
		else:
			tree.column("{}".format(column),minwidth=0,width=100)

	for column in tree["columns"]:
		tree.heading("{}".format(column),text=column)

	dbManager = db.Manage("database.db")
	dbManager.connect()

	for row in dbManager.getTableData(table,"id=id"):
		tree.insert("" , 0,    text="", values=(row))

	dbManager.close()

	tree.place(x=10,y=10,width=890)
	return tree

def updateTreeView(treeView,table):
	treeView.delete(*treeView.get_children())

	for column in treeView["columns"]:
		if column == "ID":
			treeView.column("{}".format(column),minwidth=0,width=30)
		else:
			treeView.column("{}".format(column),minwidth=0,width=100)

	for column in treeView["columns"]:
		treeView.heading("{}".format(column),text=column)

	dbManager = db.Manage("database.db")
	dbManager.connect()

	for row in dbManager.getTableData(table,"id=id"):
		treeView.insert("" , 0,    text="", values=(row))

	treeView['show'] = 'headings'
	treeView.place(x=10,y=10,width=890)

	dbManager.close()

def delete(treeView,table,dashboardData):
	selected = treeView.focus()
	ID = treeView.item(selected)["values"][0]
	print(ID)
	dbManager = db.Manage("database.db")
	dbManager.connect()
	dbManager.delete(table,"id={}".format(ID),debug=True)
	dbManager.close()
	updateTreeView(treeView,table)
	widgetsF.updateStats(dashboardData)


