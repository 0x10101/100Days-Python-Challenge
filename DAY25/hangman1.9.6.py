"""
Version 1.9.6
Changes:
    -Handles FileNotFoundError for random_words.txt
    - When the user for example enters "e" for the words 'Indepedent':
        instead of printing every time the program finds the letter and print the list like this
        You guessed a letter!
        ['I', '_', '_', 'e', '_', '_', '_', '_', '_', '_', '_']
        You guessed a letter!
        ['I', '_', '_', 'e', '_', 'e', '_', '_', '_', '_', '_']
        You guessed a letter!
        ['I', '_', '_', 'e', '_', 'e', '_', '_', 'e', '_', '_']
        
              instead it prints this:
          You guessed a letter!
          ['I', '_', '_', 'e', '_', 'e', '_', '_', 'e', '_', '_']
    -Fixed a bug where the functio pickWord() could generate an index out of range for
            words[index]
    
To-Do:
    -Redesign the code... what was I thinking when using so much global
       variable wtf -_-
    
"""

import random, sys

hangman_art = """
    __  __ ___     _   __ ______ __  ___ ___     _   __
   / / / //   |   / | / // ____//  |/  //   |   / | / /
  / /_/ // /| |  /  |/ // / __ / /|_/ // /| |  /  |/ / 
 / __  // ___ | / /|  // /_/ // /  / // ___ | / /|  /  
/_/ /_//_/  |_|/_/ |_/ \____//_/  /_//_/  |_|/_/ |_/   
 """

gameOver_art = """
 __   __            _              _   _ 
 \ \ / /__  _   _  | |    ___  ___| |_| |
  \ V / _ \| | | | | |   / _ \/ __| __| |
   | | (_) | |_| | | |__| (_) \__ \ |_|_|
   |_|\___/ \__,_| |_____\___/|___/\__(_)
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

try:
    file = open("random_words.txt", "r")
except FileNotFoundError:
    print("random_words.txt is needed for the program to run!")
    sys.exit()
    
#Make a list out of every word in file
words = list(file.read().split())

def pickWord():
    global random_word
    #Pick a random number for random_Index
    # use random_Index to pick a random word from the 'words' list
    rand_Index = random.randint(0,len(words)-1)
    random_word = words[rand_Index].title()
    #Number of guesses the user can make

def generateList():
    global letters_List
    global guessed_number
    #Testing purposes
    #print(random_word)
    guessed_number = 1
    randomMinusNumber = len(random_word) - guessed_number
    letters_Left = list(random_word)[0] + "_" * randomMinusNumber
    letters = letters_Left
    letters_List = list(letters)

def restart():
    print("Restarting...")
    global chances
    global guess_Word
    global guessed_Letters
    global tried_Letters
    guess_Word = ""
    pickWord()
    chances = 10
    indexCheck = 1
    guessed_Letters = []
    tried_Letters = []

def askPlay():
    global play
    global stages_index
    while True:
        play = input("Want to continue? y/N: ").lower().strip()
        if play == "y":
            restart()
            generateList()
            stages_index = 0
        elif play == "n":
            sys.exit()
        else:
            print("Chose a valid option!")
        break

def guessed_all_letters():
    if guessed_number == len(random_word):
        print(str(letters_List))
        print("You guessed all the letters!")
        askPlay()

tried_Letters = []
chances = 10

print(hangman_art)
print("--You have 10 guesses!--")


pickWord()
generateList()

#Index for ASCII Hangman body art
stages_index = 0
playing = True

while playing:
    while chances:
        print("The word is {}".format(random_word))
        print(str(letters_List))
        while True:
            try:
                guess_Word = str(input("Guess the word or a letter: ")).lower().strip()
                if stages_index < 10:
                    print(stages[stages_index])
                break
            except ValueError:
                print("Please don't enter integers or floating numbers!")
        if guess_Word: #not in tried_Letters   
            tried_Letters.append(guess_Word)
        #Testing purposes print(len(guess_Word))
        
        #Check if the user guessed the whole word
        if guess_Word == random_word.lower():
            print(str(letters_List))
            print("You guessed the word!")
            askPlay()
        
        print("Words/Letters you've already tried: ")
        print(*tried_Letters, sep=", ")
        if len(guess_Word) == 1:
            indexCheck = 0
            sameLetter = False
            #global indexCheck
            #global chances
            while indexCheck <= len(random_word) - 1:
                if guess_Word in list(random_word[indexCheck]):
                    #global guessed_number
                    #global letters_List
                    #global tried_Letters
                    #Testing purposes
                    #print("Guess word- " + guess_Word)
                    #print("Index Check " + str(indexCheck))
                    if guess_Word not in tried_Letters:
                        guessed_number += 1
                    letters_List[indexCheck] = guess_Word
                    tried_LettersMinusLast = tried_Letters
                    if not sameLetter and guessed_number != len(random_word) and guess_Word not in tried_Letters[:-1] and guess_Word == tried_Letters[-1]:
                        print("You guessed a letter!")
                    if indexCheck == len(random_word) - 1:
                        break
                    sameLetter = True
                indexCheck += 1
            if guess_Word in tried_Letters[:-1]:
                print("You've already guessed that letter!")
              
        if guess_Word != random_word and guess_Word not in list(random_word):
            chances -= 1
            stages_index += 1
        if stages_index == 10 and guessed_number != len(random_word):
            print("The word was: " + random_word)
            print(gameOver_art)
            sys.exit()
        #Check if the user guessed all the letters       
        if guessed_number == len(random_word) or letters_List == list(random_word):
            print(str(letters_List))
            print("You guessed all the letters!")
            askPlay()
