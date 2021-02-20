""" Вычислить M = (ln x1 + cos2 x2)/ 8,2,
где x1 – меньший из корней, x2 – больший из корней уравнения
2x2 + 5x - 3 = 0
 """

import math

# 2x**2 + 5x - 3 = 0
a = 2
b = 5
c = -3

D = b ** 2 - 4 * a * c
print(D)
if D > 0:
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    print(x1, x2)
    if x1 > x2:
        x2, x1 = x1, x2
        print(x1, x2)
    M = (math.log(abs(x1)) + math.cos(x2)) / 8.2
    print(M)
else:
    print('Дискриминант меньше 0')
