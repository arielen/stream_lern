""" Выведите на экран прямоугольник из нулей. Количество строк вводит пользователь, количество столбцов равно 5. """

string = int(input('Введите колличество строк: '))

for rectangle in range(0, string):
    if rectangle == 0 or rectangle == string-1:
        print('0'*5)
    else:
        print(0, ' ', 0)