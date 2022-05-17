number = int(input('Введите целое положительное число: '))
max_number = 0
while number > 0:
    last_number = number % 10
    if last_number > max_number:
        max_number = last_number
    number = number // 10
print('Самая большая цифра в числе: ', max_number)




