"""Задача 1. Член семьи
Дана структура, которая содержит описание одного из членов семьи (имя, фамилия, хобби, сколько лет и дети):

family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

Напишите программу, которая реализует такую структуру: имя, фамилия, хобби, количество лет и дети.
Затем с помощью метода get и установки значения по умолчанию проверьте, есть ли ребёнок с именем Bob.
Затем так же проверьте ребёнка с именем Rob. Если такого ребёнка нет, то получите значение Noname."""


def family_member():
    member = {}
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    hobbies = input('Перечислите хобби через запятую: ').split(',')
    age = int(input('Введите возраст: '))
    member['name'], member['surname'], member['hobbies'], member[
        'age'] = name, surname, hobbies, age
    member['children'] = list()
    while True:
        children = input('Введите "да", если есть и "нет", если их нет')
        if children.lower() == 'да':
            name_child = input('Имя ребенка: ')
            age_child = input('Сколько лет ребенку: ')
            member['children'].append(
                {
                    'name': name_child,
                    'age': age_child
                }
            )
        elif children.lower() == 'нет':
            break
    return member


family = family_member()
name_child_find = ['Bob', 'Rob']

for i_name in name_child_find:
    if family.get('children', {}).get(i_name, {}):
        print(f'{i_name}, найден!')
    else:
        print('Noname')

"""Задача 2. Игроки
Есть готовый словарь игроков, у каждого игрока есть имя, команда, в которой он играет, 
а также его текущий статус, в котором указано, отдыхает он, тренируется или путешествует:

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

Напишите программу, которая выводит на экран вот такие данные в разных строчках:
Все члены команды из команды А, которые отдыхают.
Все члены команды из группы B, которые тренируются.
Все члены команды из команды C, которые путешествуют."""

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

print('Все члены команды из команды А, которые отдыхают.')
for player in players_dict.values():
    if player['team'] == 'A' and player['status'] == 'Rest':
        print(player['name'])

print('\nВсе члены команды из группы B, которые тренируются.')
for player in players_dict.values():
    if player['team'] == 'B' and player['status'] == 'Training':
        print(player['name'])

print('\nВсе члены команды из команды C, которые путешествуют.')
for player in players_dict.values():
    if player['team'] == 'C' and player['status'] == 'Travel':
        print(player['name'])
