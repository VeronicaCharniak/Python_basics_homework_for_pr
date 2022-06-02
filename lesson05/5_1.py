f = open('my_file.txt', 'w', encoding='utf-8')

while True:
    line = input('Введите, пожалуйста, строку текста (для выхода из программы надмите Enter): ')
    if not line:
        break
    f.write(f'{line}\n')

f.close()
