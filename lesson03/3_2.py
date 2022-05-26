def options(**kwargs):
    return ' '.join(kwargs.values())


print(options(name=input('Введите ваше имя: '), surname=input('Введите вашу фамилию: '),
              age_of_birth=input('Год вашего рождения: '), city=input('Город проживания: '),
              email=input('Введите ваш email: '), phone_number=input('Номер телефона: ')))
