import os

# Задача 1. Иконки
# Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться вся структура его диска:
# папки одними иконками, файлы — другими. Поэтому ему нужен код, который поможет определить, какой тип иконки вставить.
# Напишите программу, которая по заданному абсолютному пути определяет, на что указывает этот путь
# (на директорию, файл, или же путь является ссылкой), и выведите соответствующее сообщение.
# Если путь указывает на файл, то также выведите его размер (сколько он весит в байтах).
# Обеспечьте контроль ввода: проверка пути на существование.
# Подсказка: для вывода размера файла поищите соответствующий метод.
#
# Пример 1:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Это файл
# Размер файла: 605 байт
#
# Пример 2:
# Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
# Указанного пути не существует

path = input('Путь: ')
if os.path.isdir(path):
    print("Это директория")
elif os.path.islink(path):
    print("Это ссылка")
elif os.path.isfile(path):
    print("Это файл")
    print(f"Размер файла: {os.path.getsize(path)} байт")
else:
    print("Указанного пути не существует")


# Задача 2. Поиск файла
# В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах указанной директории.
# Однако, как мы понимаем, файлов с таким названием может быть несколько.
# Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла,
# проходит по всем вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.
#
# Пример:
# Ищем в: C:/Users/Roman/PycharmProjects/Skillbox
# Имя файла: lesson2
#
# Найдены следующие пути:
# C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module18\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module19\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module20\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module21\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module22\lesson2.py

def find_files(cur_path, file_name):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            print(path)
        if os.path.isdir(path):
            find_files(path, file_name)


path = input('Ищем в: ')
name_file = input('Имя файла: ')

find_files(path, name_file)
