# Даны n точек на плоскости найти центр и минимальный радиус круга, куда попадут все эти точки.

# Подключаем библиотеки
from math import sqrt

import numpy as np

# Вводим количесво точек
num_points = int(input())
points_list = []
# Вводи координаты точе, создавая двухмерный массив
for x in range(num_points):
    points_list.append([float(j) for j in input().split()])
points = np.array(points_list, dtype=float)
# Вычисляем значение средней точки огругляя результат до 3-х знаков
x_y_avg = np.mean(points, 0)
x_avg = round(x_y_avg[0], 3)
y_avg = round(x_y_avg[1], 3)
# Вычисляем и формируем массив растояний от средней точки до каждой точки массива points
distances_list = []
for i in range(num_points):
    distances_list.append(sqrt(pow(points[i][0] - x_y_avg[0], 2) + pow(points[i][1] - x_y_avg[1], 2)))
distances = np.array(distances_list, dtype=float)
# Находим максимальное расттояние равное радиусу круга
radius = round(np.max(distances), 3)
# Форматный вывод
print("центр в точке (%6.3f, %6.3f), r = %6.3f" % (x_avg, y_avg, radius))