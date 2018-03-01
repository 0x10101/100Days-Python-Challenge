"""

Developer : Gjergj Kadriu
Version : 1.0
Last Update : 26.02.2018

"""


classes6 = ["Gjuhe Shqipe","Gjuhe Angleze","Matematike","Biologji","Fizike","Histori","Gjeografi"
           ,"Edukate Qytetare","Edukate Muzikore","Edukate Figurative","Teknologji/TIK"
           ,"Edukate Fizike","Etike"]


classes789 = ["Gjuhe Shqipe","Gjuhe Angleze","Matematike","Biologji","Fizike","Histori","Gjeografi"
           ,"Edukate Qytetare","Edukate Muzikore","Edukate Figurative","TIK","Teknologji"
           ,"Edukate Fizike","Etike","Kimi"]

class_number = [7,8,9]

class6_average = 0
class7_average = 0
class8_average = 0
class9_average = 0

classes6789 = []

def classf6():
    class6_sum = 0 
    for item in classes6:
        while True:
            try:
                class6_subject = float(input(str(item + " : ")))
                class6_sum += class6_subject
                break
            except ValueError:
                print("Please use an integer or floating number!")   
    print("Sum of the subjects grades: " + str(class6_sum))
    print("Number of subjects : " + str(len(classes6)))
    class6_average = class6_sum / float(len(classes6))
    print(str("C6 Average: " + str(class6_average)))
       
    
classf6()
            
    
