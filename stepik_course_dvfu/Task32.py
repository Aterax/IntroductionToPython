"""
Пусть колесо обозрения имеет высоту H, совершает полный оборот за T минут.
Вычислить, на какой высоте будет находиться кабинка через t минут после посадки в нее людей.
В задаче реализовать проверку входных данных (время движения t ограничено T минутами),
при вводе неверного числа вывести "error".
"""

from numpy import sin, cos, array, dot, radians, around

height = int(input())
time_full = int(input())
time = float(input())

rot = radians((360 * time) / time_full)
rotation = array([[cos(rot), sin(rot)], [-sin(rot), cos(rot)]])

if 0 <= time <= time_full:
    end = dot([0, -height / 2], rotation)
    print("Высота = %6.2f м" % (end[1] + height / 2))
else:
    print("error")