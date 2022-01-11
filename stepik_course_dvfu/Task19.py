"""
Дорога из пункта А в пункт В состоит из нескольких участков, известны их длины.
Для автомобиля известна средняя скорость его движения на каждом участке.
Автомобиль въехал на дорогу в начале участка k и выехал с нее после проезда по участку p.
Найти сколько километров проехал автомобиль по дороге, время движения и среднюю скорость.
"""

# Подклчение библиотеки NymPy
import numpy as np
# Входные переменные
distance = np.array(input().split(), dtype=int)
speed = np.array(input().split(), dtype=int)
lot_number_in = int(input())
lot_number_out = int(input())
# Длина пути, время в пути, средняя скорость
sum_distance = sum(distance[lot_number_in:lot_number_out + 1])
time = sum(distance[lot_number_in:lot_number_out + 1] / speed[lot_number_in:lot_number_out + 1])
avg_speed = sum_distance / time
# Строка форматного вывода
print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (sum_distance, time, avg_speed))