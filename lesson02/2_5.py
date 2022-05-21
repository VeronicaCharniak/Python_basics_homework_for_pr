rate = [9, 7, 5, 3]

while True:
    number = int(input('Введите новый элемент рейтинга >0: '))
    if number > 0:
        rate.append(number)
        rate.sort(reverse=True)
        print(rate)
    elif number == 0:
        break
print('Рейтинг составлен')
