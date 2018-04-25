import tkinter as tk

class Create:
	def __init__(self,ypos=0):
		#self.frame = frame
		self.ypos = ypos
		pass

	def top(self,frame,title,w=500,h=500):
		top = tk.Toplevel()

		ws = frame.winfo_screenwidth() # width of the screen
		hs = frame.winfo_screenheight() # height of the screen
		
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		top.geometry('%dx%d+%d+%d' % (w, h, x, y))
		top.title(title)
		
		self.w = w 
		self.h = h
		self.x = x
		self.y = y 

		return top
	
	def title(self,frame,titleText,fontfamily="",fontsize=20):
		title = tk.Label(frame,text=titleText,font=(fontfamily,fontsize))
		title.place(x=50,y=30)
		return title

	def top_labels(self,frame,columns,y_increment=50,fontsize=20,fontfamily="",xpos=100,ypos=100):
		labels = []
		for column in columns:
			label = tk.Label(frame,text=column.title() + ":",font=(fontfamily,fontsize))
			label.place(x=xpos,y=ypos)
			ypos += y_increment
			labels.append(label)
		return labels



	def top_entries(self,frame,labels,entries,columns,y_increment=50,xpos=200,ypos=100,width=250,height=50,fontsize=20,fontfamily=""):
		labelsText = []
		for label in labels:
			labelsText.append(label.cget("text"))
		print(labelsText)
		item = 0
		if entries:
			for entry in entries[0]:
				#if labelsText[item] not in notEntries:
				if labelsText[item] == "Birthday:":
					spinBoxDay_data2 = tk.StringVar()
					spinBoxDay2 = tk.Spinbox(frame,from_=01, to=31, increment=1,
					            validate='all',font=("",20),textvariable=spinBoxDay_data2)

					spinBoxMonth_data2 = tk.StringVar() 
	 				spinBoxMonth2 = tk.Spinbox(frame,from_=01, to=12, increment=1,
					            validate='all',font=("",20),textvariable=spinBoxMonth_data2)
	 				
	 				spinBoxYear_data2 = tk.StringVar()
					spinBoxYear2 = tk.Spinbox(frame,from_=1980, to=2018, increment=1,
					            validate='all',font=("",20),textvariable=spinBoxYear_data2)
					
					spinBoxDay2.place(x=xpos,y=ypos,height=50,width=80)
					spinBoxMonth2.place(x=xpos+80,y=ypos,height=50,width=80)
					spinBoxYear2.place(x=xpos+160,y=ypos,height=50,width=100)
					birthday_date = "{}/{}/{}".format(spinBoxDay_data2.get(),spinBoxMonth_data2.get(),spinBoxYear_data2.get())
					entries[1][item].set(birthday_date)
				if labelsText[item] == "Wage:":
					wage_data = tk.StringVar()
					wage = tk.Spinbox(frame,from_=100, to=2000, increment=50,
					            validate='all',font=("",20),textvariable=wage_data)
					wage.place(x=xpos,y=ypos,height=50,width=200)
					entries[1][item].set(str(wage_data.get()))
				else:
					entry.place(x=xpos,y=ypos,width=width,height=height)
				ypos += y_increment
				item += 1
		self.ypos = ypos

	def top_button(self,frame,func,xpos,text="add",width=200,height=50):
		self.ypos += 10
		button = tk.Button(frame,text=text,command=func)
		button.place(x=xpos,y=self.ypos,width=width,height=height)
	
		return (self.w,self.ypos + 20)

	def changeGeometry(self,frame):
		frame.geometry('%dx%d+%d+%d' % (self.w,self.ypos + 150,self.x,self.y))


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
	entries = create.top_entries(top,labels,[],str.split(employees,","))
	create.top_button(top,lambda: show_data(entries),160)


	root.mainloop()

