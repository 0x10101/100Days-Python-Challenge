"""

Developer : Gjergj Kadriu
Version : 1.3

Changes:
    -Removed trackChances()
    -added while True: #ask for guess_input


"""

import random
import sys

chances = 0
used_chances = 0
number = random.randint(1,15)
# Testing purposes print("------ Number is " + str(number))



while not chances:
    try:
        chances = int(input("Chances: "))
    except ValueError:
        print("No string or float values...")

for c in range(chances):
    print("------ You have " + str(chances) + " left!")
    print("Guess from 1-15")
    while True:
        try:
            number_input = int(input("Guess: "))
            break
        except ValueError:
            print("Can't be a float or a string!!")
    if number_input:
        chances -= 1
        used_chances += 1
    if number_input == number:
        print("Guessed correctly!")
        print("You used " + str(used_chances) + " chance(s)!")
        sys.exit()
    elif number_input > number:
        print("Hmm.. Lower!")
    elif number_input < number:
        print("Hmm.. Higher!")

print("chances {} and used_chances {}".format(chances,used_chances))
    
