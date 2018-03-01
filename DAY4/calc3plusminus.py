number1 = float(input("Number1 : "))
operator = input("Operator : ")
number2 = float(input("Number2 : "))
operator2 = input("Operator2 : ")
number3 = float(input("Number3 : "))

#Extra from the handcode
print(str(number1) + " " + operator + " " + str(number2) + " " + operator2 + " " + str(number3))


if operator == "+":
    number12 = number1 + number2
    print(str(number12) + " " + str(operator2) + " " + str(number3))
elif operator == "-":
    number12 = number1 - number2
    print(str(number12) + " " + operator2 + " " + str(number3))

if operator2 == "+":
    number123 = number12 + number3
    print(number123)
elif operator2 == "-":
    number123 = number12 - number3
    print(number123)
