""" Задача 9. Успеваемость в классе
В классе N человек.
Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
Напишите программу, которая получает список оценок - N чисел -
и выводит на экран сообщение о том, кого сегодня больше: отличников, хорошистов или троечников. """

foo = (input('Введите оценки через пробел: ')).split(' ')
foo = [int(f) for f in foo]
trinity = 0
good = 0
perfect = 0

for student in foo:
    if student == 3:
        trinity += 1
    elif student == 4:
        good += 1
    elif student == 5:
        perfect += 1
    else:
        continue

print(f'Троечников: {trinity}', f'Хорошистов: {good}', f'Отличников: {perfect}', sep='\n')

if trinity > good and trinity > perfect:
    print(f'Сегодня больше троечников')
elif good > trinity and good > perfect:
    print('Сегодня больше хорошистов')
else:
    print('Сегодня больше отличников')

#  оказывается еще есть .count(находимый элемент). очень классная вещь)
# foo = list(map(int, (input('Введите оценки:')).split(' ')))
# print(f'3: {foo.count(3)}, 4: {foo.count(5)}, 5: {foo .count(4)}, ')
