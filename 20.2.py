import math
import random

"""Задача 1. Создание кортежей
Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно.
Также заполните второй кортеж числами от −5 до 0.
Объедините два кортежа, создав тем самым третий кортеж.
С помощью метода кортежа определите в нём количество нулей.
Выведите на экран третий кортеж и количество нулей в нём."""

nums_1 = tuple([num for num in range(6)])
nums_2 = tuple([num for num in range(-5, 1)])
nums_3 = tuple(sorted({num for num in nums_2} | {num for num in nums_1}))
print(f'Количество "0" в nums_3: {nums_3.count(0)}')

"""Задача 2. Цилиндр
Андрей однажды уже писал функции для расчёта площади сферы и объёма шара.
И теперь для своей курсовой работы ему пришлось связаться с цилиндрами.
Пользователь вводит два значения: радиус и высоту. Напишите функцию для расчёта площади боковой поверхности цилиндра
и его полной площади. Функция должна возвращать два эти значения.
После этого в основной программе выводятся оба ответа в две строки.
Площадь боковой поверхности (r — радиус, h — высота):
side = 2п * r * h
Полная площадь (S — площадь круга):
full = side + 2 * S
"""


def side_calc(radius, height):
    sid = 2 * math.pi * radius * height
    fulling = sid + 2 * math.pi * radius ** 2
    return round(sid, 2), round(fulling, 2)


R = int(input('Введите радиус: '))
h = int(input('Введите высоту: '))
side, full = side_calc(R, h)
print(f'Площадь боковой фигуры: {side}\nПолная площадь: {full}')

"""Задача 3. Неправильный код
Дан код, в котором должно происходить следующее: изначально есть кортеж из пяти чисел.
Затем вызывается функция, которая получает на вход кортеж чисел, генерирует случайный индекс и случайное значение,
а затем по этим индексу и значению меняет сам кортеж.
Функция должна возвращать кортеж и случайное значение.
В основном коде функция используется два раза, и на экран два раза выводится новый кортеж и случайное значение.
Причём второй раз выводится сумма первого случайного значения и второго.
Однако код, который вам дали, оказался нерабочим. Исправьте его в соответствии с описанием.

import random

def change(nums):
    index = random.randint(0, 5)
    value = random.randint(100, 1000)
    nums[index] = value
    return nums, value

my_nums = 1, 2, 3, 4, 5

new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums = change(new_nums)
rand_val += change(new_nums)
print(new_nums, rand_val)"""


def change(nums):
    nums_list = list(nums)
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    nums_list[index] = value
    nums = tuple(nums_list)
    return nums, value


my_nums = 1, 2, 3, 4, 5

new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums = change(new_nums)[0]
rand_val += change(new_nums)[1]
print(new_nums, rand_val)
