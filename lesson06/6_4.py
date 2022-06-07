from random import choice


class Car:
    direction = ['left', 'right', 'back']

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'The car name is {name}. It is {color}. Is it the police car? {is_police}.')

    def go(self):
        print(f'{self.name} is starting to drive.')

    def stop(self):
        print(f'{self.name} has just stopped.')

    def turn(self):
        print(f'{self.name} is turning {choice(self.direction)}.')

    def show_speed(self):
        print(f'The car {self.name} speed is {self.speed}.')


class TownCar(Car):

    def show_speed(self):
        return f'The {self.name} speed ({self.speed}) is too high!' if self.speed > 60 else super().show_speed()


class WorkCar(Car):

    def show_speed(self):
        return f'The {self.name} speed ({self.speed}) is too high!' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=True)


town_car = TownCar('Kia', 'black', 66)
work_car = WorkCar('Maz', 'yellow', 45)
sport_car = SportCar('Speedy', 'red', 120)
police_car = PoliceCar('Ford', 'blue', 55)

list = [town_car, work_car, sport_car, police_car]

for i in list:
    i.go()
    i.turn()
    i.stop()
    print(i.show_speed())
    print()
