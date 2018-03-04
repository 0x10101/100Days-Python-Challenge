"""

Blackjack
Version : 1.1

Goshh.. I'm gonna cringe so much when I see this pile
of shit after a few years :P 

"""

import random
import sys

playerCards = 0
dealerCards = 0


notBust = True
firstDealerCard = True
playerStand = False

playerBlackjack = False
dealerBlackjack = False

while notBust:
    randomNumber = random.randint(1,11)
    if not playerStand:
        playerHit = input("ENTER to HIT!")
        if playerHit:
            playerStand = True
    if playerHit == "":
        playerCards += randomNumber
        print("Player drew - " + str(randomNumber) + " total = " + str(playerCards))
    if dealerCards < 17:
        randomNumber = random.randint(1,11)
        dealerCards += randomNumber
        print("Dealer drew a card!")
        #print(dealerCards)
    if playerCards > 21:
        print("Player...BUST!")
        notBust = False
        print("Dealer wins!")
        sys.exit()
    elif playerCards == 21:
        print("Blackjack! - Player")
    if dealerCards > 21:
        if not playerBlackjack:
            print("Dealer...BUST!")
            notBust = True
            print("Player wins!")
            sys.exit()
    if dealerCards == 21:
        if not dealerBlackjack:
            print("Blackjack! - Dealer")
            dealerBlackjack = True
    if dealerCards > 21:
        print("Player wins")
        sys.exit()
    if playerHit != "" and dealerCards > 17:
        if playerCards > dealerCards:
            print("Player wins!")
            sys.exit()
        elif playerCards == dealerCards:
            print("Tie")
            sys.exit()
        else:
            print("Dealer wins!")
            sys.exit()
    if playerHit != "" and not dealerCards >= 17:
        playerStand = True
        randomNumber = random.randint(1,11)
        dealerCards += randomNumber
        #print(dealerCards)
        print("Dealer drew a card!")
    
        
"""
print("Dealer drew - " + str(randomNumber)
+ " total = " + str(dealerCards))

"""
