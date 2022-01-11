"""
Рассчитать ежемесячную сумму платежа по кредиту при использовании дифференцированных выплат
(в этом случае ежемесячный платеж по погашению кредита постепенно уменьшается к концу периода кредитования).
Сумма кредита составляет s рублей, срок кредита n месяцев, процент - k%.
"""


def compute_payment(t, s, n, k):
    p = s / n + (s - (t - 1) * s / n) * k / 1200
    return p


credit_amount = int(input())
credit_term = int(input())
rate = int(input())


li = []
income = 0
for t in range(1, credit_term + 1):
    p = compute_payment(t, credit_amount, credit_term, rate)
    print("%2d месяц - %8.2f руб" % (t, p))
    li.append(p)
    income = sum(li) - credit_amount

print("Доход банка - %6.2f руб" % income)