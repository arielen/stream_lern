""" Задача 1. Покупка велосипеда
Напишите программу, которую мы разбирали в рамках теории. Нашему ребёнку нужен новый хороший велосипед.
Правда, никто из нас в них не разбирается, всё что нам нужно — чтобы велосипед не был устаревшим
и чтоб скоростей на нём было побольше, а сколько он стоит — пока неважно.
Чтобы не искать велосипед на сайте вручную, мы хотим написать программу,
которая будет проверять каждый велосипед на нужный нам год выпуска и на количество скоростей.
Используя один из логических операторов (and, or), напишите программу из урока,
которая запрашивает год выпуска велосипеда и количество скоростей на нём и выводит на экран сообщение о том,
подходит этот велик или нет. Год выпуска — не старше 2018-го, количество скоростей — не менее 24. """

years = int(input('Введите год выпуска:  '))
speed = int(input('Введите колличество скоростей:  '))

if years >= 2018 and speed >= 24:
    print('Велосипед подходит!')
else:
    print('Велосипед не подходит!')

""" Задача 2. Как поступить?
Илья хочет в лучший вуз страны, а для этого нужно не только хорошо сдать экзамены (балл должен быть больше 280),
но и иметь золотую медаль.
Напишите программу, которая запрашивает у пользователя два числа: результат экзаменов
и наличие золотой медали (0 — нет медали, 1 — медаль есть), а затем проверяет, поступил ли Илья в вуз.
Выведите соответствующее сообщение.

Пример:
Сколько баллов набрал? 290
Есть медаль? 1
Поздравляем! Ты поступил!

Пример 2:
Сколько баллов набрал? 269
Есть медаль? 1
К сожалению, ты не прошёл в наш университет. """

score = int(input('Введите колличество баллов:  '))
medal = int(input('Имеется ли медаль:  '))  # 0 - нет, 1 - да

if score > 280 and medal == 1:
    print('Поздравляем! Ты поступил!')
else:
    print('К сожалению ты не поступил в наш университет!')

""" Задача 3. Бактерии живут комфортно
Биолог Арсений изучает микробы и их поведение при разных температурных нагрузках. 
Он помещает их в специальную среду, где температура скачет в промежутке от 0 до 100 градусов. 
Если же температура в среде выходит за рамки промежутка, то выводится предупреждение.
Напишите программу, которая запрашивает у пользователя температуру, и, 
если она меньше нуля или больше 100, то выводится сообщение об опасности. """

temp = int(input('Введите температуру:  '))

if temp < 0 or temp > 100:
    print('WARNING!')

""" Задача 4. Игра наоборот (необязательная)
Решите две предыдущие задачи другим, альтернативным способом: если для решения вы использовали оператор and,
то теперь решите задачу через оператор or, и наоборот. """

score = int(input('Введите колличество баллов:  '))
medal = int(input('Имеется ли медаль:  '))  # 0 - нет, 1 - да

if medal == 1 or score > 280:
    print('Поздравляем! Ты поступил!')
else:
    print('К сожалению ты не поступил в наш университет!')
