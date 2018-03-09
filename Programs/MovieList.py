"""

Version : 1.0

Something to keep track of the movies I would like to watch later...

"""

import os

try:
    file = open("movieList.txt","r+")
except FileNotFoundError:
    print("Creating file..")
    file = open("movieList.txt","w")
    file = open("movieList.txt","r+")

    

print("Movies to Watch:")
print(*file, sep="\n")

print("""
Console options:
-add
-reset
-quit
-movies
""")

while True:
    console = input("Console :")
    if console == "add".lower():
        addMovie = input("Name of the movie:").title()
        file.write(addMovie)
        print("Movie added!")
    elif console == "quit".lower():
        break
    elif console == "reset".lower():
        print("Deleting file..")
        os.remove("movieList.txt")
        print("Creating file..")
        file = open("movieList.txt","w")
        file = open("movieList.txt","r+")
        print("Successfully erased the list!")
    elif console == "movies".lower():
        print("Movies to Watch:")
        print(*file, sep="\n")

file.close()
    
    
    
