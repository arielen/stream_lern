""" Задача 1. Сумма чисел 2
Пользователь вводит число N. Напишите функцию summa_n, которая принимает одно целое положительное число N
и находит сумму всех чисел от 1 до N включительно.
Функция вызывается два раза: сначала от числа N, а затем от полученной суммы.

Пример работы программы:
Введите число: 5
Сумма от 1 до 5 = 15
Сумма от 1 до 15 = 120 """


def summa_n(number):
    summa = 0
    for num in range(number + 1):
        summa += num
    return summa


N = int(input('Введите число: '))
first_sum = summa_n(N)
print(f'Сумма от 1 до {N} = {first_sum}')
second_sum = summa_n(first_sum)
print(f'Сумма от 1 до {first_sum} = {second_sum}')

""" Задача 2. «Назад в будущее»
Вы — один из разработчиков языка программирования Python, и вы пишете специальный математический модуль,
который можно было бы просто подключить внутри программы и облегчить жизнь всем программистам.
Реализуйте функцию gcd, которая получает два параметра — два числа — и возвращает наибольший общий делитель этих двух чисел.

Пример работы программы:
Введите первое число: 6
Введите второе число: 10
НОД = 2 """


def gcd(first_num, second_num):
    if first_num > second_num:
        minima = second_num
    else:
        minima = first_num
    for div in range(1, minima):
        if first_num % div == 0 and second_num % div == 0:
            max_div = div
    return max_div


first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
print(f'НОД = {gcd(first, second)}')

""" Задача 3. Приоритет задач
В одном дата-центре ресурсы распределены так, что сначала обрабатываются крупные задачи, а затем уже идут небольшие.
Каждая из этих задач, по сути, просто огромный поток цифр.
Ваша задача, как программиста этого центра, написать программу,
которая поможет определять, какую из задач нужно решать в первую очередь.
Вводится последовательность из N чисел.
Нужно определить номер числа, у которого больше всего цифр, и вывести на экран соответствующее сообщение.
Если число отрицательное, то считать его за 0.
Для подсчёта количества цифр реализуйте функцию numeral_count.

Пример работы программы:
Введите кол-во задач: 4
Введите число: 6
Введите число: 14
Введите число: 1
Введите число: 13434

Первая задача на обработку: 13434 """


def numeral_count(number):
    if number < 0:
        print('Число отрицательное! Обнуляю.')
        return 0
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


task = int(input('Введите кол-во задач: '))

count = 0
for num in range(task):
    number = int(input('Введите число: '))
    if numeral_count(number) > count:
        count = numeral_count(number)
        priority = number

print(f'Первая задача на выполнение: {priority}')