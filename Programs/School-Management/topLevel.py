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
	
	def title(self,frame,titleText,fontfamily="",fontsize=20):
		title = tk.Label(frame,text=titleText,font=(fontfamily,fontsize))
		title.place(x=50,y=30)
		return title

	def top_labels(self,frame,columns,y_increment=50,fontsize=20,fontfamily="",xpos=100,ypos=100):
		labels = []
		for column in columns:
			print(column)
			label = tk.Label(frame,text=column.title() + ":",font=(fontfamily,fontsize))
			label.place(x=xpos,y=ypos)
			ypos += y_increment
			labels.append(label)
		return labels



	def top_entries(self,frame,entries,columns,y_increment=50,xpos=200,ypos=100,width=250,height=50,fontsize=20,fontfamily=""):
		for entry in entries:
			entry.place(x=xpos,y=ypos,width=width,height=height)
			ypos += y_increment

	def top_button(self,frame,func,xpos,ypos,text="add",width=200,height=50):
		button = tk.Button(frame,text=text,command=func)
		button.place(x=xpos,y=ypos,width=width,height=height)
		return button

if __name__ == "__main__":
	root = tk.Tk()
	def test():
		print("TEST")
	create = Create()
	top = create.top(root,"Add Employee",h=600)
	def show_data(entries):
		eN = 1
		for entry in entries:
			print("{} {}".format(eN,entry.get()))
			eN += 1

	employees = "firstName,lastName,birthday,phone,address,role,classes,wage"

	create.title(top,"Add Employee")
	labels = create.top_labels(top,str.split(employees,","))
	entries = create.top_entries(top,str.split(employees,","),width=150,height=40,xpos=300)
	create.top_button(top,lambda: show_data(entries),160,500)


	root.mainloop()

