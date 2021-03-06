""" Задача 1. Опять налоги
У правительства одной из стран есть бухгалтерская программа,
которая суммирует налоги её граждан, компаний плюс НДС с товаров.
Страна развивалась, суммарные налоги увеличивались, и бухгалтеры заметили,
что после добавления к общей сумме налогов некого НДС от какого-то продукта общая сумма перестала меняться…

Нужно помочь бухгалтерам: напишите функцию, на вход которой подаются два числа —
общая сумма налога tax и новый налог new_tax, который нужно добавить к общей сумме.
Функция должна проверять, возможно ли сложить эти два числа или нет, и выводить соответствующее сообщение о том,
увеличится ли бюджет или нет.

Пример 1:
Введите бюджет страны: 1.23e2
Новые поступления (налог): 1.2e1
Результат: Бюджет увеличится

Пример 2:
Введите бюджет страны: 1.231221200034e12
Новые поступления (налог): 1.2e-2
Результат: Бюджет не изменится
"""


def tax_count(tax, new_tax):
    budget = tax + new_tax
    if int(budget) - tax == 0:
        return 'Бюджет не изменится'
    else:
        return 'Бюджет увеличится'


tax = float(input('Введите бюджет страны: '))
new_tax = float(input('Новые поступления (налог): '))

print(f'Результат: {tax_count(tax, new_tax)}')

""" Задача 2. Сравнение
Так как в Python операции с вещественными числами могут давать неожиданные результаты
(в частности, 0.1 + 0.2 не будет в точности равняться 0.3), стоит задача с этим как-то справляться.

Напишите функцию eqv, которая принимает три числа и затем сравнивает сумму первых двух чисел
с третьим с определённой степенью точности: до 15-го знака после точки.
Если равенство выполняется, то функция возвращает True, иначе возвращает False.

Пример 1:
Введите первое число: 1.1
Введите второе число: 2.2
Введите третье число: 3.3
True

Пример 2:
Введите первое число: 1e-14
Введите второе число: 1e-14
Введите третье число: 3e-14
False """


def eqv(first, second, third):
    summ = first + second
    if abs(summ - third) < 1e-15:
        return True
    else:
        return False


first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
third_number = float(input('Введите третье число: '))

print(eqv(first_number, second_number, third_number))
