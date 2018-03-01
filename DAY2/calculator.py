"""

Creator: Gjergj Kadriu
Version 1.0

"""

print("-" * 10 + " Calculator " + "-" * 10)
print("If you need help with how to use the calculator please type /help in the operator input")



def addition(number1,number2):
    print(str(number1) + " + " + str(number2) + " is equal to ", str(number1 + number2))

def subtraction(number1,number2):
    print(str(number1) + " - " + str(number2) + " is equal to ", str(number1 - number2))

def multiplication(number1,number2):
    print(str(number1) + " * " + str(number2) + " is equal to ", str(number1 * number2))
          
def division(number1,number2):
    print(str(number1) + " / " + str(number2) + " is equal to ", str(number1 / number2))

def integer_division(number1,number2):
    print(str(number1) + " // " + str(number2) + " is equal to ", str(number1 // number2))

def modulus(number1,number2):
    print(str(number1) + " % " + str(number2) + " is equal to ", str(number1 % number2))


def calculate(number1,number2):
    if function == "+":
        addition(number1,number2)
    elif function == "-":
        subtraction(number1,number2)
    elif function == "*":
        multiplication(number1,number2)
    elif function == "/":
        division(number1,number2)
    elif function == "//":
        integer_division(number1,number2)
    elif function == "%":
        modulus(number1,number2)
    elif function == int() or float():
        print("Operator cannot be an integer or floating number!")
    else:
        print("Please use /help, operator can't be a string!")

def help():
    print("'+' - Stands for addition")
    print("'-' - Stands for subtraction")
    print("'*' - Stands for multiplication")
    print("'/' - Stands for division")
    print("'//' - Stands for integer division")
    print("'%' - Stands for remaninder(modulus)")




while True:
    func = ["+","-","/","*","%"]
    number1 = float(input("First number: "))
    function = input("Choose operator + - / * % : ")
    number2 = float(input("Second number"))
    if function in func:
        calculate(number1,number2)
    elif function == "/help":
        help()
    elif function == "/exit":
        print("Successfully terminated the program")
        break
    else:
        print("Please use /help if you didn't want to quit.")
        break
