print('Задача 5. Текстовый редактор')


# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы 
# и любой цифры в тексте (а не только буквы Ы как раньше).
# 
# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
# 
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
# 
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
# 
# Количество цифр 0: 2
# Количество букв л: 1

def count_letters(text, number, word):
    K = 0  # количество соответствующих цифр
    N = 0  # количество соответствующих букв
    for letter in text:
        if letter == number:
            K += 1
        elif letter.lower() == word.lower():
            N += 1
    print(f'Количество цифр {number}: {K}', f'Количество букв: {word}: {N}', sep='\n')


text = input('Введите текст: ')
number = input('Какую цифру ищем? ')
word = input('Какую букву ищем? ')

count_letters(text, number, word)
