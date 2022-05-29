from sys import argv


def salary():
    time, rate, bonus = map(float, argv[1:])
    employee_salary = (time * rate) + bonus
    print(f'Зарплата сотрудника составила {employee_salary} рублей')


try:
    salary()
except ValueError as err:
    print(err)
