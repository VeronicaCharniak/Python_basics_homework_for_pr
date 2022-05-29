from itertools import count, cycle

try:
    my_count = count(int(input('Введите число, с которого начнется цикл: ')))
    my_cycle = cycle(input('Введите список, разделяя элементы пробелом: ').split())
    for n in range(int(input('Введите количество повторений программы: '))):
        print(f'(my_count, my_cycle) = {next(my_count)},{next(my_cycle)}')
except ValueError as err:
    print(err)


