"""

Version : 1.1

Changes:
    -Switched from simple strings concatenation to formatting

"""

nounPlural = input("Noun (plural): ")
place = input("Place: ")
noun = input("Noun:")
nounPlural2 = input("Noun (plural): ")
noun2 = input("Noun: ")
adjective = input("Adjective: ")
verb = input("Verb: ")
number = input("Number: ")
adjective2 = input("Adjective: ")
bodyPart = input("Body Part: ")
verb2 = input("Verb: ")

print("""
    Two  {} both alike in dignity,
    In fair place where we lay our scene,
    From ancient {} break to new mutiny,
    Where civil blood makes civil hands unclean.
    From forth the fatal loins of these two foes
    A pair of star-cross`d {} take their life;
    Whole misadventured piteous overthrows
    Do with their {} bury their parents` strife.
    The fearful passage of their {} love,
    And the continuance of their parents` rage,
    Which, but their children`s end, nought could {},
    Is now the {} hours` traffic of our stage;
    The which if you with {} attend,
    What here shall {}, our toil shall strive to mend.")
""".format(nounPlural,place,noun,nounPlural2,noun2,adjective,verb,
           number,adjective2,bodyPart,verb2))



