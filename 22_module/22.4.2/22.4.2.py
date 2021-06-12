# Задача 2. Всё в одном
# Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком в другой город, и там у него случилась беда:
# его диск пришлось отформатировать, а доступ в интернет отсутствует.
# Остался только телефон с мобильным интернетом.
# Так как со связью (и с памятью) проблемы, друг попросил вас скинуть одним файлом все решения и скрипты,
# которые у вас сейчас есть.
# Напишите программу, которая копирует код каждого скрипта в папке проекта python_basic в файл scripts.txt,
# разделяя код строкой из 40 символов *.
#
# Пример содержимого файла scripts.txt:
# import platform
# import sys
# info = 'OS info is \n{}\n\nPython version is {} {}'.format(
#     platform.uname(),
#     sys.version,
#     platform.architecture(),
# )
# print(info)
#
# with open('os_info.txt', 'w', encoding='utf8') as file:
#     file.write(info)
# ****************************************
# print("Введите первую точку")
# x1 = float(input('X: '))
# y1 = float(input('Y: '))
# print("\nВведите вторую точку")
# x2 = float(input('X: '))
# y2 = float(input('Y: '))
#
# print("Уравнение прямой, проходящей через эти точки:")
# x_diff = x1 - x2
# y_diff = y1 - y2
# if x_diff == 0:
#     print("x = ", x1)
# elif y_diff == 0:
#     print("y = ", y1)
# else:
#     k = y_diff / x_diff
#     b = y2 - k * x2
#     print("y = ", k, " * x + ", b)
# ****************************************
# …….

import os


def find_files_py(cur_path, list_find_files=[]):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isdir(path):
            find_files_py(path)
        elif os.path.splitext(path)[1] == ".py":
            list_find_files.append(path)
    return list_find_files


data = find_files_py(r"C:\Users\elfie\Desktop")

for i_link in data:
    print(i_link)
    file_python = open(f"{i_link}", "r", encoding="utf-8")
    data = "".join(file_python)
    file_scripts = open("scripts.txt", "a", encoding="utf-8")
    file_scripts.write(data)
    file_scripts.write('\n' + '*' * 40 + '\n')
    file_python.close()
    file_scripts.close()
