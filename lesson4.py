from math import sqrt

begin = float(input('Введите начало: '))
ender = float(input('Введите конец: '))
step = float(input('Введите шаг: '))
x = begin

while x <= ender:
    if x <= 0.5:
        y = x ** 3 * sqrt(x)
    else:
        y = x ** 3
    print(f'y = {y}', x, sep='\n')
    x += step
