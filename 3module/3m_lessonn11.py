""" Задача 11. Режем число на части

Реализуйте программу, которая получает на вход четырёхзначное число и выводит на экран каждую его цифру отдельно
(в одну строчку либо каждая цифра в новой строчке).
Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
Однако можно использовать сколько угодно переменных. """

number = int(input('Введите ваше число: '))
thousend = number // 1000
hundert = number % 1000 // 100
ten = number % 100 // 10
unit = number % 10

print(thousend, hundert, ten, unit, sep='\n')
