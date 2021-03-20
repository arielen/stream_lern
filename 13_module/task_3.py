print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225

def reverse_number(num1, num2):
    first_num = ''
    second_num = ''
    sum_reverse = ''

    while num1 != 0:
        first_num += str(num1 % 10)
        num1 //= 10
    print(f'Первое число наоборот: {first_num}')

    while num2 != 0:
        second_num += str(num2 % 10)
        num2 //= 10
    print(f'Второе число наоборот: {second_num}')

    summ = int(first_num) + int(second_num)
    print(f'Сумма: {summ}')

    while summ != 0:
        sum_reverse += str(summ % 10)
        summ //= 10
    print(f'Сумма наоборот {sum_reverse}')


N = int(input('Введите первое число: '))
K = int(input('Введите второе число: '))

reverse_number(N, K)
