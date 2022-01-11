weight = float(input())
height = float(input())

if 0.5 <= height > 3 or 1 <= weight > 500:
    print("Ошибочные входные данные")
else:
    bmi = weight / height ** 2
    bmi = round(bmi, 2)

    if bmi < 18.5:
        print("Недостаточная масса")
    elif bmi <= 25:
        print("Оптимальная масса")
    elif bmi > 25:
        print("Избыточная масса")
