month = int(input('Введите месяц в виде целого числа от 0 до 12: '))

month_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль',
              8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}

season_list = ['зима', 'весна', 'лето', 'осень']

if month in month_dict:
    print(f'{month}-й месяц года - {month_dict.get(month)}')

if 3 <= month and month <= 5:
    print(f'Этот месяц приходится на сезон {season_list[1]}')
elif 6 <= month and month <= 8:
    print(f'Этот месяц приходится на сезон {season_list[2]}')
elif 9 <= month and month <= 11:
    print(f'Этот месяц приходится на сезон {season_list[3]}')
else:
    print(f'Этот месяц приходится на сезон {season_list[0]}')
