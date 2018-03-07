"""

Version 1.8

Changes:
    -The user can guess any letter from the list not only the next one
    -The whole word is printed when the user guesses all the letters or the word
"""

import random

hangman_art = """
    __  __ ___     _   __ ______ __  ___ ___     _   __
   / / / //   |   / | / // ____//  |/  //   |   / | / /
  / /_/ // /| |  /  |/ // / __ / /|_/ // /| |  /  |/ / 
 / __  // ___ | / /|  // /_/ // /  / // ___ | / /|  /  
/_/ /_//_/  |_|/_/ |_/ \____//_/  /_//_/  |_|/_/ |_/   

 """

stages  = ['''
 =========''', '''
       |
       |
       |
       |
       |
 =========''', '''
    +---+
       |
       |
       |
       |
       |
 =========''', '''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''']


file = open("random_words.txt", "r")
#Make a list out of every word in file
words = list(file.read().split())

#Generate a random number for random_Index
# use random_Index to pick a random word from the 'words' list
rand_Index = random.randint(0,len(words))
random_word = words[rand_Index]

#Number of guesses the user can make
chances = 10

print(hangman_art)
print("---Hangman Game---")
print("--You have 5 guesses!--")

 
#Testing purposes
print(random_word)
guessed_number = 1
randomMinusNumber = len(random_word) - guessed_number
letters_Left = list(random_word)[0] + "_" * randomMinusNumber
letters = letters_Left
letters_List = list(letters)
indexCheck = 1

#Index for ASCII Hangman body art
stages_index = 0

while chances:
    print(str(letters_List))
    while True:
        try:
            guess_Word = str(input("Guess the word or a letter: "))
            if stages_index < 10:
                print(stages[stages_index])
            break
        except ValueError:
            print("Please don't enter integers or floating numbers!")
    #if guess_Word:
    #    chances -= 1
    #    stages_index += 1
        
    if len(guess_Word) == 1:
        indexCheck = 0
        global indexCheck
        global chances
        #print(indexCheck)
        while indexCheck <= len(random_word) - 1:
            if guess_Word in list(random_word[indexCheck]):
                print("Guess word" + guess_Word)
                print("Index Check " + str(indexCheck))
                global guessed_number
                global letters_List
                chances += 1
                guessed_number += 1
                letters_List[indexCheck] = guess_Word
                #print(letters_List)
                if guessed_number != len(random_word):
                    print("You guessed a letter!")
                if indexCheck == len(random_word) - 1:
                    break
            indexCheck += 1

        """
        for l in list(random_word):
            if guess_Word in list(random_word[indexCheck]):
                print(l)
                global guessed_number
                global letters_List
                chances += 1
                guessed_number += 1
                letters_List[indexCheck] = guess_Word
                #print(letters_List)
                if guessed_number != len(random_word):
                    print("You guessed a letter!")
                if indexCheck == len(random_word) - 1:
                    break
            indexCheck += 1
        """
            
    if guess_Word != random_word and guess_Word not in list(random_word):
        chances -= 1
        stages_index += 1
    if stages_index == 10 and guessed_number != len(random_word):
        print("You lost!")
        break
    #Check if the user guessed all the letters       
    if guessed_number == len(random_word):
        print(str(letters_List))
        print("You guessed all the letters!")
        break
    #Check if the user guessed the whole word
    if guess_Word == random_word:
        print(str(letters_List))
        print("You guessed the word!")
        break
    #Print chances left if user
    elif guess_Word != random_word:
        print("You have " + str(chances) + " chances left!")
    
