class Cell:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        return f"{self.numbers}"

    def __add__(self, other):
        print("Число ячеек в общей клетке:")
        return Cell(self.numbers + other.numbers)

    def __sub__(self, other):
        print("Разность количества ячеек в двух клетках:")
        return Cell(self.numbers - other.numbers) if self.numbers - other.numbers > 0 \
            else "Ячеек в первой клетке меньше второй, вычитание невозможно!"

    def __mul__(self, other):
        print("Перемножение ячеек двух клеток:")
        return Cell(self.numbers * other.numbers)

    def __floordiv__(self, other):
        print("Целочисленное деление ячеек клеток:")
        return Cell(self.numbers // other.numbers)

    def make_order(self, rows):
        return '\n'.join(['🦖' * rows for _ in range(self.numbers // rows)]) + '\n' + '🐙' * (self.numbers % rows)


cell_1 = Cell(30)
cell_2 = Cell(15)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(7))
print(cell_2.make_order(6))