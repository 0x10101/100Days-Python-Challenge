import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("School Management")
root.geometry("{}x{}".format(900,700))


root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

l1 = tk.Label(root,text="Sign in",font=("",70))
l1.place(x=50,y=50)

l2 = tk.Label(root,text="Username: ",font=("",30))
l2.place(x=130,y=180)

#e2_content = 
e2 = tk.Entry(root)
e2.place(x=360,y=180,width=300,height=55)

l3 = tk.Label(root,text="Password:",font=("",30))
l3.place(x=135,y=250)

e3 = tk.Entry(root)
e3.place(x=360,y=250,width=300,height=55)

b1 = tk.Button(root,text="Login",font=("",28))
b1.place(x=310,y=330,width=150,height=50)



root.mainloop()