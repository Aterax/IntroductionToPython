"""
Даны две различные клетки шахматной доски.
Напишите программу, которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом.
"""

col_num1 = int(input())
line_num1 = int(input())
col_num2 = int(input())
line_num2 = int(input())

if 1 <= (col_num1 and line_num1 and col_num2 and line_num2 <= 8) and col_num1 == col_num2 or line_num1 == line_num2:
    print('YES')
else:
    print('NO')