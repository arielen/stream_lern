""" Задача 1. Возможности компьютера
В одной IT-компании тестируют возможности различных языков программирования, компиляторов и, конечно же, компьютеров.
Компания дала вам задачу понять, какое самое маленькое возможное число можно получить путём постоянного деления числа на 2.
Изначально число равно единице.
Также, помимо самого числа, компания просит вывести количество делений.
Реализуйте такую программу. """


def div_count(number):
    count = 0
    while number != 0:
        number /= 2
        if number != 0:
            max_number = number
        count += 1
    print(f'Максимальное число делений: {count}')
    print(f'Минимальное число при постоянном делении на 2: {max_number}')


number = int(input('Введите число для нахождения делений: '))

div_count(number)

""" Задача 2. Тестирование
Команде программистов отдали на тестирование новую модель суперкомпьютера.
Для начала программисты решили проверить, как у компьютера обстоят дела с вычислениями вещественных чисел.
Разработчики компьютера предупредили, что на входе он работает только с экспоненциальной формой числа.

Пользователь вводит число N в экспоненциальной форме, где мантисса всегда равна числу от 1 до 9, а порядок меньше нуля.
Также есть переменная Х, которая изначально равна единице.
Посчитайте, сколько раз нужно прибавить N к Х, чтобы оно перевалило за двойку.
Дополнительно: обеспечьте контроль ввода.

Пример 1:
Введите число в эксп. форме: 1e-3
Кол-во прибавлений: 1001

Пример 2:
Введите число в эксп. форме: 5.02e-1
Кол-во прибавлений: 2 """


def count_plus(number):
    X = 1
    count = 0
    if number <= 0:
        print('Число меньше нуля. Обнуляю.')
        return count
    while X <= 2:
        X += number
        count += 1
    return count


N = float(input('Введите число в эксп. форме: '))

print(f'Кол-во прибавлений: {count_plus(N)}')

""" Задача 3. Урок информатики
На одном из уроков информатики учитель объяснял тему «Числа с плавающей точкой»,
но несколько учеников никак не могли понять, почему эта точка «плавает» и как вообще выглядят числа в такой форме.
Для наглядности учитель написал программу, которая берёт число больше десяти и выводит его в формате плавающей точки.

Пользователь вводит положительное число x (x > 10).
Напишите функцию, которая выводит его в формате плавающей точки, то есть x=a *10 ** b, где 1≤a<10.

Пример 1:
Введите число: 16
Формат плавающей точки: x = 1.6 * 10 ** 1

Пример 2:
Введите число: 92345
Формат плавающей точки: x = 9.2345 * 10 ** 4
"""


def floating_dot(number):
    degree = 0
    while number > 10:
        number /= 10
        degree += 1
        floating = (f'{str(number)} * 10 ** {degree}')
    return floating


N = int(input('Введите число: '))
print(f'Формат плавающей точки: x = {floating_dot(N)}')
