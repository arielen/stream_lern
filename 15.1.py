""" Задача 1. Таблица степеней

Аркадий как-то раз написал программу для вывода таблицы степеней для определённых чисел.
Недавно он узнал про такую штуку, как списки, и решил программу немного переписать, а заодно усовершенствовать её.
По его задумке, вначале есть всего три числа: 3, 7 и 5,
а затем с помощью бесконечного цикла программа запрашивает новое число,
закидывает его в конец текущего списка чисел и выводит вторую, третью и четвёртую степень каждого числа текущего списка.
Вот какая программа получилась у Аркадия:

Пример верного результата:
Новое число: 1
Текущий список чисел: [3, 7, 5, 1]
9 27 81
49 343 2401
25 125 625
1 1 1

Новое число: 2
Текущий список чисел: [3, 7, 5, 1, 2]
9 27 81
49 343 2401
25 125 625
1 1 1
4 8 16"""

numbers = [3, 7, 5]
while True:
    number = int(input('Новое число: '))
    numbers.append(number)
    print('Текущий список чисел:', numbers)
    for num in numbers:
        print(num ** 2, num ** 3, num ** 4, sep='\t')
    print()

""" Задача 2. Очень простая задача
У вас есть список numbers.
Напишите программу, которая заполняет список числами от 0 до 100 и выводит его на экран. """

numbers = [3, 7, 5]

for _ in range(0, 101):
    numbers.append(_)

print(numbers)

""" Задача 3. Контроль
В любой компании есть список сотрудников. Руководство одной компании хочет знать, на рабочем месте ли сейчас сотрудник.
У каждого сотрудника есть пропуск со своим ID-номером (это положительное число),
список активных пропусков сотрудников известен заранее.
Напишите программу, которая сначала запрашивает у пользователя количество сотрудников в офисе, ID их пропусков,
а затем запрашивает ID пропуска, который нужно найти в этом списке.
Если такой есть, то вывести «Сотрудник на месте», а иначе «Сотрудник не работает!».

Пример:
Кол-во сотрудников в офисе: 4
ID сотрудника: 10
ID сотрудника: 20
ID сотрудника: 30
ID сотрудника: 40
Какой ID ищем? 35
Сотрудник не работает! """

count_worker = int(input('Кол-во сотрудников в офисе: '))
worker_ID = []

for _ in range(0, count_worker):
    id = int(input('ID сотрудника: '))
    worker_ID.append(id)

search_ID = int(input('Какой ID ищем? '))

if search_ID in worker_ID:
    print('Сотрудник на месте!')
else:
    print('Сотрудника нет на месте!')