""" Задача 1. Таблица кубов
Паше для проекта по математике нужна таблица кубов (третья степень числа) только чётных чисел от 1 до N.
Напишите программу, которая выведет ему эту таблицу на экран.
Не используйте условные операторы, выведите формулу, как мы сделали это в уроке. """

n = int(input('Введите число: '))

for number in range(1, n // 2 + 1):
    number *= 2
    print(f'Куб числа {number} = {number ** 3}')

""" Задача 2. Деление клетки
Реализуйте программу, разобранную в уроке.

В одной лаборатории наблюдают за одноклеточной амёбой. Мы знаем, что каждые три часа она делится на 2 клетки. 
Нам нужно для этой лаборатории написать программу,
которая будет выводить сколько прошло часов и сколько получилось клеток. 
Также нас попросили писать на каждом этапе деления сколько осталось часов до завершения наблюдения,
чтобы ученым было проще формулировать выводы на определённом этапе наблюдения.

Пример сообщений:

Прошло часов: 3.
Клеток: 2.
Часов до конца эксперимента: 12

Прошло часов: 6... """

total_hours = int(input('Введите колличество часов: '))
ameba = 1

for hour in range(1, total_hours // 3 + 1):
    ameba *= 2
    print(f'Прошло часов: {hour * 3}', f'Клеток: {ameba}', f'Часов до конца эксперемента: {total_hours - hour * 3}', '',
          sep='\n')

""" Задача 3. Марсоход
Робот Валли помогает человечеству и исследует поверхность Марса. 
С Земли ему говорят, сколько примерно метров ему нужно будет проехать. 
Валли останавливается каждые 4 метра и сообщает землянам сколько метров он прошёл,
сколько ещё ехать и какой у него остался коэффициент прочности 
(изначально он равен 100, каждые 4 метра уменьшается на  5/2). 
Реализуйте программу для Валли, чтобы он мог держать землян в курсе событий. """

meters = int(input('Введите колличество метров: '))
archon = 100

for meter in range(1, meters // 4 + 1):
    archon -= 5 / 2
    print(f'Валли прошел {meter * 4}м.', f'Осталось ехать: {meters - meter * 4}м.', f'Прочность: {archon}', '',
          sep='\n')

""" Задача 4. Квадраты нечётных чисел
Вводится число N. Напишите программу, которая выводит квадраты нечетных чисел от 1 до N. 
Нельзя использовать условные операторы. 
Можно использовать цикл while, но постарайтесь всё-таки решить с помощью конструкции for in range. 
Не нужно искать решение в интернете, попробуйте подумать сами, в следующем уроке мы обязательно разберём эту задачу. """

n = int(input('Введите число: '))

for number in range(1, n + 1, 2):
    print(f'Квадрат числа {number} = {number ** 2}')
