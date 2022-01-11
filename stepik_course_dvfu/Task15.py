"""
Известны величины потребленной электроэнергии в некотором помещении  за каждый месяц года.
Месячная норма потребления электроэнергии n кВт·ч , стоимость 1 кВт·ч в пределах нормы  a руб,
и стоимость за каждый 1 кВт·ч потребления электроэнергии сверх нормы  b руб.
Вычислите суммарное потребление и стоимость электроэнергии за год.
"""

energy_consumed_month = [int(n) for n in input("").split(" ")]
monthly_norm = int(input())
price_norm = float(input())
price_over_norm = float(input())
sum_energy_consumed_month = sum(energy_consumed_month)

price = 0
for n in energy_consumed_month:
    if n > monthly_norm:
        over = round((monthly_norm * price_norm) + ((n - monthly_norm) * price_over_norm), 2)
        price = price + over
    else:
        norm = n * price_norm
        price = price + norm

print("Сумма: %6d кВт ч, стоимость %7.2f руб" % (sum_energy_consumed_month, price))