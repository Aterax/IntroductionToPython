"""
В течение некоторого периода ежедневно измерялись температуры в 0 и 12 часов в одном и том же месте.
Также известна средняя статистическая суточная температура за аналогичный период,
полученная в результате наблюдений за погодой за длительный период времени в рассматриваемой местности.
Необходимо вывести номера дней, в которые средняя температура за сутки (вычисляется как среднее значение температуры в 0 и 12 часов)
была выше средней статистической.
"""

temp_zero_hours = input()
temp_twelve_hours = input()
avg_temp = float(input())
list_zero_hours = [float(t) for t in temp_zero_hours.split(' ')]
list_twelve_hours = [float(t) for t in temp_twelve_hours.split(' ')]

for i in range(len(list_zero_hours)):
    avg_temp_day = (list_zero_hours[i] + list_twelve_hours[i]) / 2
    if avg_temp_day > avg_temp:
        print(i)