import sys, login_system, database

def showHelp(loggedIn):
    if loggedIn:
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

def checkOption(loggedIn,guess_Word,accountInfo,score):
    if loggedIn:
        if guess_Word == "/logout":
            loggedIn = False
            print("Logged out successfully!")
        elif guess_Word == "/help":
            showHelp(True)
        elif guess_Word == "/score":
            print("Your score is {}".format(score))
        elif guess_Word == "/account":
            login_system.accountInfo(accountInfo[1],accountInfo[2],
                                     "*" * len(accountInfo[3]),
                                     accountInfo[4],accountInfo[5])
        elif guess_Word == "/register":
            print("You can't create an account while logged in!")
        elif guess_Word == "/deleteaccount":
            logged_in[0] = database.deleteAccount(logged_in[1])
            loggedIn = False
    elif not loggedIn:
        if guess_Word == "/register":
            login_system.register()
    
    if guess_Word == "/scoreboard":
        database.showScoreboard()
    #hidden cmd option
    elif guess_Word == "/printword":
        print("The word you have to guess is {} ...".format(random_word))
    elif guess_Word == "/value":
        print(value)
    elif guess_Word == "/stages_index":
        print("value['stages_index'] = {}".format(value["stages_index"]))
    elif guess_Word == "/logged_in":
        print("logged_in = {}".format(logged_in))
    elif guess_Word =="/levels":
        print(level_system.generateLevel())
    elif guess_Word == "/exit":
        permission = input("Are you sure you want to continue?Y/n :")
        if permission.lower() == "y":
            sys.exit()
    ##############
    return loggedIn