"""
Решить задачу о попадании снаряда в мишень (напомним, что радиус мишени составляет 50 сантиметров или 0.5 метра)
в общем виде, то есть чтобы пользователь вводил координаты движения снаряда в виде списков, а также координаты положения мишени.
"""

import numpy as np

mot_coord_ox = input()
mot_coord_oy = input()
target_coord_ox = float(input())
target_coord_oy = float(input())

x_array = np.array([float(x) for x in mot_coord_ox.split(" ")])
h_array = np.array([float(x) for x in mot_coord_oy.split(" ")])

a = np.polyfit(x_array, h_array, 2)


def get_trend(x, a):
    y = a[0] * x ** 2 + a[1] * x + a[2]
    return y


h_zero = get_trend(0, a)
h_target = get_trend(target_coord_ox, a)
delta_h = abs(target_coord_oy - h_target)

if delta_h <= 0.5:
    print("h0 = %6.2f, %2s" % (h_zero, "yes"))
else:
    print("h0 = %6.2f, %2s" % (h_zero, "no"))