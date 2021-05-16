import random

"""Задача 1. Пунктуация
Напишите программу, которая считает количество знаков пунктуации в символьной строке.
К знакам пунктуации относятся символы из набора ".,;:!?".
Набор должен храниться в виде множества.

Пример:
Введите строку: Я! Есть. Грут?! Я, Грут и Есть.
Количество знаков пунктуации: 6"""

symbols_punctuation = ".,;:!?"
text = set(input('Введите строку: '))
count = [symbols for symbols in symbols_punctuation if symbols in symbols_punctuation]
print(f'Количество знаков пунктуации: {len(count)}')

"""Задача 2. Семинар
На одном семинаре по теории множеств нужно показать наглядный пример, как эти множества работают. 
Для начала было сгенерировано два набора чисел: 

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

Вас попросили написать программу, которая будет наглядно демонстрировать работу со множествами с помощью этих чисел.

Напишите программу, которая преобразует списки во множества и убирает повторяющиеся элементы. 
Затем удаляет минимальный элемент из каждого множества и добавляет туда случайное число в диапазоне от 100 до 200. 
Затем выполните следующие действия со множествами: 
Вывести все элементы множеств (объединение). 
Вывести только общие элементы (пересечение).
Вывести элементы, входящие в nums_2, но не входящие в nums_1.

Пример результата:
1-е множество: {1, 2, 3, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22, 24, 26, 27, 29}
2-е множество: {1, 5, 7, 8, 9, 11, 12, 13, 15, 16, 19, 21, 22, 23, 24, 29, 30}

Минимальный элемент 1-го множества: 1
Минимальный элемент 2-го множества: 1

Случайное число для 1-го множества: 126
Случайное число для 2-го множества: 169

Объединение множеств: {2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 29, 30, 169, 126}
Пересечение множеств: {7, 8, 11, 12, 13, 15, 16, 19, 21, 22, 24, 29}
Элементы, входящие в nums_2, но не входящие в nums_1: {5, 9, 169, 23, 30}"""

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

plenty_1 = set(nums_1)
plenty_2 = set(nums_2)
print(f'1-e множество: {plenty_1}')
print(f'2-е множество: {plenty_2}')
print(f'Минимальный элемент 1-го множества: {min(plenty_1)}')
print(f'Минимальный элемент 1-го множества: {min(plenty_2)}')
random_from1 = random.randint(100, 200)
random_from2 = random.randint(100, 200)
print(f'Случайное число для 1-го множества: {random_from1}')
print(f'Случайное число для 2-го множества: {random_from2}')
plenty_1.discard(min(plenty_1))
plenty_1.add(random_from1)
plenty_2.discard(min(plenty_2))
plenty_2.add(random_from2)
print(f'Объединение множеств: {plenty_1 | plenty_2}')
print(f'Пересечение множеств: {plenty_1 & plenty_2}')
print(f'Элементы, входящие в nums_2, но не входящие в nums_1: {plenty_2 - plenty_1}')

"""Задача 3. Различные цифры
Напишите программу, которая находит все различные цифры в символьной строке. 
Для решения используйте множество (цифры будут различные, и поиск во множестве намного быстрее, чем в списке).
Подсказка: можно использовать вот такое сравнение '0'<=x<='9'

Пример:
Введите строку: ab1n32kz2
Различные цифры строки: 123"""

numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
text = set(input('Введите строку: '))
diff_numbers = text & numbers
print(f'Различные цифры строки: {"".join(sorted(diff_numbers))}')
