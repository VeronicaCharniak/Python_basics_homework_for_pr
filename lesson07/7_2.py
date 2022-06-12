from abc import ABC, abstractmethod


class Сlothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Сlothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Сostume(Сlothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def consumption(self):
        return 2 * (self.height / 100) + 0.3


coat_1 = Coat(44)
print(f'Вам потребуется {coat_1.consumption:.2f} метров ткани на пальто {coat_1.size} размера ')
costume_1 = Сostume(168)
print(f'Вам потребуется {costume_1.consumption:.2f} метров ткани на костюм {costume_1.height} роста ')
print(f'Всего вам потребуется {coat_1 + costume_1:.2f} метров ткани')
