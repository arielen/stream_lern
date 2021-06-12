"""Задача 2. Возраст
Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.
Напишите программу, которая считывает файл, даёт имя для каждого возраста (можно просто использовать буквы алфавита)
и выводит результат в новый файл result.txt в формате «имя — возраст».
Программа должна обрабатывать следующие ошибки и выводить сообщение на экран:

1) Попытка создания файла, который уже существует.
2) На чтение ожидался файл, но это оказалась директория.
3) Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).

При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок."""
import random


def create_dict(ages):
    names = ['Варвара', 'Ева', 'Артемий', 'София', 'Егор', 'Леонид', 'Анастасия', 'Тимофей', 'Андрей', 'Любовь']
    dictionary_names = {}
    for i_age in ages:
        print(i_age)
        try:
            if int(i_age) > 70 or int(i_age) < 0:
                continue
            dictionary_names.update({names[random.randint(0, len(names) - 1)]: int(i_age)})
        except ValueError:
            print("Возраст не может содержать буквы")
    return dictionary_names


ages_file = open("ages.txt", "r", encoding="utf-8")
ages_people = ages_file.read().split()
ages_file.close()
peoples = create_dict(ages_people)

try:
    result_file = open("result.txt", "w", encoding="utf-8")
    for i_names, i_ages in peoples.items():
        result_file.write(f"{i_names} - {i_ages}\n")
    result_file.close()
except FileExistsError:
    print("Попытка создания файла, который уже существует.")
