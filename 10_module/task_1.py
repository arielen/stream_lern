""" Задача 1. Тестовое задание
Степан пришёл устраиваться на работу, где ему дали тестовое задание: проанализировать такую таблицу,
понять, как она строится, и написать программу для вывода её на экран.

Помогите Степану реализовать такую программу.
Подсказка: номера столбцов. А ещё не забудьте про литерал \t для табуляции. """

for row in range(0, 5 + 1):
    for col in range(row, row + 11, 2):
        print(col, end='\t')
    print()
