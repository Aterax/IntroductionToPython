# Вычислить численность населения в заданные годы.

import math
# Исходные данные
C = 172
T1 = 2000
T = 45
# Функция расчета численность населения в заданные годы
def compute_population(t):
    t = (C / T) * (math.pi / 2 - math.atan((T1 - t) / T))
    return t
# вводим строку с числами
line = input()
# преобразуем строку в список, элементы которого - строки
years_str_list = line.split()
# Присваиваем переменной n количесво элементов в списке
n = len(years_str_list)
# создаем новый список на основе уже сформированного,
# переводя каждый элемент в целое число
years_list = [int(x) for x in years_str_list]
# формируем пустой список
population_list = []
# Цикл который по чередно присваивает значения переменой x из списка years_list и высчитывает численность населения,
# занося полученое значение в список population_list
for x in years_list:
    population = compute_population(x)
    population_list.append(population)
# В цикле для каждого года выводится численность населения
for i in range(n):
    print("%5d - %6.3f миллиард(ов)" % (years_list[i], population_list[i]))