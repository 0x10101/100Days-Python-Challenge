"""
Version 2.1
Changes:
    -Changed all str(input(-/-)) to input(-/-)
    -Made a function register() that asks user for username, password
       and stores it in database so the user can login with it

Version 2.2
Changes:
    -Made a function responsible for checking if random_words.txt exists
       and if it doesn't then it creates it
    -When user is in register form he can enter /login to go back to login form
    -Created createDatabase() to check if database.py exists/has accounts
           TABLE and if it doesn't then it creates it
    -Created insertAccount(user,passw) for register()
    -Doesn't allow to /register with an taken username
    -Organized the code
    

To-Do:
    -Redesign the code... what was I thinking when using so much global
       variable wtf -_-
    -Add difficulty level
    -Add scoreboard
    -Register system
    -Fix updateAccount()
    -Fix "Only letters (from english vocabulary) please!" bug
        (Commented until fixed)
    -Fix bug "When user enters a uppercase letter it added stages_index +1
       even when the letter is in the word
    
"""

import random, sys, string, time, sqlite3
import fileHandling, login_system, database

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

#Function from hangman_functions
fileHandling.check_randomWFile()
    
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

        

"""Commented until fixed!
def updateAccount():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    print(logged_in)
    c.execute("UPDATE accounts SET score=logged_in[3] WHERE name=logged_in[1]")
    print(logged_in)
    c.close()
    print(logged_in)
"""
        


def showHelp():
    if logged_in[0] == True:
        print("""
        /register to create an account if you don't have one already
        /logout to log out of your account
        /exit to exit the program
        /score to see your score
        /help to show these cmd options
        /account to show your account info
        """)
    else:
        print("""
        /register to create an account if you don't have one already
        """)



tried_Letters = []
chances = 10

print(hangman_art)

pickWord()
generateList()

#Index for ASCII Hangman body art
stages_index = 0
playing = True

#register()

#Create database.db if it doesn't exist
database.createDatabase()

logged_in = login_system.login()
showHelp()

cmdOptions = ["/help","/exit","/score","/logout","/profile",
				"/account","/register","/printword"]
while logged_in[0] and chances:
    #print("The word is {}".format(random_word))
    print(str(letters_List))
    #updateAccount()
    while True:
        try:
            guess_Word = input("Guess the word or a letter: ").lower().strip()
            if guess_Word == "/logout":
                logged_in[0] = False
                print("Logged out successfully!")
                break
            elif guess_Word == "/help":
                showHelp()
            elif guess_Word == "/exit":
                print("Any data that hasn't been saved will be erased!")
                permission = input("Are you sure you want to continue?Y/n :")
                if permission.lower() == "y":
                    sys.exit()
            elif guess_Word == "/score":
                print("Your score is {}".format(logged_in[4]))
            elif guess_Word == "/account":
                login_system.accountInfo(logged_in[1],logged_in[2],
                                         "*" * len(logged_in[3]),logged_in[4])
            elif guess_Word == "/register":
                print("You can't create an account while logged in!")
            #hidden cmd option
            elif guess_Word == "/printword":
                print("The word you have to guess is {} ...".format(random_word))
            if stages_index < 10:
                print(stages[stages_index])
                break
            #Commented until I fix it
            #if guess_Word in list(string.ascii_letters):
            #    break
            #else:
            #    print("Only letters (from english vocabulary) please!")
        except ValueError:
            print("Please don't enter integers or floating numbers!")
    if logged_in[0]:
        if guess_Word and guess_Word not in cmdOptions : #not in tried_Letters (removed)  
            tried_Letters.append(guess_Word)
        #Testing purposes print(len(guess_Word))
        
        #Check if the user guessed the whole word
        if guess_Word == random_word.lower():
            print(str(letters_List))
            print("You guessed the word!")
            earnedPoints = 100 * len(guess_Word)
            logged_in[4] = logged_in[4] + earnedPoints
            print("You guessed all the letters and earned {} points!".format(earnedPoints))
            earnedPoints = 0
            askPlay()
        
        print("Words/Letters you've already tried: ")
        print(*tried_Letters, sep=", ")
        if len(guess_Word) == 1:
            indexCheck = 0
            sameLetter = False
            while indexCheck <= len(random_word) - 1:
                if guess_Word in list(random_word[indexCheck]):
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
            if guess_Word not in cmdOptions:
                chances -= 1
                stages_index += 1
        if stages_index == 10 and guessed_number != len(random_word):
            print("The word was: " + random_word)
            print(gameOver_art)
            sys.exit()
        #Check if the user guessed all the letters       
        if guessed_number == len(random_word) or letters_List == list(random_word):
            print(str(letters_List))
            earnedPoints = 100 * len(guess_Word)
            logged_in[4] = logged_in[4] + earnedPoints
            print("You guessed all the letters and earned {} points!".format(earnedPoints))
            earnedPoints = 0
            askPlay()
    else:
        logged_in = login_system.login()


