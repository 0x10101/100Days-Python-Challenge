"""

Developer : Gjergj Kadriu
Version : 1.2


"""

import random
import sys

CHANCES = 0
USED_CHANCES = 0
number = random.randint(1,15)
# Testing purposes print("------ Number is " + str(number))

def trackChances():
    global CHANCES
    global USED_CHANCES
    CHANCES = CHANCES - 1
    USED_CHANCES = USED_CHANCES + 1
    

while not CHANCES:
    try:
        CHANCES = int(input("Chances: "))
    except ValueError:
        print("No string or float values...")

for c in range(CHANCES):
    print("------ You have " + str(CHANCES) + " left!")
    print("Guess from 1-15")
    try:
        number_input = int(input("Guess: "))
    except ValueError:
        print("Can't be a float or a string!!")
        try:
            number_input = int(input("Guess: "))
        except ValueError:
            print("Moron..")
            break
    if number_input == number:
        trackChances()
        print("Guessed correctly!")
        print("You used " + str(USED_CHANCES) + " chance(s)!")
        sys.exit()
        
    elif number_input > number:
        trackChances()
        print("Hmm.. Lower!")
    elif number_input < number:
        trackChances()
        print("Hmm.. Higher!")
    else:
        trackChances()
    
