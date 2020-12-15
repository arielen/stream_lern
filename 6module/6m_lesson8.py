""" Задача 8. Продолжаем бегать
В первый день спортсмен пробежал X километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
По данному числу X определите номер дня, на который пробег спортсмена составит не менее Y километров. """

distance = int(input('Сколько пробежал спортсмен в первый день? '))
day = int(input('Введите день: '))
procent = 0.1
count = 0
sum_distance = 0

while count < day:
    count += 1
    sum_distance += distance
    print(count, distance, sum_distance)
    distance += distance * procent

# TODO - не совсем понятна суть задания
