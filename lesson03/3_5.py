def sum_fun():
    result = 0
    stop = False
    while not stop:
        print(f'Сумма ваших чисел - {result}')
        numbers = input('Введите строку чисел, разделенных пробелом: \n чтобы выйти - нажмите "q"\n').split()
        for el in numbers:
            if el.lower() == 'q':
                print(f'Подсчет завершен. Итоговая сумма ваших чисел - {result}')
                stop = True
            else:
                try:
                    result += int(el)
                except ValueError as err:
                    print(err)


sum_fun()
