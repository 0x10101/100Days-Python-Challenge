import random

""""words_list = ["wood","ball","dog","cat","shit","complex"]
#words_list = ["dog","dog","dog","dog","dog","dog"]
rand_Index = random.randint(0,5)
"""
words_list = input("Fjala: ")
random_word = words_list[words_list]

chances = 5

print("---Hangman Game---")
print("--You have 5 guesses!--")
print("--If you want to type a letter you can predict only the next letter!")
      
#Testing purposes
#print(random_word)
guessed_letters = [list(random_word)[0]]
guessed_number = 1
randomMinusNumber = len(random_word) - guessed_number
letters_Left = guessed_letters[0] + "_" * randomMinusNumber
letters = letters_Left
letters_List = list(letters)
indexCheck = 1

while chances:
    print(str(letters_List))
    while True:
        try:
            guess_Word = str(input("Guess the word or a letter: "))
            break
        except ValueError:
            print("Please don't enter integers or floating numbers!")
    if guess_Word:
        chances -= 1
    if len(guess_Word) == 1:
        global indexCheck
        global chances
        #print(indexCheck)
        for l in list(random_word):
            if guess_Word in list(random_word[indexCheck]):
                print(l)
                global guessed_number
                global letters_List
                print("You guessed a letter!")
                chances += 1
                guessed_number += 1
                letters_List[indexCheck] = guess_Word
                print(letters_List)
                indexCheck += 1
                break
            
    if guessed_number == len(random_word):
        print("You guessed all the letters!")
        break
    if guess_Word == random_word:
        print("You guessed the word!")
        break
    elif guess_Word != random_word:
        print("You have " + str(chances) + " chances left!")
