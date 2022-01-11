"""
Даны точки на плоскости, координаты которых занесены в массивы x_array и y_array.
Постройте по этим точкам наиболее подходящий тренд: линейный (полином первой степени)  или квадратичный (полином второй степени).
Для этого для каждого типа тренда:
    найдите коэффициенты полинома;
    сформируйте массив значений, посчитанных по формуле тренда в точках  x_array;
    вычислите среднюю ошибку между известными значениями y_array и посчитанными с
    помощью формулы тренда (начала посчитать относительную погрешность между координатой  точки по оси ОУ и
     значением тренда в этой точке, потом найти среднее значение погрешности).

Далее необходимо сравнить среднюю погрешность двух трендов и вывести коэффициенты тренда  с наименьшей средней ошибкой. Если ошибки одинаковы, то выводить коэффициенты полинома второй степени.
"""

# Импорт библиотеки NumPy
import numpy as np


# Функция расчета тренда (полином первой степени)
def get_trend_one(x, a):
    y = a[0] * x + a[1]
    return y


# Функция расчета тренда (полином второй степени)
def get_trend_two(x, b):
    y = b[0] * x ** 2 + b[1] * x + b[2]
    return y


# Функция расчета относительной прогрешности
def rel_err(x_fact, x_real):
    p = abs((x_real - x_fact) / x_fact)
    return p


# Вводные данные, строки координат
mot_coord_ox = input()
mot_coord_oy = input()

# Преобразование строк координат через цикл for в массивы занчиний координат
x_array = np.array([float(x) for x in mot_coord_ox.split(" ")])
h_array = np.array([float(x) for x in mot_coord_oy.split(" ")])

# Вычисляем коофиценты для полинома первой\второй степени
a = np.polyfit(x_array, h_array, 1)
b = np.polyfit(x_array, h_array, 2)
# Формируем массивы значений тренда, посчитанных по формуле тренда в точках x_array.
pol_one = get_trend_one(x_array, a)
pol_two = get_trend_two(x_array, b)

# Высчитываем относительную погрешность между координатой  точки по оси ОУ и значением тренда в этой точке
rel_err_pol_one = rel_err(h_array, pol_one)
rel_err__pol_two = rel_err(h_array, pol_two)
# Высчитываем среднюю ошибку между известными значениями y_array и посчитанными с помощью формулы тренда
avg_err_pol_one = np.sum(rel_err_pol_one) / len(rel_err_pol_one)
avg_err_pol_two = np.sum(rel_err__pol_two) / len(rel_err__pol_two)

# Сравниваем среднюю погрешность двух трендов и выводим коэффициенты тренда  с наименьшей средней ошибкой
if avg_err_pol_one <= avg_err_pol_two:
    print(f"%5.3f %5.3f" % (a[0], a[1]))
else:
    print(f"%5.3f %5.3f %5.3f" % (b[0], b[1], b[2]))