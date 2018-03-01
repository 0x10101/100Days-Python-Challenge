"""

Creator: Gjergj Kadriu
Version 1.1

Update:
    made the variables global for some reason :P
    Have an option to ask for help in the beggining instead of using the-
       operator to get /help or exit ...
    Have an option in the end of the calculation if you want to exit
    Added some ValueError so the user can't put invalid data and if he does
        it will not take out an error instead it will tell the user to put
        a valid number/data ( except ValueError )


"""

yesAnswer = {"Yes","yes","Y","y","Ye","yeah","ye"}
noAnswer = {"No","no","N","n"}
number1 = ""
number2 = ""
function = ""
leave = ""
advice = ""

print("-" * 10 + " Calculator " + "-" * 10)


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
        print("Operator can't be a string!")

def resetData():
    global number1
    global number2
    global function
    global leave
    global advice
    number1 = ""
    number2 = ""
    function = ""
    leave = ""
    advice = ""
    """ For testing purposes
    print("Number1 : " + number1)
    print("number2 : " + number2)
    print("function : " + function)
    print("leave : " + leave)
    print("advice : " + advice)
    """

def help():
    print("'+' - Stands for addition")
    print("'-' - Stands for subtraction")
    print("'*' - Stands for multiplication")
    print("'/' - Stands for division")
    print("'//' - Stands for integer division")
    print("'%' - Stands for remaninder(modulus)")

    
while not advice:
    try:
        advice = input("Do you need help on how to use the calculator? : ")
        if advice in yesAnswer:
            help()
        elif advice in noAnswer:
            print("You know your shit huh... :P")
    except ValueError:
        print("Please use Yes or No!")
    


while True:
    func = {"+","-","/","*","%"}
    while number1 == "" and number2 == "":
        if function not in func:    
            try:
                number1 = float(input("First number: "))
                function = input("Choose operator + - / * % : ")
                number2 = float(input("Second number"))
            except ValueError:
                print("Please give us the right data")
    #if function in func:
    calculate(number1,number2)
    leave = input("Do you want to exit? : ")
    if leave in yesAnswer:
        break
    elif leave in noAnswer:
        print("You choosed no")
        resetData()
    else:
        resetData()
