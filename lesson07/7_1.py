class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join([f"{itm:03}" for itm in line]) for line in self.matrix)

    def __add__(self, other):
        try:
            m = [[int(self.matrix[line][itm]) + int(other.matrix[line][itm]) for itm in range(len(self.matrix[line]))]
                 for line in range(len(self.matrix))]
            return Matrix(m)
        except IndexError:
            return f'Ошибка размерностей матриц'


m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [[31, 22, 3], [37, 43, 5], [51, 86, 7]]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 + mtrx_2

print('First matrix:\n', mtrx_1, end='\n\n')
print('Second matrix:\n', mtrx_2, end='\n\n')
print('Summ of first and second matrix:\n', mtrx_1 + mtrx_2)
