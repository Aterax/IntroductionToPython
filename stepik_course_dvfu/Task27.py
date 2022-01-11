"""
Семья из трех человек планирует поехать отдыхать из города А в город B.
Можно полететь самолетом, а можно – на своей машине.
Сколько рублей придется заплатить за самую дешевую поездку на троих туда и обратно?
"""

ticket_price = float(input())
gasoline_price = float(input())
distance = float(input())

if ticket_price <= 0 or gasoline_price <= 0 or distance <= 0:
    print("error")
else:
    air_price = round(ticket_price * 3, 2)
    car_price = round((((12 / 100 * distance) * gasoline_price) * 2), 2)

    if air_price >= car_price:
        print(car_price)
    else:
        print(air_price)