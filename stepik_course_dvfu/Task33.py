"""
На основе данных о количестве  туристов в некоторой стране с 2005 по 2017 год
спрогнозировать количество туристов в 2018 году. Затем сравнить полученный результат
с известным значением этого показателя для страны, вычислить  относительную погрешность в процентах.
"""

from numpy import array, polyfit, polyval

country = input()
tur = array(input().split(), dtype='float')
years = [i for i in range(2005, 2018)]
deg = int(input())
kol = float(input())

a = polyfit(years, tur, deg)

trend = polyval(a, 2018)
pogr = abs((trend - kol) / kol * 100)

print("Страна:%6s, прогноз:%6.3fмлн чел, относительная погрешность:%4.2fпроц." % (country, trend, pogr))