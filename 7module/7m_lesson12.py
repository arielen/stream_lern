""" Задача 12. Замечательные числа
Напишите программу, которая находит и выводит все двузначные числа,
которые равны утроенному произведению своих цифр.
К таким относятся, например, 15 и 24. """

for number in range(10, 100):
    composition = (number // 10) * (number % 10) * 3  # десятые, еденицы, умножение на 3
    if composition == number:
        print(number)
