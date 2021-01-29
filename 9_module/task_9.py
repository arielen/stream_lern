""" Задача 9. Коровы
Для коров есть 10 стойл.
В каждом стойле разные условия для животных, поэтому и молока они дают по-разному.
В первом стойле производят 2 литра в день, во втором 4, в третьем - 6, потом 8, 10, 12, 14, 16, 18, 20.
Но коровы стоят не во всех стойлах.
Свободные и занятые обозначаются строкой из букв a и b, где a - свободное стойло, b - занятое.

Пользователь вводит строку из 10 символов a и b.
Необходимо определить, сколько в итоге будет произведено молока за день. """

text = input('Введите строку: ')
stall = 1
milk = 0

for letter in text:
    if letter.lower() == 'a':
        milk += stall * 2
    elif letter.lower() == 'b':
        pass
    else:
        print(f'Символ неверный: {letter}')
        continue
    stall += 1

print(f'Всего молока: {milk}')