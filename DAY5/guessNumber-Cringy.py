import random
chances = 0
true = True
             
while true:
    while not chances:
        try:
            chances = int(input("Chances: "))
        except ValueError:
            print("Ooppss, please use integers")
    for i in range(chances):
        print("---------------------")
        print("-Guess from 1 to 15")
        number = random.randint(1,15)
        print("----NUMBER data------")
        print("TEST(" + str(number) + ")")
        print("----------")
        guess = input("Guess: ")
        chances = int(chances) - 1
        print("-----Chances data-----")
        print("TEST(" + str(chances) + ")")
        print("----------")
        if not guess or guess == float():
            continue
        print("----Number data------")
        print("TEST" + str(number))
        print("----------")
        if int(guess) == number:
            print("-Guessed correctly")
            true = False
        if chances == 0:
            print("-You used up all your chances")
            true = False
    start(chances)
    if chances == 0:
        true = False
