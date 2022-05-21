phrase = input('Введите несколько слов, разделенных пробелами: ')
phrase = phrase.split()

for i, word in enumerate(phrase, 1):
    print(f'{i}) - {word:.10}')
   