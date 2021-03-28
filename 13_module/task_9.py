print('Задача 9. Сумма ряда')


# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

def factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


def exponent(num, degree):
    exponent = num
    for n in range(degree - 1):
        exponent *= num
    return exponent


def finder(x, precesion):
    member = 1
    summ = 1
    degree = 1
    while abs(member) > precesion:
        member = exponent(-1, degree) * (exponent(x, 2 * degree) / factorial(2 * degree))
        summ += member
        degree += 1
    return summ


precision = float(input('Введите точность: '))
x = int(input('Введите X: '))

print(f'Сумма ряда = {finder(x, precision)}')
