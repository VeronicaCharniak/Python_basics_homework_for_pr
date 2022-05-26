def f_div(number_1, number_2):
    number_1 = int(number_1)
    number_2 = int(number_2)
    print(round(number_1 / number_2, 3))


try:
    f_div((input('Введите первое число: ')), (input('Введите второе число: ')))
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
