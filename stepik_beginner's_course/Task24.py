# Средние значения

from math import sqrt

a, b = float(input()), float(input())
avr_arith = (a + b) / 2
avr_geo = sqrt(a * b)
avr_harm = (2 * a * b) / (a + b)
avr_quad = sqrt((pow(a, 2) + pow(b, 2)) / 2)

print(avr_arith, avr_geo, avr_harm, avr_quad, sep="\n", end=" ")