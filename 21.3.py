import random
from ast import literal_eval

"""Задача 1. Ошибка
В одном проекте на 10 000 строк кода произошла критическая ошибка.
Хорошо, что старший разработчик быстро её нашёл и исправил.
Он решил проверить, смогли бы вы её исправить, если бы его не было на месте.
Поэтому он написал для вас код с аналогичной ошибкой:

import random

def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)

nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}

change_dict(common_dict)
print(common_dict)

Суть кода в том, что у вас есть общий словарь из нескольких ключей, значения которых равны ранее объявленным переменным.
Затем вызывается функция, которая должна изменять значения словаря, добавляя к значениям случайное число,
в зависимости от типа данных. Но при этом меняются и ранее объявленные переменные.
Исправьте эту ошибку и убедитесь, что nums_list, some_dict и uniq_nums не меняются."""


def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)


nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
common_dict = {1: [num for num in nums_list], 2: {key: value for key, value in some_dict.items()},
               3: {num for num in uniq_nums}, 4: (10, 20, 30)}

change_dict(common_dict)
print(nums_list)
print(some_dict)
print(uniq_nums)
print(common_dict)

"""Задача 2. Непонятно!
Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками, объектами и их id.
Видя, как он мучается, вы решили добить помочь ему и объяснить эту тему наглядно.
Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых данных,
информацию о его изменяемости, а также id этого объекта.

Пример 1:
Введите данные: привет

Тип данных: str (строка)
Неизменяемый (immutable)
Id объекта: 1705156583984

Пример 2:
Введите данные: {‘a’: 10, ‘b’: 20}

Тип данных: dict (словарь)
Изменяемый (mutable)
Id объекта: 1705205308536"""


def valid_data(data):
    type_variable = {'Изменяемый (mutable)': [dict, set, list],
                     'Неизменяемый (immutable)': [int, float, str, tuple]}
    types = type(literal_eval(data))
    type_data = ''
    for i_key, i_value in type_variable.items():
        if types in i_value:
            type_data += i_key
    print(f'\nТип данных: {types}')
    print(f'{type_data}')
    print(f'ID объекта: {id(data)}')


data_input = input('Введите данные: ')
valid_data(data_input)
