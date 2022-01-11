"""
Дан многоугольник на плоскости, заданный  координатами своих вершин.
Найти координаты вершин многоугольника, полученные поворотом каждой точки  на заданный угол вокруг начала координат.
Вычислить средние значения координат по оси ОХ и ОУ повернутого многоугольника.
"""

# Подключение библиотек
import math as mt

import numpy as np

# Ввод количесво вершинм
num_vert = int(input())
# Создаем двухмерный массив с помощью цикла
list_vert = []
for i in range(num_vert):
    list_vert.append([int(j) for j in input().split()])
vert = np.array(list_vert, dtype=int)
# Угол поворота в градусах
rot_degr = mt.radians(int(input()))
# Составление матрицы пороворота
rotation = np.array([[mt.cos(rot_degr), mt.sin(rot_degr)],
                     [-mt.sin(rot_degr), mt.cos(rot_degr)]])
#  Вычисляем матрицу после поворота
coord = np.dot(vert, rotation)
# Вычислем средние значение по осям OX,OY
avg = np.mean(coord, 0)
# Форматный вывод среднего значения с огрубление до двух знаков
print("avg_x = %6.2f, avg_y = %6.2f" % (np.round(avg[0], 2), np.round(avg[1], 2)))