"""

Developer : Gjergj Kadriu
Version : 1.1

Changes:
    Made possible to do multiple calculations
    Added exit input to ask the user if he wants to terminate the program
    Put the if-elif's statements in a function
    Changed some variables to global    

"""

import sys

GETDATA = True
NUMBER1 = None
NUMBER2 = None
NUMBER3 = None
OPERATOR = ""
OPERATOR2 = ""
operators = "+", "-"
yesAnswer = ["Yes","y","Ye","yeh","Yep","yEs","Y"]


def resetData():
    global NUMBER1
    global NUMBER2
    global NUMBER3
    global OPERATOR
    global OPERATOR2
    NUMBER1 = None
    NUMBER2 = None
    NUMBER3 = None
    OPERATOR = ""
    OPERATOR2 = ""

def exit():
    leave = input("Do you want to exit?")
    if leave in yesAnswer:
        sys.exit()
    else:
        resetData()

    

def calculate():
    print(str(NUMBER1) + " " + OPERATOR + " " + str(NUMBER2) + " " + OPERATOR2 + " " + str(NUMBER3))
    if OPERATOR == "+":
        number12 = NUMBER1 + NUMBER2
        print(str(number12) + " " + str(OPERATOR2) + " " + str(NUMBER3))
    elif OPERATOR == "-":
        number12 = NUMBER1 - NUMBER2
        print(str(number12) + " " + OPERATOR2 + " " + str(NUMBER3))
    if OPERATOR2 == "+":
        number123 = number12 + NUMBER3
        print(number123)
    elif OPERATOR2 == "-":
        number123 = number12 - NUMBER3
        print(number123)

while True:
    try:
        NUMBER1 = float(input("Number1 : "))    
        while OPERATOR not in operators:
            OPERATOR = input("Operator : ")
            if OPERATOR not in operators:
                print("Please put + for addition or - for subtraction!")
        while not NUMBER2:
            try:
                NUMBER2 = float(input("Number2 : "))
            except ValueError:
                print("Please put an integer or floating number")
        while not OPERATOR2 in operators:
            OPERATOR2 = input("Operator2 : ")
            if OPERATOR2 not in operators:
                print("Please put + for addition or - for subtraction!")
        while not NUMBER3:   
            try:
                NUMBER3 = float(input("Number3 : "))
            except ValueError:
                print("Please put an integer or floating number")
    except ValueError:
        print("Please give the right data")
    if NUMBER1 and NUMBER2 and NUMBER3 and OPERATOR and OPERATOR2:
        calculate()
        exit()
        resetData()
    else:
        resetData()
        continue
