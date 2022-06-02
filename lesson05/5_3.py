with open('text_3.txt', 'r', encoding='utf-8') as f:
    my_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    average_salary = round(sum(my_dict.values()) / len(my_dict), 2)
    print(f'Средний доход сотрудников составил {average_salary}')
    less_than_twenty = {e[0] for e in my_dict.items() if e[1] < 20000}
    print(f'Заработная плата ниже 20000 у следующих работников {less_than_twenty}')