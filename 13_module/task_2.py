print('Задача 2. Функция максимума')


# Юра пишет различные полезные функции для Питона,
# чтобы остальным программистам стало проще работать.

# Он захотел написать функцию, 
# которая будет находить максимум из перечисленных чисел.
# Функция для нахождения максимума из двух чисел у него уже есть.

# Юра задумался: может быть, её можно как-то использовать 
# для нахождения максимума уже от трёх чисел?


# Напишите программу, 
# которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.

def max_count(num1, num2):
    if num1 > num2:
        maxx = num1
    else:
        maxx = num2
    return maxx


def search_max():
    number1 = float(input('Введите первое число: '))
    number2 = float(input('Введите второе число: '))
    number3 = float(input('Введите третье число: '))
    max_number = max_count(max_count(number1, number2), number3)
    print(f'Максимальное число из введенных: {max_number}')


search_max()
