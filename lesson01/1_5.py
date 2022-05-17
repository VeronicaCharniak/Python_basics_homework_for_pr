earnings = int(input('Введите значение вашей прибыли: '))
costs = int(input('Введите значение ваших издержек: '))
if earnings > costs:
    print('Ваша прибыль составила', earnings - costs)
elif earnings < costs:
    print('Ваш убыток составил', costs - earnings)
elif earnings == costs:
    print('Вы отработали в ноль')
