""" Задача 5. Простые числа
Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран. """

N = int(input('Введите кол-во чисел: '))
numberCount = 0
flag = 0

for number in range(N):
    num = int(input('Введите число: '))
    for n in range(num - 1, 1, -1):
        if num % n == 0:
            flag = 1
    if flag == 0:
        numberCount += 1
    flag = 0

print(f'Кол-во простых чисел в последовательности = {numberCount}')
