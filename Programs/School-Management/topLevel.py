import tkinter as tk

class Create:
	def __init__(self):
		#self.frame = frame
		pass

	def top(self,frame,title="",w=500,h=500):
		top = tk.Toplevel()

		ws = frame.winfo_screenwidth() # width of the screen
		hs = frame.winfo_screenheight() # height of the screen
		
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		top.geometry('%dx%d+%d+%d' % (w, h, x, y))
		top.title(title)

		xpos = 100
		ypos = 100
		return top

	def top_labels(self,frame,labels,y_increment=50,fontsize=20,fontfamily="",xpos=100,ypos=100):
		xpos = 100
		ypos = 100
		for label in labels:
			label.configure(font=(fontfamily,fontsize))
			label.place(x=xpos,y=ypos)
			ypos += y_increment



	def top_entries(self,frame,entries,y_increment=50,xpos=200,ypos=100,width=250,height=50,fontsize=20,fontfamily=""):
		for entry in entries:
			entry.configure(font=(fontfamily,fontsize))
			entry.place(x=xpos,y=ypos,width=width,height=height)
			ypos += y_increment

"""
root = tk.Tk()

create = Create()
top = create.top(root)
l1 = tk.Label(top,text="DSA")
l2 = tk.Label(top,text="DAS")

e1 = tk.Entry(top)
e2 = tk.Entry(top)
create.top_labels(top,[l1,l2])
create.top_entries(top,[e1,e2])

root.mainloop()
"""

