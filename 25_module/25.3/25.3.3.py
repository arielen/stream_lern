# Задача 3. Кастомные исключения
# Исключения в Python также являются классами, и все они берут свои истоки от самого главного класса — Exception.
# И для создания своего собственного класса ошибки достаточно написать его дочерний класс.
# Например:
#
# class MyOwnException(Exception):
#     pass
#
# raise MyOwnException('Это моя ошибка!')
#
# Причём содержимое объекта исключения чаще всего так и оставляют (просто pass),
# чтобы не сломать автоматические обработчики исключений.
#
# Напишите программу, которая считывает из файла numbers.txt пары чисел,
# делит первое число на второе и выводит ответ на экран.
# Если первое число меньше второго, то программа выдаёт исключение DivisionError (нельзя делить большее на меньшее).
#
# Дополнительно, с помощью try except, можно обработать исключение на своё усмотрение.


class DivisionError:
    pass


with open("numbers.txt", "r", encoding="utf-8") as file:
    for i_string in file:
        try:
            massive = [int(num) for num in i_string.split()]
            if massive[0] < massive[1]:
                raise DivisionError("Первое значение меньше второго!")
            else:
                print(massive[0] / massive[1])
        except DivisionError:
            raise Exception
