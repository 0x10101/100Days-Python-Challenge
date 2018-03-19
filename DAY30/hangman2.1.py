"""
Version 2.0
Changes:
    -User can enter /help to get a list of cmd options
    -User can enter /exit to exit the program
    -After the user enters /exit it asks if he's sure he wants to procced
    -User can enter /account to show his account informations

Version 2.1
Changes:
    -Changed all str(input(-/-)) to input(-/-)
    -Made a function register() that asks user for username, password
       and stores it in database so the user can login with it

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
    print("""
    /register to create an account if you don't have one already
    """)
    while True:
        username = input("Username: ").lower()
        if username == "/register":
            register()
        password = input("Password: ").lower()
        if password == "/register":
            register()
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        access = [False,0,"","",0]
        for account in c.execute("SELECT * from accounts"):
            #Prints username and password for every row in account table
            #print(account[1],account[2])
            if username == account[1] and password == account[2]:
                #accounts[3] is the score
                print(account[3])
                access = [True,account[0],account[1],account[2],account[3]]
        if access[0]:
            print("Logged in successfully!")
            break
        else:
            print("Username or Password is wrong!")
        conn.close() #Closes the database connection
    print(access)
    return access

def register():
    while True:
        print("Register an account!")
        username = input("Create Username: ").lower()
        password = input("Create Password: ").lower()
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("""INSERT INTO accounts(username,password)
                   VALUES(?,?)""", (username,password))
        conn.commit()
        for account in c.execute("SELECT * from accounts"):
            for value in account:
                print(value)
        conn.close()
        print("Account successfully registered. Please log in!")
        login()
        break
        

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


def accountInfo():
    print("""
    ID : {}
    Username : {}
    Password : {}
    Score : {}
    """.format(logged_in[1],logged_in[2],"*" * len(logged_in[3]),logged_in[4]))



tried_Letters = []
chances = 10

print(hangman_art)
print("--You have 10 guesses!--")


pickWord()
generateList()

#Index for ASCII Hangman body art
stages_index = 0
playing = True

#register()


logged_in = login()
showHelp()

cmdOptions = ["/help","/exit","/score","/logout","/profile","/account","/register"]
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
                accountInfo()
            elif guess_Word == "/register":
                print("You can't create an account while logged in!")
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
        logged_in = login()


