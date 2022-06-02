russian_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
f = open('text_4.txt', 'r', encoding='utf-8')
f_1 = open('text_4_1.txt', 'w', encoding='utf-8')
f_1.writelines([line.replace(line.split()[0], russian_dict.get(line.split()[0])) for line in f])
f.close()
f_1.close()
