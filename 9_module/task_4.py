""" Задача 4. Театр
Планируется построить театр под открытым небом, но для начала нужно хотя бы примерно понять
сколько должно быть рядов, сидений в них и какое лучше сделать расстояние между рядами.

Напишите программу, которая получает на вход кол-во рядов, сидений и свободных метров между рядами,
а затем выводит примерный макет театра на экран. """

row = int(input('Введите кол-во рядов:  '))
seats = int(input('Введите кол-во сидений:  '))
meters = int(input('Введите кол-во сободных метров:  '))

print('Сцена')
for theatr in range(0, row):
    print('=' * seats, end='*' * meters)
    print('=' * seats)