import random
print("Dice Rolling Simulator")

print("You win if the dice rolls 6 (You have 3 chances)")
chances = 3

while chances:
    roll = input("Press ENTER to roll!")
    chances -= 1
    if roll == "":
        dice = random.randint(1,6)
    if dice:
        print("You rolled " + str(dice))
        if dice == 6:
            print("You win....")
            break
        elif chances == 2:
            print("You have " + str(chances) + " chances left!")
        elif chances == 1:
            print("You have only 1 chance left!")
if not chances:    
    print("Lost pff")
