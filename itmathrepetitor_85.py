""" Пользователь вводит количество строк. Вывести на экран логотип соответствующего размера.
Если текст не помещается, то вывести логотип без текста. """

string = int(input('Введите колличество строк:  '))
if string >= 9:
    for text in range(0, string):
        if text == 0 or text == string - 1:
            print('[' * 15, ' ' * 5, ']' * 15)
        elif text == 1 or text == 2 or text == string - 2 or text == string - 3:
            print('[' + ':' * 14, ' ' * 5, ':' * 14 + ']')
        elif text == 3 or text == string - 4:
            print('[' + ':' * 6 + '[' * 7 + ':', ' ' * 5, ':' + ']' * 7 + ':' * 6 + ']')
        else:
            print('[' + ':' * 5 + '[' + 'Code the world'.center(23) + ']' + ':' * 5 + ']')
else:
    print('Code the world')