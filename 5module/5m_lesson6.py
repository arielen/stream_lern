""" Задача 6. Свободная касса!

Паша открыл несколько продуктовых магазинов, но никак не может понять, сколько ему нужно нанять продавцов,
чтобы люди не толпились в очередях на кассе и самим продавцам было комфортно.

Напишите программу по следующей инструкции: программа запрашивает количество клиентов,
количество продавцов и зарплату одного продавца.

Если один продавец обслуживает более четырёх покупателей, то:
    вывести сообщение: «Слишком мало продавцов»;
    если зарплата меньше 20 000, то повысить её на 2 000 рублей.
Иначе вывести сообщение: «Продавцов достаточно».
В конце вывести текущую зарплату продавцов. """

clients = int(input('Введите колличество клиентов:  '))
sellers = int(input('Введите колличество продавцов:  '))
salary = int(input('Введите зарплату одного продовца:  '))

if clients / sellers >= 4:
    print('Слишком мало продавцов')
    if salary < 20000:
        salary += 2000
else:
    print('Продавцов достаточно')


print(f'Зарплата продавцов составляет: {salary} рублей.')
