"""
Вы положили некоторую сумму x в банк на n месяцев под k% годовых с капитализацией процентов.
Посчитать прибыль от вложения (разницу между конечной и исходной суммой), результат округлить до целого.
"""

# deposit - сумма вклада, interest_rate -процентная ставка,
# amount_months - количество месяцев
def compute_income(deposit, interest_rate, amount_months):
    profit = deposit * pow((1 + interest_rate / (12 * 100)), amount_months)
    return profit - deposit

x = float(input())
k = float(input())
n = int(input())

# вычислить прибыль с помощью функции
S = compute_income(x, k, n)

#вывести результат
print("%4d" % round(S))