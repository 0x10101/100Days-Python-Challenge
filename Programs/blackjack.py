"""

Blackjack :P

"""

import random
import sys

playerCards = 0
dealerCards = 0

notBust = True

while notBust:
    randomNumber = random.randint(1,10)
    player = input("ENTER to draw a card!")
    if player == "":
        playerCards += randomNumber
        print("Player drew - " + str(randomNumber) + " total = " + str(playerCards))
        randomNumber = random.randint(1,10)    
        dealerCards += randomNumber
        print("Dealer drew - " + str(randomNumber) + " total = " + str(dealerCards))
    else:
        if playerCards > dealerCards:
            print("Player wins!")
        else:
            print("Dealer wins!")
    if playerCards > 21:
        print("Player...BUST!")
        notBust = False
    elif dealerCards > 21:
        print("Dealer...BUST!")
        notBust = False
    
        
        
    
