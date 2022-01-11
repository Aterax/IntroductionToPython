from math import sqrt, pow

try:
    a = int(input("Введите чило a: "))
    b = int(input("Введите чило b: "))
    if b != 0:
        print("**************************")
        print(f"Сумма чисел {a} и {b} = {a + b}")
        print(f"Разность чисел {a} и {b} = {a - b}")
        print(f"Произведение чисел {a} и {b} = {a * b}")
        print(f"Частное чисел {a} и {b} = {a / b}")
        print(f"Целая часть от деления числа {a} на {b} = {a // b}")
        print(f"Остаток от деления числа {a} и {b} = {a % b}")
        print(f"Квадратный корень из суммы 10-х степеней {a} и {b} = {sqrt(pow(a, 10) + pow(b, 10))}")
    else:
        print("Указаны не верные данные!")
except ArithmeticError:
    print("Указаны не верные данные!")
