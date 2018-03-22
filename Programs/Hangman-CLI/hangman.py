"""
Version 2.2
Changes:
    -Made a function responsible for checking if random_words.txt exists
       and if it doesn't then it creates it
    -When user is in register form he can enter /login to go back to login form
    -Created createDatabase() to check if database.py exists/has accounts
           TABLE and if it doesn't then it creates it
    -Created insertAccount(user,passw) for register()
    -100 * len(random_word) instead of 100 * len(guess_Word)
    -Score is saved on database now
    -The programs runs database.showScoreboard when cmd option /scoreboard is
         entered.
    -Created hidden cmd option /value to print out "value" dict
    -Organized the code

Version 2.3
Changes:
    -/account shows your level
    -After the user loses it doesn't sys.exit() after printing gameOver_art
    -Doesn't ask "Want to continue? y/N: " anymore
    

To-Do:
    -Redesign the code... what was I thinking when using so much global
       variable wtf -_-
    -Add difficulty level
    -Fix "Only letters (from english vocabulary) please!" bug
        (Commented until fixed)
    -Fix bug "When user enters a uppercase letter it added stages_index +1
       even when the letter is in the word
    -Fix /deleteAccount cmd option "Guss the word or a letter" bug
    
"""

import random, sys, string, time, sqlite3
import fileHandling, login_system, database#, level_system

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

def restart(dict_):
    #print("Restarting...")
    dict_["guess_Word"]
    pickWord()
    dict_["chances"] = 10
    dict_["indexCheck"] = ""
    dict_["guessed_Letters"] = []
    dict_["tried_Letters"]  = []
    dict_["stages_index"] = 0
    return dict_

#def restart():
#    generateList()


def guessed_all_letters():
    if guessed_number == len(random_word):
        print(str(letters_List))
        print("You guessed all the letters!")
        generateList()
        restart(value)
        

def showHelp():
    if logged_in[0] == True:
        print("""
        /logout to log out of your account
        /register to create an account if you don't have one already
        /account to show your account info
        /deleteAccount
        /score to see your score
        /help to show these cmd options
        /scoreboard to show Scoreboard
        /exit to exit the program       
        """)
    else:
        print("""
        /register to create an account if you don't have one already
        """)


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

value = {"chances":10,"guess_Word":"","guesed_Letters":[],
                      "tried_Letters":[],"stages_index":0}

cmdOptions = ["/help","/exit","/score","/logout","/profile","/scoreboard",
				"/account","/register","/printword",
                                "/value","/deleteaccount"]
while logged_in[0] and value["chances"]:
    #print("The word is {}".format(random_word))
    print(str(letters_List))
    #updateAccount()
    while True:
        try:
            value["guess_Word"] = input("Guess the word or a letter: ").lower().strip()
            if value["guess_Word"] == "/logout":
                logged_in[0] = False
                print("Logged out successfully!")
                break
            elif value["guess_Word"] == "/help":
                showHelp()
            elif value["guess_Word"] == "/exit":
                print("Any data that hasn't been saved will be erased!")
                permission = input("Are you sure you want to continue?Y/n :")
                if permission.lower() == "y":
                    sys.exit()
            elif value["guess_Word"] == "/score":
                print("Your score is {}".format(logged_in[4]))
            elif value["guess_Word"] == "/account":
                login_system.accountInfo(logged_in[1],logged_in[2],
                                         "*" * len(logged_in[3]),logged_in[4],logged_in[5])
            elif value["guess_Word"] == "/register":
                print("You can't create an account while logged in!")
            elif value["guess_Word"] == "/scoreboard":
                database.showScoreboard()
            elif value["guess_Word"] == "/deleteaccount":
                logged_in[0] = database.deleteAccount(logged_in[1])
            #hidden cmd option
            elif value["guess_Word"] == "/printword":
                print("The word you have to guess is {} ...".format(random_word))
            elif value["guess_Word"] == "/value":
                print(value)
            ##############
            if stages_index < 10 and logged_in[0]:
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
        if value["guess_Word"] and value["guess_Word"] not in cmdOptions : #not in tried_Letters (removed)  
            value["tried_Letters"].append(value["guess_Word"])
        #Testing purposes print(len(guess_Word))
        
        #Check if the user guessed the whole word
        if value["guess_Word"] == random_word.lower():
            print(str(letters_List))
            print("You guessed the word!")
            earnedPoints = 100 * len(random_word)
            logged_in[4] = logged_in[4] + earnedPoints
            print("You guessed all the letters and earned {} points!".format(earnedPoints))
            database.addScore(logged_in[4],logged_in[2])
            print(logged_in[4],logged_in[2])
            print(logged_in)
            earnedPoints = 0
            value = restart(value)
            restart(value)
            generateList()
        
        print("Words/Letters you've already tried: ")
        print(*value["tried_Letters"], sep=", ")
        if len(value["guess_Word"]) == 1:
            indexCheck = 0
            sameLetter = False
            while indexCheck <= len(random_word) - 1:
                if value["guess_Word"] in list(random_word[indexCheck]):
                    #Testing purposes
                    #print("Guess word- " + guess_Word)
                    #print("Index Check " + str(indexCheck))
                    if value["guess_Word"] not in value["tried_Letters"]:
                        guessed_number += 1
                    letters_List[indexCheck] = value["guess_Word"]
                    tried_LettersMinusLast = value["tried_Letters"]
                    if not sameLetter and guessed_number != len(random_word):
                        if value["guess_Word"] not in value["tried_Letters"][:-1]:
                            if value["guess_Word"] == value["tried_Letters"][-1]:
                                print("You guessed a letter!")
                    if indexCheck == len(random_word) - 1:
                        break
                    sameLetter = True
                indexCheck += 1
            if value["guess_Word"] in value["tried_Letters"][:-1]:
                print("You've already guessed that letter!")
              
        if value["guess_Word"] != random_word and value["guess_Word"] not in list(random_word):
            if value["guess_Word"] not in cmdOptions:
                value["chances"] -= 1
                stages_index += 1
        if stages_index == 10 and guessed_number != len(random_word):
            print("The word was: " + random_word)
            print(gameOver_art)
            restart(value)
            generateList()
        #Check if the user guessed all the letters       
        if guessed_number == len(random_word) or letters_List == list(random_word):
            print(str(letters_List))
            earnedPoints = 100 * len(random_word)
            logged_in[4] = logged_in[4] + earnedPoints
            print("You guessed all the letters and earned {} points!".format(earnedPoints))
            earnedPoints = 0
            database.addScore(logged_in[4],logged_in[2])
            value = restart(value)
            restart(value)
            generateList()
    else:
        logged_in = login_system.login()


