"""
Цвета колеса рулетки
"""

pocket = int(input())

if -1 < pocket <= 36:
    if pocket == 0:
        print("зеленый")
    elif 0 < pocket <= 10:
        if pocket % 2 == 0:
            print("черный")
        else:
            print("красный")
    elif 11 <= pocket <= 18:
        if pocket % 2 == 0:
            print("красный")
        else:
            print("черный")
    elif 19 <= pocket <= 28:
        if pocket % 2 == 0:
            print("черный")
        else:
            print("красный")
    elif 29 <= pocket <= 36:
        if pocket % 2 == 0:
            print("красный")
        else:
            print("черный")
else:
    print("ошибка ввода")