import random

"""Задача 1. Саботаж!
Какой-то нехороший человек решил подпортить жизнь frontend-разработчикам и добавил в код сайта символ ~ (тильда).
Но программисты быстро решили эту проблему, пройдясь по всему коду маленькой программой.
Пользователь вводит строку. Напишите программу, которая проходит по строке и выводит в консоль индексы символа ~.
Для решения этой задачи (и остальных тоже) используйте функцию enumerate.

Пример:
Строка: so~mec~od~e
Ответ: 2 6 9 """

text = input('Строка: ')
print('Ответ: ', end='')
for index, symbol in enumerate(text):
    if symbol == '~':
        print(index, end=' ')
"""Задача 2. Словари из списков
Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита (могут повторяться).
Затем для каждого списка создайте словарь из пар «индекс — значение» и выведите оба словаря на экран.
Подсказка: random

Пример:
Первый список: ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
Второй список: ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']

Первый словарь: {0: 'й', 1: 'р', 2: 'с', 3: 'г', 4: 'а', 5: 'а', 6: 'т', 7: 'ж', 8: 'е', 9: 'к'}
Второй словарь: {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}"""

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
first_list = list(alphabet[random.randint(0, 33)] for _ in range(10))
second_list = list(alphabet[random.randint(0, 33)] for _ in range(10))
print(f'Первый список: {first_list}')
print(f'Второй список: {second_list}\n')

first_dict = {index: symbol for index, symbol in enumerate(first_list)}
second_dict = {index: symbol for index, symbol in enumerate(second_list)}
print(f'Первый словарь: {first_dict}')
print(f'Второй словарь {second_dict}')
"""Задача 3. Универсальная программа
Один заказчик попросил нас написать небольшой скрипт для своих криптографических нужд.
При этом он заранее предупредил, что скрипт должен уметь работать с любым итерируемым типом данных.
Напишите функцию, которая возвращает список из элементов итерируемого объекта
(кортежа, строки, списка, словаря), у которых индекс чётный.

Пример 1:
Допустим, есть такая строка: 'О Дивный Новый мир!'
Результат: ['О', 'Д', 'в', 'ы', ' ', 'о', 'ы', ' ', 'и', '!']

Пример 2:
Допустим, есть такой список: [100, 200, 300, 'буква', 0, 2, 'а']
Результат: [100, 300, 0, 'а']

Примечание: для проверки типа можно использовать функцию
isinstance(<элемент>, <тип данных>), которая возвращает True,
если элемент принадлежит к этому типу данных, и возвращает False в противном случае."""


def iteration_even(elem):
    if isinstance(elem, dict):
        result = list(elem.get(symbol) for index, symbol in enumerate(elem) if index % 2 == 0)
    else:
        result = list(symbol for index, symbol in enumerate(elem) if index % 2 == 0)
    return result


text = 'О Дивный Новый мир!'
spisok = [100, 200, 300, 'буква', 0, 2, 'а']
sad = 1, 2, 3, 4, 5, 6, 7
dictionary = {
    1: 2,
    2: 3,
    3: 4,
    5: 6,
    7: 8
}

print(f'Результат: {iteration_even(text)}')
print(f'Результат: {iteration_even(spisok)}')
print(f'Результат: {iteration_even(sad)}')
print(f'Результат: {iteration_even(dictionary)}')
