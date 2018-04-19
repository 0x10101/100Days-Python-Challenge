import tkinter as tk

class Create:
	def __init__(self,frame):
		self.frame = frame
	def top(self,title,columns,w=500,h=500,xpos=100,ypos=100,y_increment=50,fontsize=20,fontfamily=""):
		add = tk.Toplevel()
		w = 500
		h = 500

		ws = self.frame.winfo_screenwidth() # width of the screen
		hs = self.frame.winfo_screenheight() # height of the screen
		
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		add.geometry('%dx%d+%d+%d' % (w, h, x, y))
		add.title(title)

		xpos = 100
		ypos = 100
		for column in columns:
			column = column.title() + ": "
			label = tk.Label(add,text=column,font=(fontfamily,fontsize))
			label.place(x=xpos,y=ypos)
			ypos += y_increment



