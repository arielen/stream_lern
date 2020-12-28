""" Задача 12. Выражение
Дано число x. Напишите программу для вычисления следующего выражения
#(x-1)(x-3)(x-7) * ... * (x-63)
#(x-2)(x-4)(x-8) * ... * (x-64)
"""

# странное задание, если только x не меньше 64 или является отрицательным

x = int(input('Введите значение X: '))
sum_number_up = 1
sum_number_down = 1

for number in range(1, 64, 2):
    sum_number_up *= x - number
    print(number, sum_number_up)

for number in range(2, 64 + 1, 2):
    sum_number_down *= x - number
    print(number, sum_number_down)

S = sum_number_up / sum_number_down

print(f'Сумма равна: {S}')
