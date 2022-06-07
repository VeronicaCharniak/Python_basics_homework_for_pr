class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def formula(self, weight=25, thickness=5):
        print(f'Масса асфальта = {self._length * self._width * weight * thickness / 1000} тонн')


while True:
    try:
        road_1 = Road(int(input('Enter the length, please: ')), int(input('Enter the width, please: ')))
        road_1.formula()
        break
    except ValueError as err:
        print(err)
