"""

Version : 1.0
Words Counter

#I am supposed to memorize a bunch of useless things right now instead of procrastinating -_-

"""

print("Words Counter!")


while True:
    words = 0
    foundFile = False
    while not foundFile:
        try:
            fileLocation = input("File Location : ")
            file = open(fileLocation, "r")
            foundFile = True
        except OSError:
            print("---File not found!")
    content = file.read()
    for i in content.split():
        words += 1
    print("The file has " + str(words) + " words!")
    true = input("---ENTER to exit")
    if not true:
        break
