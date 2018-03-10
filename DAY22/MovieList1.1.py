"""

Version : 1.1

Changes:
    -Made functions for each console command except for -quit
    -Fixed a bug where the -movies command didn't update after adding
          a new movie name
    -If deleteFile() is called but file doesn't exist then it doesn't
          crash the program with a FileNotFoundError
"""

import os


print("""
Console commands:
-add
-reset
-quit
-movies
""")


def showMovies():
    print()
    print("Movies to watch:")
    with open("movieList.txt") as file:
        content = file.read()
        print(content)
    print()

def deleteFile():
    print("Deleting the list..")
    try:
        os.remove("movieList.txt")
    except FileNotFoundError:
        pass

def createFile():
    print("Creating list..")
    file = open("movieList.txt","w")
    file.close()
    print("Successfully created the new list!")

def addMovie(name):
    with open("movieList.txt", "a") as file:
        file.write("\t-" + name + "\n")
        print("Movie added!")    

try:
    with open("movieList.txt") as file:
        pass
except FileNotFoundError:
    createFile()

while True:
    console = input("Console :")
    if console == "add".lower():
        nameMovie = input("Name of the movie: ").title()
        addMovie(nameMovie)
    elif console == "quit".lower():
        break
    elif console == "reset".lower():
        deleteFile()
        createFile()
    elif console == "movies".lower():
        showMovies()

    
    
    
