"""
Дан порядковый номер месяца.
Напишите программу, которая выводит на экран количество дней в этом месяце.
"""


i = int(input())
x = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
print(x[i - 1])

