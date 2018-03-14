"""

Version : 1.2
Words Counter

Changes:
    -After typing the file location it shows how many characters the file
       contains.


"""

print("Words Counter!")


while True:
    words = 0
    foundFile = False
    characters = 0
    while not foundFile:
        try:
            fileLocation = input("File Location : ")
            with open(fileLocation, "r") as file:
                foundFile = True
        except OSError:
            print("---File not found!")
    with open(fileLocation,"r") as file:
        content = file.read()
        for word in content.split():
            words += 1
            for character in word:
                characters += 1
    print("The file has {} words and {} characters!".format(str(words),str(characters)))                                                         
    true = input("---ENTER to exit")
    if not true:
        break
