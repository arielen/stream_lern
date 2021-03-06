""" Задача 1. Среднее арифметическое
Программа получает от пользователя два числа — a и b.
Реализуйте функцию, которая принимает на вход числа a и b,
считает и выводит в консоль среднее арифметическое всех чисел из отрезка [a; b].
Обеспечьте контроль ввода: не забывайте, что а всегда должно быть меньше, чем b.

Пример:
Введите левую границу: 3
Введите правую границу: 8
Среднее: 5.5

Усложнение: сделайте это без использования циклов. """
import math as m


def average(a, b):
    count = 0
    sum = 0
    for number in range(a, b + 1):
        count += 1
        sum += number
    average = sum / count
    print(f'Среднее арифмитическое: {average}')


while True:
    left = int(input('Введите левую границу: '))
    right = int(input('Введите правую границу: '))
    if left < right:
        average(left, right)
        break
    else:
        print('Левое число должно быть меньше правого!')

""" Задача 2. Почта 2
На почте немного поменялись правила: теперь в почтовом извещении нужно указывать: 
фамилию, имя, страну проживания, город, улицу, номер дома и номер квартиры.

Реализуйте функцию, которая получает все эти данные и выводит на экран. 
В программе вызовите функцию три раза с разными значениями аргументов.

Подсказка: семь аргументов. """


def adress(family, name, country, city, street, number_home, number_room):
    print(f'Фамилия: {family}')
    print(f'Имя: {name}')
    print(f'Страна: {country}')
    print(f'Город: {city}')
    print(f'Улица: {street}')
    print(f'Дом: {number_home}')
    print(f'Квартира: {number_room}')


adress('Петров', 'Василий', 'Россия', 'Москва', 'Ленина', '35', '89')

""" Задача 3. GPS-навигатор 2.0
Нам поручили усовершенствовать GPS-навигатор, добавив в него новую фишку. 
Теперь пользователь может не только смотреть расстояние от себя до объекта, 
но и задавать в навигаторе две произвольные точки, после чего на экран ему выводится расстояние между ними. 
Для этого пользователь вводит четыре действительных числа x1, y1, x2, y2 — это как раз координаты этих двух точек.

Напишите программу, где у пользователя спрашивается, чего он хочет — 
найти расстояние от себя до точки или найти расстояние между двумя произвольными точками, 
после чего запрашиваются необходимые координаты точек и выводится ответ на экран. """


def myDistance(x, y):
    distance = m.sqrt(x ** 2 + y ** 2)
    print(f'Расстояние: {distance}')


def betweenDistance(x_1, y_1, x_2, y_2):
    distance = m.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    print(f'Расстояние: {distance}')


choice = int(input('1- расстояние до точки; 2- расстояние от точки до точки:  '))

if choice == 1:
    x = float(input('Введите координату X: '))
    y = float(input('Введите координату Y: '))
    myDistance(x, y)
elif choice == 2:
    x_1 = float(input('Введите координату X первой точки: '))
    y_1 = float(input('Введите координату Y первой точки: '))
    x_2 = float(input('Введите координату X второй точки: '))
    y_2 = float(input('Введите координату Y второй точки: '))
    betweenDistance(x_1, y_1, x_2, y_2)
else:
    print('Введите корректные данные!')