import time



timeout = time.time() + 60

words_file = open('words.txt', 'r')
words_content = words_file.read()


WPM = 0
print("Typing Test!")
while True:
    for words in words_content.split():
        print(words)
        word = input("Type : ")
        if word == words:
            WPM += 1
        if time.time() > timeout:
            break
    print("Your speed is " + str(WPM) + "WPM")
    break
