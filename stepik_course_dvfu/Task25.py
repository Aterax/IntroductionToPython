"""
Измерили дальности полета воды, выпущенной из шланга, под разными углами к горизонту.
По этим данным построить тренд (полином второй степени) зависимости дальности полета
от угла наклона шланга и найти дальность полета струи воды для произвольного угла.
"""

import numpy as np


# Функция расчета тренда (полином второй степени)
def get_trend_two(x, b):
    y = b[0] * x ** 2 + b[1] * x + b[2]
    return y


# Вводные данные
corner = np.array(input().split(), dtype=int)
list_distances = np.array(input().split(), dtype=float)
inclination = np.array(input().split(), dtype=float)
# Строим тренд (полином второй степени) зависимости дальности полета от угла наклона шланга
trend = np.polyfit(corner, list_distances, 2)
# находим дальность полета струи воды для произвольного угла.
distance = get_trend_two(inclination, trend)

print("Дальность: %6.2f м" % distance)