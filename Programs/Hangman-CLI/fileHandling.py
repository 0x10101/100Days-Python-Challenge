import time, random

#Make a list out of every word in file
with open("random_words.txt","r") as file:
    words = list(file.read().split())

def pickWord():
    #Pick a random number for random_Index
    # use random_Index to pick a random word from the 'words' list
    rand_Index = random.randint(0,len(words)-1)
    word = words[rand_Index].title()
    return word

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
