"""
Самописный калькулятор
"""

num1 = int(input())
num2 = int(input())
str_opr = input()

if num2 == 0 and str_opr == "/":
    print("На ноль делить нельзя!")
elif str_opr == "*":
    print(num1 * num2)
elif str_opr == "/":
    print(num1 / num2)
elif str_opr == "+":
    print(num1 + num2)
elif str_opr == "-":
    print(num1 - num2)
else:
    print("Неверная операция")