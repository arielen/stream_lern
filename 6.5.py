""" Задача 1. Надоедливый заказчик
Нашему заказчику нужно, чтобы фраза «Я — программист!» выводилась на экран столько раз, сколько он сам этого захочет.
Напишите программу, которая запрашивает число — количество строчек с фразой
«Я — программист!» — и столько же раз выводит на экран эту фразу.
Для решения задачи используйте переменную-счётчик, которая увеличивается на единицу до тех пор,
пока не будет введено нужное количество слов. """

text = 'Я — программист!'
line = int(input('Сколько строчек вывести? '))
count = 0

while count < line:
    print(text)
    count += 1

""" Задача 2. Напоминалка
У Евгения много работы, а ещё он очень забывчивый. 
Иногда он забывает о какой-нибудь важной встрече, и ему приходится выслушивать критику от начальства. 
Напишите для него программу-напоминалку. 
В самом начале программа спрашивает, сколько раз ему напомнить, а затем нужное количество раз выводит: 
«Вы хотели не забыть о чём-то». """

remind = int(input('Сколько раз вам напомнить ?  '))
count = 0

while count < remind:
    print('Вы хотели не забыть о чём-то')
    count += 1

""" Задача 3. Рыбалка
Наши прекрасные родственники удачно сходили на рыбалку. 
Настолько, что ходили мешком перетаскивать рыбу с берега в машину целых n раз. 
Каждый мешок они взвешивали на электронных весах (все мешки весили по-разному). 
Напишите программу для весов, которая считает суммарный вес мешков и выводит его на экран. """

dragged = int(input('Сколько мешков с рыбой?  '))
sum_weight = 0
count = 0

while count < dragged:
    bag_weight = int(input('Вес мешка: '))
    sum_weight += bag_weight
    count += 1
    print(f'Перенесено {count} мешков из {dragged}')
print(f'Суммарный вес мешков: {sum_weight} кг, количество мешков: {count}')

""" Задача 4. Любовь с первой цифры
Паша очень любит математику. 
Настолько сильно, что у него по всей комнате висят таблицы умножения, сложения, какие-то графики, формулы. 
И теперь он захотел распечатать таблицу степеней двойки, у них как раз началась новая тема по информатике.

Используя цикл while, выведите на экран для числа 2 его степени от 0 до 20. 
Напоминалка: возведение в степень в Python обозначается как **. """

number = 2
degree = 1

while degree <= 20:
    print(degree, number ** degree)
    degree += 1
