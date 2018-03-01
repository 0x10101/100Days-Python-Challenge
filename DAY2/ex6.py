# put 10 in a variable and use it on the x variable
types_of_people = 10
x = f"There are {types_of_people} types of people"

# put some data on the var binary and do_not and use it in y variable
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# print x and y in seperate lines
print(x)
print(y)

# print using f-string 
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny! {}"

print(joke_evaluation.format(hilarious))

# store strings on a variable
w = "This is the left side of..."
e = "a string with a right side."

# print the result of merging variable w and e
print(w + e)
