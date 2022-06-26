class Data:
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

    @classmethod
    def number(self):
        return int(self.date), int(self.month), int(self.year)

    @staticmethod
    def validation(self):
        pass

date_1 = Data(13, 12, 1990)
print(date_1.number())