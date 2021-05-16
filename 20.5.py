"""Задача 1. Паспортные данные
В базе данных поликлиники хранятся паспортные данные людей.
Хранение реализовано с помощью словаря, состоящего из пар «Серия и номер паспорта — фамилия и имя».
Серия и номер — составной ключ, а фамилия и имя — составное значение.

data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

Реализуйте функцию, которая по номеру и серии паспорта выдаёт имя и фамилию человека."""


def show_person():
    passport = (int(input('Номер паспорта: ')), int(input('Серия паспорта: ')))
    for i_series, i_person in data.items():
        if passport == i_series:
            return print(f'Человек с такими данными: {i_person[0]} {i_person[1]}')
    return print('Такого человека в базе нет! Проверьте введенные данные')


data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

show_person()

"""Задача 2. Контакты 2
Мы уже реализовывали телефонную книгу для Степана, однако её проблема была в том,
что туда нельзя было добавить людей с одинаковыми именами. Надо это исправить.
Напишите программу, которая запрашивает у пользователя имя контакта, фамилию и номер телефона,
добавляет их в словарь и выводит на экран текущий словарь контактов.
Словарь состоит из пар «Ф. И. — телефон», где Ф. И. — это составной ключ.
Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы).
Обеспечьте контроль ввода: если этот человек уже есть в словаре, то выведите соответствующее сообщение."""


def add_contact():
    person = (input('\nВведите фамилию: '), input('Введите имя: '))
    if person not in phone_numbers:
        mob_numbers = int(input('Введите номер контакта: '))
        phone_numbers.update({person: mob_numbers})
    else:
        print(f'Такой контакт уже есть в телефоне')


phone_numbers = dict()

while True:
    print(f'\nТекущие номера на телефоне: ')
    if len(phone_numbers) == 0:
        print('<Пусто>')
    for i_user, i_number in phone_numbers.items():
        print(f'{i_user[0]} {i_user[1]}: {i_number}')
    choice = input('\nДобавить контакт: (да, нет): ').lower()
    if choice != 'нет':
        add_contact()
    else:
        print(f'\nВаша записная книга:')
        [print(f'{i_user[0]} {i_user[1]}: {i_number}') for i_user, i_number in phone_numbers.items()]
        break