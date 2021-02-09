""" Задача 5. Простые числа
Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран. """

N = int(input('Введите число: '))
numberCount = 0

print('Простые числа: ', end='')
for number in range(2, N + 1):
    if (number % 2 != 0 or number == 2) \
            and (number % 3 != 0 or number == 3) \
            and (number % 5 != 0 or number == 5) \
            and (number % 7 != 0 or number == 7) \
            and (number % 11 != 0 or number == 11) \
            and (number % 13 != 0 or number == 13):
        print(number, end=' ')
        numberCount += 1

print(f'\nКоличество простых чисел в последовательности {numberCount}')

# смотрел алгоритм решета эрастофена, можно в принципе сделать через список.
# не самое лучшее решение показал
