""" Задача 7. Наибольшая сумма цифр
Вводится N чисел. Среди натуральных чисел, которые были введены, найдите наибольшее по сумме цифр.
Выведите на экран это число и сумму его цифр. """

N = int(input('Сколько ввести цифр: '))
array = []
max_number = 0
sum_number = 0

for input_number in range(N):
    number = int(input('Введите число: '))
    array.append(number)

for number in array:
    if number > max_number:
        max_number = number

# или так: max_number = max(array), можно еще внутри проверять,
# но тогда понадобится переменная для предыдущего максимального

print(f'Максимальное число из введенных: {max_number}.', end=' ')
while max_number != 0:
    sum_number += max_number % 10
    max_number = max_number // 10

print(f'Сумма его чисел: {sum_number}')
