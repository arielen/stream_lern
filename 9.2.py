""" Задача 1. Урок литературы
Выполните задание, разобранное в уроке.

К уроку литературы нужно было прочитать “Евгения Онегина”.
Учитель задаёт вопрос пяти случайным детям.
Она задаёт вопрос “Кто написал произведение?” и если ученик не угадывает,
то учитель ставит двойку и спрашивает следующего.
Если хоть кто-то угадает, то вопросы больше не задаются.
Напишите программу, которая посчитает количество двоечников из этих пяти. """

badScore = 0

for student in range(5):
    answer = input('Кто написал произведение?  ')
    if answer.lower() == 'пушкин':
        print('Верно!')
        break
    badScore += 1
    print('Неверно! Два!')

print(f'Колличество двоек: {badScore}')

""" Задача 2. Начальник
Напишите программу для робота-начальника. 
Он спрашивает у пользователя, выполнил ли он задание, которые выдавал вчера, 
и продолжает это делать до тех пор, пока тот не ответит ему “Да, конечно, сделал”. """

while True:
    answer = input('Выполнили задание?  ')
    if answer.lower() == 'да' or 'конечно' or 'сделал':
        print('Молодец')
        break

""" Задача 3. Дразнилка.
Напишите программу-дразнилку “Купи слона”. 
Она спрашивает у пользователя, как его зовут, затем отвечает “%username%, купи слона”. 
Дальше, что бы он ни говорил, она передразнивает: Все говорят “...”, а ты купи слона!
Пример:
Как тебя зовут? Дима
Дима, купи слона!
Хорошо, давай куплю
Все говорят Хорошо, давай куплю, а ты купи слона!
... """

name = input('Как вас зовут?  ')

while True:
    answer = input(f'{name}, купи слона')
    print(f'Все говорят {answer}, а ты купи слона!')