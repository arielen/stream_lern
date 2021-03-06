""" Задача 12. Выражение
Дано число x. Напишите программу для вычисления следующего выражения
#(x-1)(x-3)(x-7) * ... * (x-63)
#(x-2)(x-4)(x-8) * ... * (x-64)
"""

# при некоторых числах, таких как 2, 4, 8 - возникает ошибка, но если быть точнее, то значение (2,4,8,16) вычитает себя
# на определенной итерации и при перемножении вся сумма равна 0.

x = int(input('Введите значение X: '))
sum_number_up = 1
sum_number_down = 1

for number in range(1, 6 + 1):
    sum_number_up *= x - 2 ** number + 1
    sum_number_down *= x - 2 ** number
    print(number, sum_number_up, sum_number_down)

S = sum_number_up / sum_number_down

print(f'Сумма равна: {S}')
