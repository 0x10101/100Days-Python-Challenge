"""
Version 1.9.8
Changes:
    -The program depends on database.db for accouunts data
    -Added accounts system

To-Do:
    -Redesign the code... what was I thinking when using so much global
       variable wtf -_-
    -Add difficulty level
    -Add scoreboard
    -Register system
    
"""

import random, sys, string, time, sqlite3

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
    time.sleep(0.3)
    print("Creating random_words.txt")
    file = open("random_words.txt","w")
    time.sleep(0.3)
    print("Inserting random words in it...") 
    file.write("""
acres
adult
advice
arrangement
attempt
August
Autumn
border
breeze
brick
calm
canal
Casey
cast
chose
claws
coach
constantly
contrast
cookies
customs
damage
Danny
deeply
depth
discussion
doll
donkey
Egypt
Ellen
essential
exchange
exist
explanation
facing
film
finest
fireplace
floating
folks
fort
garage
grabbed
grandmother
habit
happily
Harry
heading
hunter
Illinois
image
independent
instant
January
kids
label
Lee
lungs
manufacturing
Martin
mathematics
melted
memory
mill
mission
monkey
Mount
mysterious
neighborhood
Norway
nuts
occasionally
official
ourselves
palace
Pennsylvania
Philadelphia
plates
poetry
policeman
positive
possibly
practical
pride
promised
recall
relationship
remarkable
require
rhyme
rocky
rubbed
rush
sale
satellites
satisfied
scared
selection
shake
shaking
shallow
shout
silly
simplest
slight
slip
slope
soap
solar
species
spin
stiff
swung
tales
thumb
tobacco
toy
trap
treated
tune
University
vapor
vessels
wealth
wolf
zoo
""")
    file.close()
    time.sleep(0.3)
    print("Done.")
    
#Make a list out of every word in file
with open("random_words.txt","r") as file:
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

def login():
    username = str(input("Username: ")).lower()
    password = str(input("Password: ")).lower()
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    for account in c.execute("SELECT * from accounts"):
        #Prints username and password for every row in account table
        #print(account[1],account[2])
        if username == account[1] and password == account[2]:
            return True
    

tried_Letters = []
chances = 10

print(hangman_art)
print("--You have 10 guesses!--")


pickWord()
generateList()

#Index for ASCII Hangman body art
stages_index = 0
playing = True

logged_in = login()

while logged_in:
    while playing:
        while chances:
            print("The word is {}".format(random_word))
            print(str(letters_List))
            while True:
                try:
                    guess_Word = str(input("Guess the word or a letter: ")).lower().strip()
                    if stages_index < 10:
                        print(stages[stages_index])
                    if guess_Word in list(string.ascii_letters):
                        break
                    else:
                        print("Only letters (from english vocabulary) please!")
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
