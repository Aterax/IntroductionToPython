"""
Автомобиль из пункта А в пункт В проезжает по нескольким участкам дорог определенной длины.
Для каждого участка известно среднее количество машин, находящихся на нем, в момент времени,
когда там проезжает автомобиль. Плата за проезд по любому участку вычисляется в зависимости
от количества автомобилей на 1 км дороги
"""

import numpy as np

distance_list = np.array(input().split(), dtype=int)
avg_cars = np.array(input().split(), dtype=int)

cars = np.around(avg_cars / distance_list)

price = 0
for x in cars:
    if x <= 30:
        price += 1
    elif 31 <= x <= 60:
        price += 1.5
    elif 6 <= x <= 120:
        price += 3
    else:
        price += 4.5

print("Длина пути: %3d км, оплата: %5.2f S$" % (sum(distance_list), price))