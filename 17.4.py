"""Задача 1. Анализ цен
Нашему другу заказали написать программу, которая анализирует цены на бирже.
Она получает этот пакет данных, но делать что-либо с ним нельзя.
Для нормальной работы аналитической программы берётся новый список, который равен тому, что пришло.
Затем идёт работа с новым списком: если есть отрицательные цены, то программа их зануляет и в конце выводит на экран,
сколько денег мы по итогу потеряли. Получился вот такой код:

original_prices = [-12, 3, 5, -2, 1]
new_prices = original_prices
for i in range(len(original_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0
print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))

Однако при таких входных данных программа почему-то работает неправильно:
она выводит ответ 0, когда правильный ответ 14.
Помогите другу исправить программу, а также сделайте так,
чтобы список цен генерировался случайно (диапазон можно выбрать любой)."""

import random

original_prices = [random.randint(-10, 10) for _ in range(5)]
new_prices = original_prices[:]
for i in range(len(original_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0
print("Мы потеряли: ", abs(sum(original_prices) - sum(new_prices)))

"""Задача 2. Срезы
Дан список чисел:
nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
Напишите программу, которая выводит на экран шесть ответов:
В первой строке выведите первые пять элементов списка.
Во второй строке выведите весь список, кроме последних двух элементов.
В третьей строке выведите все элементы с чётными индексами.
В четвёртой строке выведите все элементы с нечётными индексами.
В пятой строке выведите все элементы в обратном порядке.
В шестой строке выведите все элементы списка через один в обратном порядке, начиная с последнего.
Для решения используйте только срезы (и без функции len).

Результат:
[48, -10, 9, 38, 17]
[48, -10, 9, 38, 17, 50, -5, 43]
[48, 9, 17, -5, 46]
[-10, 38, 50, 43, 12]
[12, 46, 43, -5, 50, 17, 38, 9, -10, 48]
[12, 43, 50, 38, -10]"""

nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
print(nums[:5])
print(nums[:-2])
print(nums[::2])
print(nums[1::2])
print(nums[::-1])
print(nums[::-2])

"""Задача 3. Удаление части
Дан список из N чисел, а также числа А и В (можно сгенерировать случайно, при этом А < B). 
Напишите программу, которая удаляет элементы списка с индексами от А до В. 
Не используйте дополнительные переменные и методы списков."""

N = int(input('Длинна списка: '))
A = random.randint(0, N)
B = random.randint(A, N)
nums = [random.randint(0, 50) for _ in range(N)]
print(f'A = {A}\nB = {B}\nСписок: {nums}')
nums = nums[A:B]
print(nums)
