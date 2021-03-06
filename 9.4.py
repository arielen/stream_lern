""" Задача 1. Доска
Используя новые знания с циклами и оператором end, выведете на экран “доску”, которую вы делали в первом модуле """

print('-' * 10)
for doska in range(4):
    print('|' + '0' * 8 + '|')
print('-' * 10)

""" Задача 2. Локальная сеть
У Никиты дома есть много компьютеров, которые он хочет подключить к одной локальной сети. 
Для этого ему нужно сгенерировать айпи адрес для каждого компьютера. 
Айпи адрес записывается как 4 числа, которые отделяются точкой. 
Не долго думая, для генерации Никита решил использовать арифметическую прогрессию, 
причём первые 3 числа в адресе - это члены прогрессии, а последнее число - это её сумма.

Напишите программу, где пользователь вводит первый член прогрессии и разность и в результате получает айпи-адрес. """

number = int(input('Введите число:  '))
step = int(input('Введиите шаг:  '))
last_symbol = 0

print('IP-адресс: ', end='')
for ip in range(3):
    print(number, end='.')
    last_symbol += number
    number += step
print(last_symbol)

""" Задача 3. Табло
Петя пишет компьютерную спортивную игру, где каждый “гол” это десять очков. 
Он хочет сделать красивое табло с градацией этих очков.
Пользователь вводит число N (N >= 0). 
Реализуйте программу, которая выводит в одну строчку каждое десятое число, разделяя их символами “-=-”. 
Эти же символы стоят перед первым числом и после последнего.

Пример:
Введите число: 50
-=- 0 -=- 10 -=- 20 -=- 30 -=- 40 -=- 50 -=-
 """

number = int(input('Введите число: '))

print(' -=- ', end='')
for num in range(0, number+1, 10):
    print(num, end=' -=- ')