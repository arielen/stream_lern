print('Задача 8. НОД')


# Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def AverageDiv(first, second):
    # находим минимальное значения для ориентации по нему
    if first < second:
        minimma = first
    else:
        minimma = second
    # цикл для нахождения общего делителя
    for div in range(1, minimma):
        if first % div == 0 and second % div == 0:
            max_div = div
    print(f'Наибольший общий делитель: {max_div}')


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

AverageDiv(first_number, second_number)
