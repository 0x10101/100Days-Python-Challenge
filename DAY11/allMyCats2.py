"""
My version
"""

catNames = []

print("Type /names when you finished putting the names of your cats!")
order = 1
while True:
    catName_input = input("Cat " + str(order) + " : ")
    order += 1
    if catName_input == "/names":
        print("Your cat names are :")
        for item in catNames:   
            print(item, end=" " )
        break
    else:
        catNames.insert(-1,catName_input)
