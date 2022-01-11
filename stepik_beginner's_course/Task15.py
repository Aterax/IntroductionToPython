"""
Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.
"""

a, b, c = int(input()), int(input()), int(input())

if a > b > c or a > b < c or a < b < c:
    print(b)
elif (a < b > c) and a < c:
    print(c)
else:
    print(a)