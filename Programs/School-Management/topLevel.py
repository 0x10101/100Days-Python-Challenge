import tkinter as tk

class Create:
	def __init__(self):
		#self.frame = frame
		pass

	def top(self,frame,title,w=500,h=500):
		top = tk.Toplevel()

		ws = frame.winfo_screenwidth() # width of the screen
		hs = frame.winfo_screenheight() # height of the screen
		
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		top.geometry('%dx%d+%d+%d' % (w, h, x, y))
		top.title(title)

		return top
	
	def createTitle(self,frame,titleText,fontfamily="",fontsize=20):
		title = tk.Label(frame,text=titleText,font=(fontfamily,fontsize))
		title.place(x=50,y=30)

	def top_labels(self,frame,columns,y_increment=50,fontsize=20,fontfamily="",xpos=100,ypos=100):
		labels = []
		for column in columns:
			print(column)
			label = tk.Label(frame,text=column.title() + ":",font=(fontfamily,fontsize))
			label.place(x=xpos,y=ypos)
			ypos += y_increment
			labels.append(label)
		return labels



	def top_entries(self,frame,columns,y_increment=50,xpos=200,ypos=100,width=250,height=50,fontsize=20,fontfamily=""):
		entries = []
		for column in columns:
			print(column)
			entry = tk.Entry(frame,font=(fontfamily,fontsize))
			entry.place(x=xpos,y=ypos,width=width,height=height)
			ypos += y_increment
			entries.append(entry)
		return entries

root = tk.Tk()

create = Create()
top = create.top(root,"Add Employee")
l1 = tk.Label(top,text="DSA")
l2 = tk.Label(top,text="DAS")

e1 = tk.Entry(top)
e2 = tk.Entry(top)

employees = "firstName,lastName,birthday,phone,address,role,classes,wage"

create.createTitle(top,"Add Employee")
labels = create.top_labels(top,str.split(employees,","))
create.top_entries(top,str.split(employees,","),width=150,height=40,xpos=300)
print(labels)
root.mainloop()

