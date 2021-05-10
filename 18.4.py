"""Задача 1. Шифр Цезаря 2
Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря.
Напомним, что в таком способе шифрования каждая буква заменяется на следующую по алфавиту через K позиций по кругу.
Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования.
Не используйте конкатенацию и сделайте так, чтобы текст был в одном регистре."""

rus_let = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
           'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
           'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

text = input('Введите текст: ').lower()
shift = int(input('Введите сдвиг: '))
secret_text = [(rus_let[(rus_let.index(let) + shift) % len(rus_let)] if let != ' ' else ' ') for let in text]
print(f'Зашифрованное сообщение: {"".join(secret_text)}')

"""Задача 2. Путь к файлу
Все данные сайта лежат в одном проекте. 
При написании кода, внутри этого проекта часто используются абсолютные пути файлов, которые необходимо проверять.
Пользователь вводит абсолютный путь к текстовому файлу, а также проверяемые данные:
диск и расширение файла. Напишите программу, которая проверяет корректность этого пути.

Пример:
Путь к файлу: C:/user/docs/folder/new_file.txt
На каком диске должен лежать файл: C
Требуемое расширение файла: .txt
Путь корректен!"""

path = input('Путь к файлу: ')
disk = input('На каком диске должен лежать файл: ')
expansion = input('Требуемое расширение файла: ')

if not path.startswith(disk):
    print('Не верно указанный диск!')
elif not path.endswith(expansion):
    print('Не верное расширение файла!')
else:
    print('Путь корректен!')

"""Задача 3. Удаление части
На вход в программу подаётся строка, состоящая из прописных и заглавных букв кириллицы. 
Напишите код, который проверяет, каких букв в строке больше, прописных или заглавных. 
Если заглавных букв больше, то сделать все буквы строки заглавными, иначе сделать все прописными.
Подсказка: используйте методы islower() и/или isupper().

Пример:
Введите строку: ПитоН - этО хорошО
Результат: питон - это хорошо

Пример 2:
Введите строку: ПиТоН - ЭтО УДоБнО
Результат: ПИТОН - ЭТО УДОБНО"""

text = input('Введите строку: ')
low = 0
UP = 0

for i_letter in text:
    if i_letter.islower():
        low += 1
    else:
        UP += 1

if low > UP:
    print(text.lower())
else:
    print(text.upper())
