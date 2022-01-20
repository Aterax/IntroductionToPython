# Звездный треугольник

n = int(input())

if n >= 2:
    for i in range(n, 0, -1):
        print("*" * i)
else:
    print("error")