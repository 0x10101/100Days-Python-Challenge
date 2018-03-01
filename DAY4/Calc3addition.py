print("------ Calculator ------")
def addition(number1,number2,number3):
    equals = number1 + number2 + number3
    print(str(number1) + "+" + str(number2) + "+" + str(number3) + " equals" + str(equals))

while True:
    number1 = float(input("Number1: "))
    number2 = float(input("Number2: "))
    number3 = float(input("Number3: "))
    addition(number1,number2,number3)
    break

print("Test")
print(addition(1,1,1))
