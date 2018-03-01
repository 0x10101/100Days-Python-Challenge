"""

Bonus Points on 9th grade test!
Developer : Gjergj Kadriu
Version : 1.0

Handwrited

"""

def classf(classesSum,classes):
    global classA
    classA = classesSum / classes
    print("Average: " + str(classA))

print("Class 6")
classes = float(input("How many classes? : "))
classesSum = float(input("Sum of the grades of the classes : "))
classf(classesSum,classes)
class1 = classA

print("Class 7")
classes = float(input("How many classes? : "))
classesSum = float(input("Sum of the grades of the classes : "))
classf(classesSum,classes)
class2 = classA

print("Class 8")
classes = float(input("How many classes? : "))
classesSum = float(input("Sum of the grades of the classes : "))
classf(classesSum,classes)
class3 = classA

print("Class 9")
classes = float(input("How many classes? : "))
classesSum = float(input("Sum of the grades of the classes : "))
classf(classesSum,classes)
class4 = classA

bonusPoints = (class1 + class2 + class3 + class4) / 4 * 5
print("You'll have " + str(bonusPoints) + " extra points in the exam")





