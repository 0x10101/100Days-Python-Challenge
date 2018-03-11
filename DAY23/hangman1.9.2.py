"""

Version 1.9.2

Changes:
    -Removed the global variables, replaced them with function arguments
To-Do:
    -Fix the bugs that came with replacing global variables with func arg :P
    -Find a way to use this piece of code right after the user input is taken
    "if guess_Word not in tried_Letters:    
       tried_Letters.append(guess_Word)"
    -Fix this output
         You guessed a letter!
         You've already guessed that letter!
    
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



#Make a list out of every word in file
filename = "random_words.txt"
with open(filename,"r") as file:
    words = list(file.read().split())

tried_Letters = []
chances = 10
#random_word = ""
guessed_number = 1
letters_List = []
rand_Index = random.randint(0,len(words))

#Index for ASCII Hangman body art
stages_index = 0
playing = True
play = ""


#ranWord = random_word
#wordsList = words
def pickWord(wordsList,index):
    #Pick a random number for random_Index
    # use random_Index to pick a random word from the 'words' list
    random_word = wordsList[index].title()
    #Number of guesses the user can make
    print("words : " + random_word)
    return random_word

#res - equals - guessed_number
#letList - equals - letters_List
def generateList(res,letList):
    #Testing purposes
    #print(random_word)
    res = 1
    randomMinusNumber = len(random_word) - res
    letters_Left = list(random_word)[0] + "_" * randomMinusNumber
    letters = letters_Left
    letList = list(letters)

#res1,res2,res3,res4,res5,res6 used for restarting the values after
    #the user wants to continue playing
def restart(res1,res2,res3,res4,res5):
    print("Restarting...")
    res1 = "" #guess_Word
    pickWord(random_word)
    res2 = 10 #chances
    res3 = 1 #indexCheck
    res4 = [] #guessed_Letters
    res5 = 0 #stages_index

def askPlay(playInput):
    while True:
        playInput = input("Want to continue? y/N: ").lower().strip()
        if play == "y":
            restart(guess_Word,chances,indexCheck,
                         guessed_Letters,stages_index)
            generateList(guessed_number,letters_List)
        elif play == "n":
            sys.exit()
        else:
            print("Chose a valid option!")
        break

def guessed_all_letters():
    if guessed_number == len(random_word):
        print(str(letters_List))
        print("You guessed all the letters!")
        askPlay(play)

print(hangman_art)
print("--You have 10 guesses!--")


pickWord(words,rand_Index)
generateList(guessed_number,letters_List)



while playing:
    while chances:
        print(str(letters_List))
        while True:
            try:
                guess_Word = str(input("Guess the word or a letter: ")).lower().strip()
                if stages_index < 10:
                    print(stages[stages_index])
                break
            except ValueError:
                print("Please don't enter integers or floating numbers!")
        if guess_Word not in tried_Letters:    
            tried_Letters.append(guess_Word)
        #Testing purposes print(len(guess_Word))
        print("Words/Letters you've already tried: ")
        print(*tried_Letters, sep=", ")
        if len(guess_Word) == 1:
            indexCheck = 0
            #global indexCheck
            #global chances
            print("(Testing) The word is :" + random_word)
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
                    print(letters_List)
                    if guessed_number != len(random_word):
                        print("You guessed a letter!")
                    if indexCheck == len(random_word) - 1:
                        break
                indexCheck += 1
            if guess_Word in letters_List:
                print("You've already guessed that letter!")
              
        if guess_Word != random_word and guess_Word not in list(random_word):
            chances -= 1
            stages_index += 1
        if stages_index == 10 and guessed_number != len(random_word):
            print("The word was: " + random_word)
            print(gameOver_art)
            sys.exit()
        #Check if the user guessed all the letters       
        if guessed_number == len(random_word):
            print(str(letters_List))
            print("You guessed all the letters!")
            askPlay(play)
            
        #Check if the user guessed the whole word
            if guess_Word == random_word.lower():
                print(str(letters_List))
                print("You guessed the word!")
                askPlay(play)
    
