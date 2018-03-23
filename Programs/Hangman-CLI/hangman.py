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
    -Fixed bug where stages_index was used instead of value["stages_index"]
       accidentally unnoticed which introduced some unusual behavior
    -Created /staged_index and /logged_in hidden cmd option
    -Prints youWon_art when the user guessed the word 
    -pickWord() returns word instead of changing with globals random_word
    -generateList() returns letters_List value instead of changing with globals 
             letters_List
    -Moved all the variables containing ascii art in ascii_art.py
    -Fixed a bug where after deleting your account user woulds still be logged in
    -Removed all globals
    -40 * len(random_word) instead of 100 * len(random_word)
    -Used level_system functions on the while loop
    -Changed print(letters_List) to print(*letters_List, sep=" ")

    

To-Do:
    -Add difficulty level
    -Fix "Only letters (from english vocabulary) please!" bug
        (Commented until fixed)
    -Fix bug where for t
    -Fix /deleteAccount cmd option "Guss the word or a letter" bug
    
"""

import random, sys, string, time, sqlite3
import fileHandling, login_system, database, level_system
from ascii_art import *
import console

#Function from hangman_functions
fileHandling.check_randomWFile()
    
#Make a list out of every word in file
with open("random_words.txt","r") as file:
    words = list(file.read().split())

def pickWord():
    #Pick a random number for random_Index
    # use random_Index to pick a random word from the 'words' list
    rand_Index = random.randint(0,len(words)-1)
    word = words[rand_Index].title()
    return word

def generateList():
    #Testing purposes
    #print(random_word)
    randomMinusNumber = len(random_word) - value["guessed_number"]
    letters_Left = list(random_word)[0] + "_" * randomMinusNumber
    letters = letters_Left
    letters_List = list(letters)
    return letters_List

def restart(dict_):
    #print("Restarting...")
    dict_["guess_Word"]
    random_word = pickWord()
    dict_["chances"] = 10
    dict_["indexCheck"] = ""
    dict_["guessed_Letters"] = []
    dict_["tried_Letters"]  = []
    dict_["stages_index"] = 0
    dict_["guessed_number"] = 1
    return dict_
        

value = {"chances":10,"guess_Word":"","guesed_Letters":[],
                      "tried_Letters":[],"stages_index":0,
                      "guessed_number":1}

cmdOptions_list = ["/help","/exit","/score","/logout","/profile","/scoreboard",
                  "/account","/register","/printword","/stages_index",
                              "/logged_in","/value","/deleteaccount",
                              "/levels"]

print(hangman_art)

#Create database.db if it doesn't exist
database.createDatabase()

random_word = pickWord()
letters_List = generateList()


logged_in = login_system.login()
showHelp()

while logged_in[0] and value["chances"]:
    #print("The word is {}".format(random_word))
    print(*letters_List, sep=" ")
    #updateAccount()
    while True:
        pastLevel = level_system.checkLevel(logged_in[4])
        try:
            value["guess_Word"] = input("Guess the word or a letter: ").lower().strip()
            logged_in[0] = console.checkOption(True,value["guess_Word"],logged_in)
            if not logged_in[0]:
              break
            if value["stages_index"] < 10 and logged_in[0]:
                print(stages[value["stages_index"]])
                break
            #Commented until I fix it
            #if guess_Word in list(string.ascii_letters):
            #    break
            #else:
            #    print("Only letters (from english vocabulary) please!")
        except ValueError:
            print("Please don't enter integers or floating numbers!")
    if logged_in[0]:
        if value["guess_Word"] and value["guess_Word"] not in cmdOptions_list : #not in tried_Letters (removed)  
            value["tried_Letters"].append(value["guess_Word"])
        #Testing purposes print(len(guess_Word))
        
        #Check if the user guessed the whole word
        if value["guess_Word"] == random_word.lower():
            print(str(letters_List))
            print("You guessed the word!")
            earnedPoints = 40 * len(random_word)
            logged_in[4] = logged_in[4] + earnedPoints
            print("You guessed all the letters and earned {} points!".format(earnedPoints))
            print(youWon_art)
            database.addScore(logged_in[4],logged_in[2])
            #print(logged_in[4],logged_in[2])
            #print(logged_in)
            earnedPoints = 0
            value = restart(value)
            random_word = pickWord()
            letters_List = generateList()
        
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
                    if not sameLetter and value["guessed_number"] != len(random_word):
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
            if value["guess_Word"] not in cmdOptions_list:
                value["chances"] -= 1
                value["stages_index"] += 1
        if value["stages_index"] == 10 and value["guessed_number"] != len(random_word):
            print("The word was: " + random_word)
            print(gameOver_art)
            value = restart(value)
            random_word = pickWord()
            letters_List = generateList()
        #Check if the user guessed all the letters       
        if value["guessed_number"] == len(random_word) or letters_List == list(random_word):
            print(str(letters_List))
            earnedPoints = 40 * len(random_word)
            logged_in[4] = logged_in[4] + earnedPoints
            print("You guessed all the letters and earned {} points!".format(earnedPoints))
            print(youWon_art)
            earnedPoints = 0
            database.addScore(logged_in[4],logged_in[2])
            value = restart(value)
            random_word = pickWord()
            letters_List = generateList()
    else:
        logged_in = login_system.login()
    currentLevel = level_system.checkLevel(logged_in[4])
    logged_in[5] = level_system.updateLevel(pastLevel,currentLevel)


