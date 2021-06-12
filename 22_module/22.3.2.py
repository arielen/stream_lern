import os

"""Задача 2. Поиск файла 2
Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только программисту. 
Таким образом, с ними можно работать точно так же, как и с обычными текстовыми файлами.
Используя функцию поиска файла из предыдущего урока, реализуйте программу, 
которая находит внутри указанного пути все файлы с искомым названием и 
выводит на экран текст одного из них (выбор можно сгенерировать случайно).
Подсказка: можно использовать, например, список для сохранения найденного пути."""


def find_files(cur_path, file_name, list_find_files=[]):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            list_find_files.append(path)
        if os.path.isdir(path):
            find_files(path, file_name)
    return list_find_files


path = input('Ищем в: ')
name_file = input('Имя файла: ')

list_files = find_files(path, name_file)
if list_files:
    print("\nНайдены следующие пути:")
    for i_index, i_elem in enumerate(list_files):
        print(i_index + 1, i_elem)

    choice = int(input('\nКакой файл выбрать?  '))
    print(f'Открытие {choice} файла: {list_files[choice - 1]}')
    file = open(f"{list_files[choice - 1]}", "r", encoding="utf-8")
    for i_string in file:
        print(i_string, end="")
    file.close()
else:
    print('Файл с таким именем не найден')
