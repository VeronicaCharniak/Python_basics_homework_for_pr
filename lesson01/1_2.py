number = int(input('Введите число в секундах (число должно быть менее 86400):'))
hours = number // 3600
seconds_left = number % 3600
minutes = seconds_left // 60
seconds = seconds_left % minutes
hhmmss = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
print(hhmmss)
