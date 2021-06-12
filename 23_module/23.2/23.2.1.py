"""Задача 1. Пятый элемент
В курсе по программированию студенту дали простую задачу:
умножить константу (число 42) на пятый элемент строки, введённой пользователем.
Вот код студента:

BRUCE_WILLIS = 42

input_data = input('Введите строку: ')
leeloo = int(input_data[4])
result = BRUCE_WILLIS * leeloo
print(f'- Leeloo Dallas! Multi-pass № {result}!')

Модифицируйте этот код, обработав исключения для произвольных входных параметров:
ValueError — невозможно преобразовать к числу,
IndexError — выход за границы списка,
остальные исключения.
Для каждого типа исключений выведите на консоль соответствующее сообщение."""

BRUCE_WILLIS = 42

try:
    input_data = input('Введите строку: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError:
    print("Невозможно преобразовать к числу")
except IndexError:
    print("Выход за границы списка")
