"""
Даны длины стороны основания и высоты нескольких пирамид.
Вывести номера пирамид, имеющих максимальный объем, и номера пирамид,
имеющих минимальную площадь боковой поверхности.
"""

from numpy import array, sqrt

base_lengths = array(input().split(), dtype=float)
pyramid_heights = array(input().split(), dtype=float)


v, s = [], []
for i in range(len(base_lengths)):
    v.append(round(1 / 3 * pow(base_lengths[i], 2) * pyramid_heights[i], 2))
    s.append(round(base_lengths[i] * sqrt(4 * pow(pyramid_heights[i], 2) + pow(base_lengths[i], 2)), 2))

V = max(v)
S = min(s)
iV = v.index(V)
iS = s.index(S)
print("Vmax: %2d, %8.2f, Smin: %2d, %8.2f" % (iV, V, iS, S))