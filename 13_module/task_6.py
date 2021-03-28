print('Задача 6. Недоделка 2')


# Вы всё так же работаете в конторе по разработке игр
# и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.

def change_rev(number, count):
    last_digit = number % 10
    first_digit = number // 10 ** (count - 1)
    between_digits = number % 10 ** (count - 1) // 10
    number = last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit
    return number


def num_count(number):
    count = 0
    temp = number
    while temp > 0:
        count += 1
        temp = temp // 10
    return count


def first_number():
    first_n = int(input("Введите первое число: "))
    first_num_count = num_count(first_n)
    if first_num_count < 3:
        print("В первом числе меньше трёх цифр.")
        return 0
    else:
        first_n = (change_rev(first_n, first_num_count))
        print('Изменённое первое число:', first_n)
        return first_n


def second_number():
    second_n = int(input("\nВведите второе число: "))
    second_num_count = num_count(second_n)
    if second_num_count < 4:
        print("Во втором числе меньше четырёх цифр.")
        return 0
    else:
        second_n = (change_rev(second_n, second_num_count))
        print('Изменённое второе число:', second_n)
        return second_n


def sum_number(first_n, second_n):
    if first_n == 0 or second_n == 0:
        print('\nОшибка, введены неверные числа!')
    else:
        print('\nСумма чисел:', first_n + second_n)


sum_number(first_number(), second_number())
