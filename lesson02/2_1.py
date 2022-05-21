my_list = [
    18, 3.4, 7 + 8j, 'строка', True, None, [1, 2, 3], (4, 5, 6), {7, 8, 9}, {'key_1': 1, 'key_2': 2},
    b'thirteen', bytearray(b'fourteen'), frozenset('cat')
]
for i, el in enumerate (my_list):
    print(f'{i+1}) {el} - {type(el)}')

