"""Задача 1. Простая программа
Напишите программу, которая открывает файл и записывает туда введённую пользователем строку.
Используйте операторы try except else finally. Обработайте возможные ошибки:

Проблема при открытии файла.
Нельзя преобразовать данные в целое.
Неожиданная ошибка."""

text_file = open("text.txt", "a", encoding="utf-8")
try:
    text = int(input("Введите текст: "))
    text_file.write(str(text))
except ValueError:
    print("Нельзя преобразовать данные в целое.")
except FileNotFoundError:
    print("Проблема при открытии файла.")
finally:
    text_file.close()
