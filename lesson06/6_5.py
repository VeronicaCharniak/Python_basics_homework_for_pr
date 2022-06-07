class Stationery:

    def __init__(self, title='random'):
        self.title = title

    def draw(self):
        print(f'You are drawing with the {self.title} stationery.')


class Pen(Stationery):

    def draw(self):
        print(f'You are drawing with the {self.title} pen.')


class Pencil(Stationery):

    def draw(self):
        print(f'You are drawing with the {self.title} pencil.')


class Handle(Stationery):

    def draw(self):
        print(f'You are drawing with the {self.title} handle.')


stationery = Stationery()
pen = Pen("ink")
pencil = Pencil("lead")
handle = Handle("permanent")

list = [stationery, pen, pencil, handle]

for i in list:
    i.draw()
