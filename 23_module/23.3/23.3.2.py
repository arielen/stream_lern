"""Задача 2. Старая задача
Возьмите любую задачу из домашнего задания, например, предыдущего модуля и оформите её решение
 в виде try except finally (можно ещё и else), обрабатывая возможные ошибки.
Посмотрев на то, что получилось, попробуйте ответить себе на такой вопрос:
когда стоит использовать обработку исключений и когда она будет излишней?"""

import collections
import zipfile


def unzip(archive):
    try:
        zfile = zipfile.ZipFile(archive, "r")
        for i_file_name in zfile.namelist():
            zfile.extract(i_file_name)
        zfile.close()
    except zipfile.BadZipfile:
        print("Файл не является zip-архивом")


def collect_stats(file_name):
    result = {}
    if file_name.endswith(".zip"):
        unzip(file_name)
        file_name = "".join((file_name[:-3], "txt"))
    text_file = open(file_name, "r", encoding="utf-8")
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():  # проверка на отношение символа
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
    text_file.close()
    return result


def print_stats(stats):
    print("+{:-^19}+".format("+"))
    print("|{: ^9}|{: ^9}|".format("буква", "частота"))
    print("+{:-^19}+".format("+"))
    for char, count in stats.items():
        print("|{: ^9}|{: ^9}|".format(char, count))
    print("+{:-^19}+".format("+"))


def sort_by_frequency(stats_dict):
    sorted_values = sorted(stats_dict.values(), reverse=True)
    sorted_dict = collections.OrderedDict()
    for i_value in sorted_values:
        for j_key in stats_dict.keys():
            if stats_dict[j_key] == i_value:
                sorted_dict[j_key] = stats_dict[j_key]
    return sorted_dict


try:
    file_name = "voyna-i-mir.html"
    stats = collect_stats(file_name)
    stats = sort_by_frequency(stats)
    print_stats(stats)
except FileNotFoundError:
    print("Такой файл не найден")
