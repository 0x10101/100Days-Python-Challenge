"""

Version : 1.3
Words Counter

Changes
    -Exit the program after /q


"""

print("Words Counter!")
print("ENTER /q when you want to exit")

while True:
    words = 0
    foundFile = False
    characters = 0
    while not foundFile:
        try:
            fileLocation = input("File Location : ")
            if fileLocation.lower() == "/q":
                break
            with open(fileLocation, "r") as file:
                foundFile = True
        except OSError:
            print("---File not found!")
    if fileLocation.lower() == "/q":
        break
    with open(fileLocation,"r") as file:
        content = file.read()
        for word in content.split():
            words += 1
            for character in word:
                characters += 1
    print("The file has {} words and {} characters!".format(str(words),str(characters)))                                                         
