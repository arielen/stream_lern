import itertools
from string import digits, punctuation, ascii_letters


def brute_parol():
    try:
        password_lenght = input('Введите длину пароля (Например: 8 - 10): ')
        password_lenght = [int(item) for item in password_lenght.split('-')]
    except:
        print('Проверьте введенные данные!')

    try:
        choice = int(input('Если пароль содержит только цифры: 1\nЕсли пароль содержит только буквы: 2\nЕсли пароль содержит цифры и буквы: 3\nЕсли пароль содержит цифры, буквы и спецсимволов введите: 4')
        if choice == 1:
            possible_symbols = digits
        elif choice == 2:
            possible_symbols = ascii_letters
        elif choice == 3:
            possible_symbols = digits + ascii_letters
        elif choice == 4:
            possible_symbols = digits + ascii_letters + punctuation
        else:
            possible_symbols = 'Ошибка! Введите корректные данные'
    except:
        print('Ошибка! Введите корректные данные')

    file = open('parols.txt', 'w')

    for pass_lenght in range(password_lenght[0], password_lenght[1] + 1):
        for password in itertools.product(possible_symbols, repeat=pass_lenght):
            password = ''.join(password)
            file.write(password + '\n')

    file.close()

    print(f'База паролей сгенерирована! {pass_lenght:}')
