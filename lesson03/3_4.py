def my_func(x, y):
    x = float(x)
    y = int(y)
    if x <= 0 or y >= 0:
        print('Введите корректные данные')
    else:
        result = round(x ** y, 5)
        return result


number_1 = input('Введите действительное положительное число: ')
number_2 = input('Введите целое отрицательное число: ')
print(my_func(number_1, number_2))
