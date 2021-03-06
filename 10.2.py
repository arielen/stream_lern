""" Задача 1. Матрица
Напишите программу, которая выводит квадратную матрицу размера N на N.
В каждой нечётной строке матрицы идут числа от 1 до N, а в каждой чётной — просто числа, равные номеру этой строки.

Пример: """

N = int(input('Введите размер матрицы: '))

for number in range(1, N + 1):
    for num in range(1, N + 1):
        if number % 2 == 0:
            print(number, end=' ')
        else:
            print(num, end=' ')
    print()

""" Задача 2. Чёрный ящик

Преподаватель показал студентам несколько результатов программы и сказал: 
«Кто догадается, что делает программа и как она это делает, получит зачёт автоматом». 
Студент Миша намерен получить этот зачёт. Он заметил, что в результатах программы есть определённая закономерность. 
Вот некоторые результаты:  
Введите размер матрицы: 6
1 1 3 1 1 6 
2 2 3 2 2 6 
3 3 3 3 3 6 
4 4 3 4 4 6 
5 5 3 5 5 6 
6 6 3 6 6 6 
Введите размер матрицы: 3
1 1 3 
2 2 3 
3 3 3 """

N = int(input('Введите размер матрицы: '))

for number in range(1, N + 1):
    for num in range(1, N + 1):
        if num % 3 == 0:
            print(num, end=' ')
        else:
            print(number, end=' ')
    print()

""" Задача 3. Координатные оси

Напишите программу, которая рисует координатные оси на поле 20×50. Результат должен получиться таким: 
                        |                         
                        |                         
                        |                         
                        |                         
                        |                         
                        |                         
                        |                         
                        |                         
                        |                         
--------------------------------------------------
                        |                         
                        |                         
                        |                         
                        |                         
                        |                         
                        |                         
                        |                         
                        |                         
                        |                         
                        |       """

for vertical in range(20):
    for horizontal in range(50):
        if vertical == 9:
            print('-', end='')
        elif horizontal == 24:
            print('|', end='')
        else:
            print(' ', end='')
    print()