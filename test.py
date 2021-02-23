import math

print('Введите местоположение коня: ')
x = float(input())
y = float(input())
print('Введите местоположение на доске: ')
x_desire = float(input())
y_desire = float(input())
print(f'Конь в клетке ({int(x * 10)}, {int(y * 10)}). Точка в клетке ({int(x_desire * 10)}, {int(y_desire * 10)}).')

if int(x * 10) >= 0 and int(y * 10) >= 0:
    if int(math.fabs((int(x * 10) + int(y * 10)) - (int(x_desire * 10) + int(y_desire * 10)))) == 3 or int(math.fabs(
            (int(x * 10) + int(y * 10)) - (int(x_desire * 10) + int(y_desire * 10)))) == 1:
        print('Да, конь может ходить в эту точку')
    else:
        print('Конь не можнт ходить в этом направлении!')

