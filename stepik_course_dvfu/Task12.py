"""
Сравнить значения реальной численности населения в определенные годы со значениями,
вычисленными по формуле в те же годы
"""

from math import pi, atan


# Функция расчета численность населения в заданные годы
def compute_population(t):
    t = (172 / 45) * (pi / 2 - atan((2000 - t) / 45))
    return t


years = [1000, 1750, 1800, 1850, 1900, 1950, 1955, 1960,
         1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000,
         2005, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
         2017, 2018, 2019]
#  реальной численности населения в определенные годы(порядок списка years)
populalion = [0.400, 0.791, 1.000, 1.262, 1.650, 2.519,
              2.756, 3.021, 3.335, 3.692, 4.068, 4.435,
              4.831, 5.264, 5.674, 6.071, 6.344, 6.933,
              7.015, 7.100, 7.162, 7.271, 7.358, 7.444,
              7.530, 7.669, 7.763]

# Cписок со значениями числености, посчитанными с помощью функции compute_population(t) для годов из списка years
calculated_value = [compute_population(t) for t in years]
# Входные данные
index_start = int(input())
index_stop = int(input())
# Срезы списков
years = years[index_start:index_stop+1]
populalion = populalion[index_start:index_stop+1]
calculated_value = calculated_value[index_start:index_stop+1]
# Вычисление относительной погрешности и занесение значений в список error_list
# Переменной i присваивается длина списка years
error_list = [abs((populalion[i] - calculated_value[i]) / populalion[i])
              for i in range(len(years))]
# Максимальная погрешность и её индекс
max_error = max(error_list)
index_max_error = error_list.index(max_error)
# Минимальная погрешность и её индекс
min_error = min(error_list)
index_min_error = error_list.index(min_error)
# Средняя погрешность
avg_error = sum(error_list) / len(populalion) * 100
# Строка форматного вывода
print("Погрешность - минимальная, год: %4d, максимальная, год: %4d, средняя, процент: %6.3f" % (years[index_min_error], years[index_max_error], avg_error))