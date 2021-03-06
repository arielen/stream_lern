""" Задача 6. Счастливый билетик
В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры, существовало поверье:
если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх, то это к удаче.
Напишите программу, которая получала бы на входе шестизначный номер билета и выводила, счастливый это билет или нет.
К примеру, билеты 666 666 и 252 135 — счастливые, а 123 456 — нет.
Подумайте, нужны ли для решения этой задачи циклы? """

number = int(input('Введите число: '))
left = number // 1000
right = number % 1000
sum_left = 0
sum_right = 0

while left != 0:
    sum_left += left % 10
    sum_right += right % 10
    left //= 10
    right //= 10

if sum_right == sum_left:
    print('Билет счастливый!')
else:
    print('Нет')
