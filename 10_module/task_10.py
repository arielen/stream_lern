""" Задача 10. Яма
В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
Напишите программу, которая получает на вход число N и выводит на экран числа в виде «ямы» вот так:  """

N = int(input('Введите число: '))

for row in range(N):
    number = N
    number_right = -N
    for col in range(N * 2):
        if col <= row:
            print(number, end='')
        elif col / 2 - 1 == abs(number_right + row):
            print(abs(number_right), end='')
            number_right -= 1
            break
        else:
            print('.', end='')
        number -= 1

    print()
