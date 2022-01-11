# Цветовой микшер

red = "красный"
blue = "синий"
yellow = "желтый"

col_a = input()
col_b = input()

if col_a not in (red, blue, yellow) or col_b not in (red, blue, yellow):
    print("ошибка цвета")
elif col_a == red and col_b == blue or col_a == blue and col_b == red:
    print("фиолетовый")
elif col_a == red and col_b == yellow or col_a == yellow and col_b == red:
    print("оранжевый")
elif col_a == blue and col_b == yellow or col_a == yellow and col_b == blue:
    print("зеленый")
elif col_a == col_b:
    print(col_a)