earnings = int(input('Введите значение вашей прибыли: '))
costs = int(input('Введите значение ваших издержек: '))
profit = earnings - costs
profitability = (profit / earnings) * 100
if earnings > costs:
    print('Ваша прибыль составила', earnings - costs)
    print('Рентабельность выручки составила', f"{profitability:.2f}", 'процентов')
    number = int(input('Введите число сотрудников фирмы: '))
    net_profit = profit / number
    print('Прибыль фирмы в расчете на 1 сотрудника составила', f"{net_profit:.2f}")
elif earnings < costs:
    print('Ваш убыток составил', costs - earnings)
elif earnings == costs:
    print('Вы отработали в ноль')
