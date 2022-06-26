class ZeroDivisionError:
    num_1 = 300

    def division(self, num_2):
        self.num_2 = int(input())
        try:
            return num_1 / num_2
        except ZeroDivisionError as err:
            print('Вы ввели ноль. На ноль делить нельзя. Попробуйте еще раз.')
