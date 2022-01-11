# Дан треугольник ABC на плоскости, заданный координатами своих вершин.
# Для этого треугольника вычислить:
# радиус вписанной в треугольник окружности;
# радиус описанной вокруг треугольника окружности;
# сумму длин трех медиан треугольника.


from math import pi, sqrt, pow

x_a = float(input())
y_a = float(input())
x_b = float(input())
y_b = float(input())
x_c = float(input())
y_c = float(input())

def compute_len(x_0, y_0, x_1, y_1):
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return len_line

a = compute_len(x_b, y_b, x_c, y_c)
b = compute_len(x_a, y_a, x_c, y_c)
c = compute_len(x_a, y_a, x_b, y_b)

if a + b <= c or b + c <= a or a + c <= b:
    print("error")
else:
    p = a + b + c
    s = sqrt(p / 2 * (p / 2 - a) * (p / 2 - b) * (p / 2 - c)) # Площадь треугольника
    r = round(sqrt(((p/2 - a) * (p/2 - b) * (p/2 - c)) / (p/2)), 4) # Радиус вписанной в треугольник окружности
    R = round((a * b * c) / (4*s), 4) # Радиус описанной вокруг треугольника окружности
    Ma = (1/2 * (sqrt(2 * (pow(c, 2) + pow(b, 2)) - pow(a, 2)))) # Длины меридиан
    Mb = (1/2 * (sqrt(2 * (pow(a, 2) + pow(c, 2)) - pow(b, 2))))
    Mc = (1/2 * (sqrt(2 * (pow(a, 2) + pow(b, 2)) - pow(c, 2))))
    print(r, R,round(Ma + Mb + Mc, 4))