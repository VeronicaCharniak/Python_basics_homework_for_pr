import json

with open('text_7.json', 'w', encoding='utf-8') as f:
    with open('text_7.txt', 'r', encoding='utf-8') as f_1:
        dif = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_1}
        profit = [i for i in dif.values() if i > 0]
        my_py_list = [dif, {'average_profit': round(sum(profit) / len(profit))}]

        json.dump(my_py_list, f, ensure_ascii=False)
