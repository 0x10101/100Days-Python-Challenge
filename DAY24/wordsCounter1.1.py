"""

Version : 1.1
Words Counter

Changes:
    -Handled text files better


"""

print("Words Counter!")


while True:
    words = 0
    foundFile = False
    while not foundFile:
        try:
            fileLocation = input("File Location : ")
            with open(fileLocation, "r") as file:
                foundFile = True
        except OSError:
            print("---File not found!")
    with open(fileLocation,"r") as file:
        content = file.read()
        for i in content.split():
            words += 1
    print("The file has " + str(words) + " words!")
    true = input("---ENTER to exit")
    if not true:
        break
