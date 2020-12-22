""" Задача 14. ...Теперь можно посчитать и свою
Пока бухгалтер считала среднюю зарплату сотрудников, ей стало интересно,
а не зря ли она работает столько времени на одном месте?
Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.

Пользователь вводит 10 чисел. Напишите программу, которая проверяет, упорядочены ли они по возрастанию. """

hight = True
previous_salary = 0

for mounth in range(1, 11):
    salary = int(input(f'Введите вашу зарплату за {mounth} месяц: '))
    if salary <= previous_salary:
        hight = False
        break
    previous_salary = salary

if hight is True:
    print('Зарплата: возрастает!')
else:
    print('Зарплата: не возрастает!')
