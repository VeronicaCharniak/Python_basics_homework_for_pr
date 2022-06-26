class Exception:
    my_class = []

    def add(self):
        n = input()
        try:
            my_class.append(n)
        except not n.isdigit():
            print("Вводите, пожалуйста, только числа")