""" Задача 15. (*необязательная)
Для настольной игры используются карточки с номерами от 1 до N.
Одна карточка потерялась.
Найдите ее, зная номера оставшихся карточек.

Вводится число N, далее еще N − 1 чисел: номера оставшихся карточек (различные числа от 1 до N).
Программа должна вывести номер потерянной карточки. """

# TODO - тут неправильно, следует в условии изменить переменные
cards = int(input('Введите сколько карт в колоде: '))
number = 1
center = (cards + number) // 2
while True:
    print(f'Ваша карта, больше или меньше: {center}')
    answer = int(input('1 - равно, 2 - больше, 3 - меньше: '))
    center = (cards + number) // 2
    if answer == 1:
        print('Я угадал!')
        break
    elif answer == 2:
        number = int(center)
        center *= 2
    else:
        number = int(center)
        center /= 2