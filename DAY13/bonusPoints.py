"""

Developer : Gjergj Kadriu
Version : 2.0
Last Update : 02.03.2018

"""


classes6 = ["Gjuhe Shqipe","Gjuhe Angleze","Matematike","Biologji","Fizike","Histori","Gjeografi"
           ,"Edukate Qytetare","Edukate Muzikore","Edukate Figurative","Teknologji/TIK"
           ,"Edukate Fizike","Etike"]

classes789 = ["Gjuhe Shqipe","Gjuhe Angleze","Matematike","Biologji","Fizike","Histori","Gjeografi"
           ,"Edukate Qytetare","Edukate Muzikore","Edukate Figurative","TIK","Teknologji"
           ,"Edukate Fizike","Etike","Kimi"]

class_number = [7,8,9]
classesAverage = []
classes6789 = []

def classesGrades(cls): # cls for classes6 or classes789
    global class_sum
    global classes
    class_sum = 0 
    for classes in cls:
            while True:
                try:
                    class_subject = float(input(str(classes + " : ")))
                    class_sum += class_subject
                    break
                except ValueError:
                    print("Please use an integer or floating number!")       

def classf6():
    global class_average
    global classesAverage
    print("---Data for class 6!")
    classesGrades(classes6)
    print("Sum of the subjects grades: " + str(class_sum))
    print("Number of subjects : " + str(len(classes)))
    class_average = class_sum / 13
    classesAverage.append(class_average)
    print(str("C6 Average: " + str(class_average)))

def classf789():
    global classesAverage
    #for n in class_number:
    #Testing - print("C" + str(c))
    classesGrades(classes789)
    print("Sum of the subjects grades: " + str(class_sum))
    print("Number of subjects : " + str(len(classes)))
    class_average = class_sum / float(len(classes789))
    classesAverage.append(class_average)
    #testing
    print("class_average = " + str(class_average))
    print("class_sum = " + str(class_sum))
    print("len(classes789) = " + str(float(len(classes789))))
    ####
    print(str("C" + str(c) + " Average: " + str(class_average)))
    if len(classesAverage) == 4:
        classesAverage_sum = 0
        for i in classesAverage:   
            classesAverage_sum += i
            bonusPoints = ( classesAverage_sum / 4 ) * 5
        print("---You'll get " + str(bonusPoints) + " bonus points!")

classf6()
for c in class_number:
    print("---Data for class " + str(c) + "!")
    classf789()





    
