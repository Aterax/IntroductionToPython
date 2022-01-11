"""
Даны n населенных пунктов, каждый из которых в некоторой относительной системе координат имеет две координаты x и y.
В пункте с номером (индексом) k установлена радиостанция с радиусом действия  r км. Определить, сколько населенных
пунктов попадает в радиус ее действия  (включая населенный пункт k).
"""

from math import sqrt

OX = [int(x) for x in input("").split(" ")]
OY = [int(y) for y in input("").split(" ")]
number_locality = int(input(""))
if number_locality < 0 or number_locality > len(OX) - 1 or len(OX) != len(OY):
    print("error")
    exit(0)
radio_zone = int(input(""))

distances = []
for x in range(len(OX)):
    distance = sqrt(pow(OX[number_locality] - OX[x], 2) + pow(OY[number_locality] - OY[x], 2))
    distances.append(distance)

count = 0
for d in distances:
    if d <= radio_zone:
        count = count + 1

print(count)