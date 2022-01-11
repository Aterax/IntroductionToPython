# По номеру года найти число дней в этом году (вывести 365, если это не високосный год, или 366, если високосный).

year = int(input())

if year <= 1582:
    print("error")

elif year%100 == 0 and year%400 != 0:
    print(365)
elif year%4 == 0:
    print(366)
else:
    print(365)