""" Задача 2. Шутник
На уроке информатики учитель дал задачу написать программу, где с двумя числами производятся разные арифметические операции.
Одноклассник Вани решил подшутить над ним и, пока тот не видит, специально наделал ошибок в его программе.
Дана программа, которая должна получать на вход от пользователя два числа, затем умножать первое число на три,
второе делить с остатком на восемь (нас будет интересовать именно остаток, а не целая часть)
и в конце выводить сумму получившихся результатов умножения и деления:
a = int('Введите первое число: ')
b = input('Введите второе число: ')
a *\ = 3
b %= 8
print('a'+'b')
Скопируйте её в редактор и исправьте все ошибки. Убедитесь, что программа работает верно. """

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
a *= 3
b %= 8
print('Сумма результатов: ' + str(a + b))