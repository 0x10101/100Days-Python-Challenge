"""
Calculator from codereview ( cleaning it )
https://codereview.stackexchange.com/questions/31286/py
thon-calculator-script?newreg=a64e20a154d54122a704bc5e22ad9dfa

"""

theList = ["add","multiply",
           "divide","subtract"]

def getNumbers():
    global x
    global y
    while True:
        try:
            x = int(input("First number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    while True:
        try:
            y = int(input("Second number: "))
            break
        except ValueError:
            print("Make sure to enter a number...")

while True:
    operation = input("What would you like to do? Multiply/Divide" +
            "/Add/Subtract ")
    if operation.lower() in theList:
        break
    else:
        print("That was not an option..")

if operation.lower() == "multiply": # If operation is equal to "multiply"
    getNumbers()
    z = x * y
    print(z)
elif operation.lower() == "subtract": # If operation is equal to "substract"
    getNumbers()
    z = x - y
    print(z)
elif operation.lower() == "add": # If operation  is equal to "add"
    getNumbers()
    z = x + y
    print(z)
elif operation.lower() == "divide": # If operation is equal to "divide"
    getNumbers()
    z = x / y
    print(z)

