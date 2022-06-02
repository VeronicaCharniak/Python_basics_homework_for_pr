with open('text_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line_of_numbers = ''.join((i if i in '1234567890' else ' ') for i in line)
        hours = [int(i) for i in line_of_numbers.split()]
        print(f'{line.split()[0]} {sum(hours)}')
