""" Задача 1. Текстовый редактор: возвращение
Мы продолжаем участвовать в разработке нового текстового редактора и делать жизнь обычных пользователей чуть лучше.
В этот раз у нас стоит задача сделать фишку с поиском и заменой символов в выделенной строчке.
Например, человек что-то перечислял в тексте, но ошибся и вместо точек с запятой использовал двоеточия.
Лингвисты негодуют.
Пользователь вводит строку S.
Напишите программу, которая заменяет в строке все двоеточия (:) на точки с запятой (;).
Также подсчитайте количество замен и выведите ответ на экран (и новую строку тоже).
Для решения используйте список.

Пример:
Введите строку: гвозди:шурупы:гайки
Исправленная строка: гвозди;шурупы;гайки
Кол-во замен: 2 """

text = input('Введите строку: ')
array_text = list(text)
new_array = []
count = 0

for _ in array_text:
    if _ == ':':
        count += 1
        new_array.append(';')
        continue
    new_array.append(_)

print('Исправленная строка:', end=' ')
for _ in new_array:
    print(_, end='')
print(f'\nКол-во замен: {count}')

""" Задача 2. Соседи
Дана строка S и номер позиции символа в строке.
Напишите программу, которая выводит соседей этого символа и сообщение о количестве таких же символов среди этих соседей:
их нет, есть ровно один или есть два таких же.

Пример 1:
Введите строку: abbc
Номер символа: 3
Символ слева: b
Символ справа: c
Есть ровно один такой же символ.

Пример 2:
Введите строку: abсd
Номер символа: 3
Символ слева: b
Символ справа: d
Таких же символов нет. """

text = input('Введите строку: ')
number = int(input('Номер символа: '))
array_text = list(text)
count = -1

print(f'Символ слева: {array_text[number - 2]}')
print(f'Символ справа: {array_text[number]}')

for _ in array_text:
    if array_text[number - 1] == _:
        count += 1

if count != 0:
    print(f'Похожих символов: {count}')
else:
    print('Таких же символов нет.')

""" Задача 3. Улучшенная лингвистика
Мы уже писали программу для лингвистов, которая считала количество определённых букв в тексте.
Теперь эту программу нужно улучшить. Есть список из трёх слов, которые вводит пользователь.
Затем вводится сам текст произведения строго по словам. Текст вводится до тех пор, пока не встретится слово end.
Напишите программу, которая посчитает, сколько раз слова пользователя встречаются в тексте.

Пример:
Введите 1 слово: я
Введите 2 слово: год
Введите 3 слово: лучший

Слово из текста: этот
Слово из текста: год
Слово из текста: -
Слово из текста: лучший
Слово из текста: год

Подсчёт слов в тексте
я: 0
год: 2
лучший: 1 """

array_text = []
count = [0, 0, 0]

for _ in range(3):
    text = input(f'Введите {_ + 1} слово: ')
    array_text.append(text)

print()
while text != 'end':
    text = input('Слово из текста: ')
    for _ in array_text:
        if text == _:
            count[array_text.index(_)] += 1

print('\nПодсчет слов в тексте')
for _ in range(3):
    print(f'{array_text[_]}: {count[_]}')