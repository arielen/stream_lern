""" Задача 14. Кинотеатр (необязательно)
X мальчиков и Y девочек пошли в кинотеатр и купили билеты на подряд идущие места в одном ряду.
Напишите программу, которая выдаст, как нужно сесть мальчикам и девочкам,
чтобы рядом с каждым мальчиком сидела хотя бы одна девочка, а рядом с каждой девочкой — хотя бы один мальчик.

На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
В ответе выведите какую-нибудь строку, в которой будет ровно X символов “B” (обозначающих мальчиков)
и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
Пробелы между символами выводить не нужно.
Если рассадить мальчиков и девочек согласно условию задачи невозможно, выведите строку “Нет решения”.

Пример 1:
Введите кол-во мальчиков: 5
Введите кол-во девочек: 5
Ответ: BGBGBGBGBG

Пример 2:
Введите кол-во мальчиков: 5
Введите кол-во девочек: 3
Ответ: BGBGBBGB

Пример 3:
Введите кол-во мальчиков: 100
Введите кол-во девочек: 1
Ответ: Нет решения """

boys = int(input('Введите кол-во мальчиков: '))
girls = int(input('Введите кол-во девочек: '))

if boys > girls:
    maximum_count = boys
    minimum_count = girls
    maximum = 'b'
    minimum = 'g'
else:
    maximum_count = girls
    minimum_count = boys
    maximum = 'g'
    minimum = 'b'

if maximum_count > minimum_count * 2:
    print('error')
else:
    print(maximum, end='')
    maximum_count -= 1
    while maximum_count != 0:
        if minimum_count == maximum_count:
            print(minimum + maximum, end='')
            minimum_count -= 1
            maximum_count -= 1
            continue
        elif maximum_count > minimum_count:
            print(minimum, end='')
            minimum_count -= 1
            print(maximum * 2, end='')
            maximum_count -= 2
