f = open('my_file.txt', 'r', encoding='utf-8')
content = f.readlines()
for index, value in enumerate(content, 1):
    number_of_words = len(value.split())
    print(f'Строка номер {index} содержит {number_of_words} слов')
f.close()
