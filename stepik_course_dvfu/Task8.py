"""
Дано значение времени в 12-ти часовом формате h:m:s.
 Определить угол в градусах между положением часовой стрелки в начале суток и
  ее положением в h часов,m минут и s секунд.
  """

hour = int(input())
minutes = int(input())
second = int(input())

if hour < 0 or hour > 11 or minutes < 0 or minutes > 59 or second < 0 or second > 59:
    print("error")
else:
    degree_hour = hour * (360 / 12)
    degree_minutes = minutes * (360 / 720)
    degree_second = second * (360 / 43200)
    print(round(degree_hour + degree_minutes + degree_second, 2))