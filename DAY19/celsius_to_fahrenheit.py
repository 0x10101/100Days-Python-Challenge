import tkinter as tk

#Celsius to Fahrenheit // -> celsius * 1.8 + 32
#Fahrenheit to Celsius // -> fahrenheit - 32 * 0.5556

def convertTo_fahrenheit():
    convert = float(celsius_data) * 1.8 + 32
    fahrenheit_dataGet.delete(0, END)
    fahrenheit_dataGet.insert(0, str(convert))

def convertTo_celsius():
    convert = float(fahrenheit_data) - 32 * 0.5556
    fahrenheit_entry.delete(0, END)
    fahrenheit_entry.insert(0, convert)

root = tk.Tk()

def callback(message):
    print(message)

    

title = tk.Label(text="Temperature Converter",
                 font=("Courier", 20)).pack()

celsius = tk.Label(text="Celsius",
                 font=("Courier", 15)).pack()


celsius_dataGet = tk.StringVar()
celsius_entry = tk.Entry(root,textvariable = celsius_dataGet).pack()
celsius_dataGet.set("0")
celsius_data = celsius_dataGet.get()

celsius_button = tk.Button(root,
                           text="Convert to fahrenheit",
                           command=lambda:convertTo_fahrenheit).pack()

fahrenheit = tk.Label(text="Fahrenheit",
                 font=("Courier", 15)).pack()

fahrenheit_dataGet = tk.StringVar()
fahrenheit_entry = tk.Entry(root,textvariable = fahrenheit_dataGet).pack()
fahrenheit_dataGet.set("0")
fahrenheit_data = fahrenheit_dataGet.get()

fahrenheit_button = tk.Button(root,
                           text="Convert to celsius",
                           command=lambda:convertTo_celsius).pack()

root.mainloop()
