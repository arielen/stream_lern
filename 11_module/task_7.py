""" Задача 7. Ход конём
В рамках разработки шахматного ИИ стоит новая задача.
По заданным вещественным координатам коня и второй точки программа должна определить может ли конь ходить в эту точку.
Используйте как можно меньше конструкций if и логических операторов.
Обеспечьте контроль ввода.

Пример:
Введите местоположение коня:
0.071
0.118
Введите местоположение точки на доске:
0.213
0.068
Конь в клетке (0, 1). Точка в клетке (2, 0).
Да, конь может ходить в эту точку. """

import math

while True:
    try:
        print('Введите местоположение коня: ')
        x = float(input())
        y = float(input())
        print('Введите местоположение на доске: ')
        x_desire = float(input())
        y_desire = float(input())

        x_sharp = int(x * 10)
        y_sharp = int(y * 10)
        x_des_sharp = int(x_desire * 10)
        y_des_sharp = int(y_desire * 10)

        if (0 >= x_sharp <= 0.7) or (0 >= y_sharp <= 0.7) or (0 >= x_des_sharp <= 0.7) or (
                0 >= y_des_sharp <= 0.7):
            print(
                f'Конь в клетке ({x_sharp}, {y_sharp}). Точка в клетке ({x_des_sharp}, {y_des_sharp}).')

            if math.fabs((x_sharp + y_sharp) - (x_des_sharp + y_des_sharp)) == 3 or math.fabs(
                    (x_sharp + y_sharp) - (x_des_sharp + y_des_sharp)) == 1:
                print('Да, конь может ходить в эту точку')
            else:
                print('Конь не можнт ходить в этом направлении!')
            break

        else:
            print(
                f'Ваши данные ({x_sharp}, {y_sharp}). Точка в клетке ({x_des_sharp}, {y_des_sharp}). Шахматная доска размером от 0-7',
                f'Введите корректные данные!', sep='\n')

    except ValueError:
        print('Вы ввели не число. Введите корректные данные!')
