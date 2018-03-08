
"""

Temperature Converter:

Version : 1.1
Changes:
    -Removed notTrue and changed "while not notTrue" to "while True" duh..
    -Removed askValid....
    #Reminder : Do not code after 2-3AM
    -When the user types the option in "ask" input it lowercases its letters
         and strips whitespace so for ex. " CELsIuS   " is changed to
         "celsius"

"""

import sys

print("Temperature Converter")

print("'celsius' to convert celsius to fahrenheit")
print("'fahrenheit' to conver fahrenheit to celsius")
print("--------------------")
print("Type 'q' to quit any time!")

def celsius_to_fahrenheit():
    while True:
        try:
            celsius = float(input("Celsius: "))
            break
        except ValueError:
            print("Please type an integer or flaoting number!")
    fahrenheit = (float(celsius) * 1.8) + 32
    print(str(celsius) + " celsius equals " + str(fahrenheit) + " fahrenheit!")

def fahrenheit_to_celsius():
    while True:
        try:
            fahrenheit = float(input("Fahrenheit : "))
            break
        except ValueError:
            print("Please type an integer or floating number!")
    celsius = (float(fahrenheit) - 32) * 0.5556
    print(str(fahrenheit) + " fahrenheit equals " + str(celsius) + " celsius!")



while True:
    ask = str(input("Celsius/Fahrenheit : "))
    ask = ask.lower().strip()
    if ask == "celsius":
        celsius_to_fahrenheit()
    elif ask == "fahrenheit":
        fahrenheit_to_celsius()
    elif ask == "q":
        print("Terminating the program!")
        sys.exit()
    else:
        print("Please chose an option!")
