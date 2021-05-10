print('Задача 4. Урок информатики 3')


# Наконец-то учитель смог объяснить детям,
# что такое эта «плавающая точка». Однако долго его радость не продлилась, 
# ведь на следующем уроке нужно будет объяснить такие страшные слова, 
# как «экспоненциальное», «мантисса» и «порядок».

# Хоть старшеклассники и знакомы с экспонентой,
# учитель всё равно не уверен, что здесь всё будет понятно. 
# Поэтому для наглядности он также написал программу.

# На вход подаётся строка — это экспоненциальная форма числа.
# Напишите программу, 
# которая выводит отдельно мантиссу и отдельно порядок этого числа.

def expon_form(num):
    mantis = ''
    exponent = 0  # порядок
    for letter in str(num):
        if letter == 'e':
            break
        mantis += letter
    if int(num) > 10:
        while num > 10:
            num /= 10
            exponent += 1
    while num < 10:
        num *= 10
        exponent += 1
    print(f'Мантиса числа: {mantis}, Порядок: {exponent}')


number = float(input('Введите число в эксп. форме: '))

expon_form(number)