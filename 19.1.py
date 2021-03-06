"""Задача 1. Словарь квадратов чисел
На вход программе поступает целое число num.
Напишите программу создания словаря, который включает в себя ключи от 1 до num,
а значениями соответствующего ключа будет значение ключа в квадрате.

Пример:
Введите целое число: 5
Результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}"""

num = int(input('Введите целое число: '))
result = dict()

for number in range(1, num + 1):
    result[number] = number ** 2

print(f'Результат: {result}')

"""Задача 2. Студент
Пользователь вводит фамилию, имя студента, город проживания, вуз, в котором он учится, и все его оценки. 
Всё вводится в одну строку через пробел. 
Напишите программу, которая по этой информации составит словарь и выведет его на экран.

Пример:
Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): Илья Иванов Москва МГУ 5 4 4 4 5
Результат: 
Имя - Илья
Фамилия - Иванов
Город - Москва
Место учёбы - МГУ
Оценки - [5, 4, 4, 4, 5]"""

student_str = input('Введите информацию о студенте, через пробел\n'
                    '(имя, фамилия, город, место учебы, оценки): ')

student_info = student_str.split()
student = dict()
student['Имя'] = student_info[0]
student['Фамилия'] = student_info[1]
student['Город'] = student_info[2]
student['Место учебы'] = student_info[3]
student['Оценки'] = []
for i_grade in student_info[4:]:
    student['Оценки'].append(int(i_grade))

for i_info in student:
    print(f'{i_info} - {student[i_info]}')

"""Задача 3. Контакты
Энтузиаст Степан, купив новый телефон, решил написать для него свою собственную операционную систему. 
И, конечно же, первое, что он захотел в ней реализовать, — это телефонная книга.
Напишите программу, которая запрашивает у пользователя имя контакта и номер телефона, 
добавляет их в словарь и выводит на экран текущий словарь контактов. 
Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы). 
Обеспечьте контроль ввода: если это имя уже есть в словаре, то выведите соответствующее сообщение.

Пример:
Текущие контакты на телефоне:
<Пусто>

Введите имя: Иван
Введите номер телефона: 100200300

Текущие контакты на телефоне:
Иван  100200300

Введите имя: Лена
Введите номер телефона: 8005555522

Текущие контакты на телефоне:
Иван  100200300
Лена  8005555522

Введите имя: Иван
Ошибка: такое имя уже существует.
..."""

phone_number = dict()
name = ''

while name != 'end':
    print(f'\nТекущие номера на телефоне: ')
    if len(phone_number) == 0:
        print('<Пусто>')
    for i_user in phone_number:
        print(f'{i_user} {phone_number[i_user]}')

    name = input('\nВведите имя: ')
    if name in phone_number:
        print('Ошибка, такое имя уже существует.')
    else:
        number = input('Введите номер телефона: ')
        phone_number[name] = number
