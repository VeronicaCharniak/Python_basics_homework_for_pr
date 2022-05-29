from itertools import count
from math import factorial


def fact_gen():
    for number in count(1):
        yield factorial(number)


a = 0
for i in fact_gen():
    if a == 10:
        break
    else:
        a += 1
        print(f'Факториал {a} = {i}')