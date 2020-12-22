""" Задача 10. Отрезок
Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль
среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3. """

a = int(input('Введите число a:  '))
b = int(input('Введите число b:  '))
massive = []

for number in range(a, b + 1):
    if number % 3 == 0:
        massive.append(number)

print(sum(massive) / len(massive))
