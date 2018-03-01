import random

chances = 0
used_chances = 0
number = random.randint(1,15)
print("------ Number is " + str(number))

while not chances:
    try:
        chances = int(input("Chances: "))
    except ValueError:
        print("No string or float values...")

for c in range(chances):
    print("------ Chances is " + str(chances))
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
        chances = chances - 1
        used_chances = used_chances + 1
        print("Guessed correctly!")
        print("You used " + str(used_chances) + " chances!")


    else:
        chances = chances - 1
        used_chances = used_chances + 1
    
