"""

GOAL

Create a program that prints out every line to the song "99 bottles of beer on the wall." This
should be a pretty simple program, so to make it a bit harder, here are some rules to follow.

RULES

If you are going to use a list for all of the numbers, do not manually type them all in.
Instead, use a built in function.

Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.

Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

Put a blank line between each verse of the song.

Developer : Gjergj Kadriu
Version : 1.0

"""

bottles = 99
print("Lyrics of the song 99 Bottles of Beer")
while bottles:
    if bottles == 1:
        print(str(bottles) + " bottle of beer on the wall," + str(bottles)
                  + " bottle of beer.")
        bottles -= 1
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    else:
        print(str(bottles) + " bottles of beer on the wall," + str(bottles)
              + " bottles of beer.")
        bottles -= 1
        print("Take one down and pass it around," + str(bottles)
                + " bottles of beer on the wall\n")

print("\nNo more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
        

    
    
