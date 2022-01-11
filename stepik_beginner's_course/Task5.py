"""
Напишите программу для нахождения цифр четырёхзначного числа.
"""

class_num = ["тысяч", "сотен", "десятков", "единиц"]


def digits_iterative(nonneg):
    digits = []
    while nonneg:
        digits += [nonneg % 10]
        nonneg //= 10
    return digits[::-1] or [0]


num = int(input())
num_list = digits_iterative(num)

for x in range(4):
    print(f"Цифра в позиции {class_num[x]} равна {num_list[x]}")