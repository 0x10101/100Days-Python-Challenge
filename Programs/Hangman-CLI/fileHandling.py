"""
Version 1.1
Changes:
    -Handled 
        FileNotFoundError: [Errno 2] No such file or 
        directory: 'random_words.txt'
"""


import time, random

#Make a list out of every word in file
def createWordsList(wordsList):
    with open("random_words.txt","r") as file:
        wordsList = list(file.read().split())
    return wordsList

def pickWord(wordsL,wordVar):
    #Pick a random number for random_Index
    # use random_Index to pick a random word from the 'words' list
    rand_Index = random.randint(0,len(wordsL)-1)
    wordVar = wordsL[rand_Index].title()
    return wordVar

def check_randomWFile():
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
