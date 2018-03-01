"""

59) Nje teater ka 13 rreshta me ulese.
Rreshti i parre ka 32 ulese dhe secili rresht pasues ka nga
dy ulse me teper se rreshti para tij.
Sa ulese ka ne ate teater?

"""

ulese = 32
rreshta = 13
shtohen = 0
shtohen_gjithsej = 0
order = 0
shtohen_list = [32]

shtohen = 0
while order != 13:
    order = order + 1
    shtohen += 2
    ulese += shtohen
    ulese_all = shtohen_list[
    shtohen_list.insert(0,ulese)
    print(shtohen_list)

print(shtohen_gjithsej)

