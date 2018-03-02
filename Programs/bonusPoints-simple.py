"""

Bonus Points on 9th grade test!
Developer : Gjergj Kadriu
Version : 1.1

Changes:
    Blahh.. just made it less repetetive
"""

cl = 6

def classf(classesSum,classes):
    global classA
    classA = classesSum / classes
    print("Average: " + str(classA))

def askUser():
    global cl
    global classes
    global classesSum
    print("Class " + str(cl))
    classes = float(input("How many classes? : "))
    classesSum = float(input("Sum of the grades of the classes : "))
    cl += 1

askUser()
classf(classesSum,classes)
class1 = classA

askUser()
classf(classesSum,classes)
class2 = classA

askUser()
classf(classesSum,classes)
class3 = classA

askUser()
classf(classesSum,classes)
class4 = classA

bonusPoints = (class1 + class2 + class3 + class4) / 4 * 5
print("You'll have " + str(bonusPoints) + " extra points in the exam")





