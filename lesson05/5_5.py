from random import randint

with open('text_5.txt', 'w+', encoding='utf-8') as f:
    f.write(' '.join([str(randint(1, 100)) for i in range(100)]))
    f.seek(0)
    print(sum(map(int, f.readline().split())))
    