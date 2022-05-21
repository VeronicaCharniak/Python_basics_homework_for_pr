your_list = input('Введите целые числа через пробел')
your_list = your_list.split()

for i in range(1, len(your_list), 2):
    your_list[i - 1], your_list[i] = your_list[i], your_list[i - 1]

print(your_list)
