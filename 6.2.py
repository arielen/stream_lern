""" Задача 1. Циклы — это сложно?
Даша начала проходить циклы. Она написала программу, которая просто должна считать сумму чисел до тех пор,
пока мы не ввели 0, но что-то пошло не так.
number = int(input(‘Введите число: ’))
While number <= 0:
 summ += number
 number = int(input(‘Введите число: ’))
print(Summ)
"""
number = int(input('Введите число: '))
summ = 0

while number != 0:
    summ += number
    print(summ)
    number = int(input('Введите число: '))

""" Задача 2. Введите пароль
Когда мы включаем ноутбук, он просит нас ввести пароль. 
Если пароль оказался неверным, нам сообщают об этом и снова просят ввести пароль. 
И так до тех пор, пока мы не введём правильный пароль, — тогда ноутбук даст доступ в учётную запись,
и программа завершится.
Напишите программу, которая запрашивает у пользователя пароль до тех пор, пока он не введёт верный 
(верным будет считаться пароль 235).

Пример:
Введите пароль: 100000
Неверный пароль!
Попробуйте ещё раз: 500
Неверный пароль!
Попробуйте ещё раз: 235
Пароль верный! Добро пожаловать. """

password = int(input('Введите пароль:  '))

while password != 235:
    print('Неверный пароль!')
    password = int(input('Попробуйте еще раз:  '))

print('Пароль верный! Добро пожаловать.')

""" Задача 3. Накопления
Кирилл копит себе на хорошую новенькую машину и для этого он каждый раз откладывает в копилку 
определённую сумму с зарплаты.
Напишите программу, которая спрашивает у пользователя 
«Сколько отложить денег?» до тех пор, пока сумма в копилке не превысит или не станет равна 500 000 рублей. """

money = 0

while summ < 500000:
    money = int(input('Сколько денег отложить ? '))
    summ += money

print('В копилке:', summ)

""" Задача 4. Шоппинг
Васе пришла зарплата, и он отправился в торговый центр за покупками. Он будет покупать всё подряд до тех пор, 
пока на карточке не останется менее 3 000 рублей — в этом случае ему придёт смс с предупреждением, 
и он закончит покупать.
Напишите программу, которая запрашивает у пользователя баланс карты и тратит её, каждый раз запрашивая цену товара. 
Когда денег остаётся мало, выводится сообщение: 
«Внимание: на карте осталось мало денег! Остановитесь!» и показывается баланс счёта. """

balance = int(input('Введите баланс карты:  '))

while balance >= 3000:
    buy = int(input('Введите стоимость товара:  '))
    balance -= buy

print('Внимание: на карте осталось мало денег! Остановитесь!', f'Баланс счета: {balance} рублей', sep='\n')

""" Задача 5. Закономерности
Арина считает, что всё в нашей жизни закономерно. И она в очередной раз убедилась в этом, 
когда узнала своё домашнее задание по математике.
Напишите программу, которая выводит на экран вот такую последовательность чисел (каждое число в новой строчке):

7 14 21 28 35 42 49 56 63 70 77 84 91 98 """

number = 7
number_all = 0

while number_all < 98:
    number_all += number
    print(number_all)


