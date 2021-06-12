"""Задача 2. Логирование
Возможно, вы замечали, что некоторые программы не просто выдают ошибку и закрываются,
но и записывают эту ошибку в файл.
Таким образом проще сформировать отчёт об ошибках, а значит, программисту будет проще их исправить.
Это называется логированием ошибок.
Дан файл words.txt, в котором построчно записаны слова.
Необходимо определить количество слов, из которых можно получить палиндром (привет предыдущим модулям).
Если в строке встречается число, то программа выдаёт ошибку ValueError и записывает эту ошибку в файл errors.log"""

word_makes_palindrome = []

try:
    text_file = open("words.txt", "r", encoding="utf-8")
    text = text_file.read().split()
    count_string = 0
    for i_string in text:
        count_string += 1
        if not i_string.isalpha():
            raise ValueError
        may_palindrome = sum([1 for symbol in i_string if i_string.count(symbol) % 2 != 0])
        if may_palindrome <= 1:
            print(f"Из слова {i_string} можно составить палиндром")
            word_makes_palindrome.append(i_string)
except FileNotFoundError:
    print("Данного файла нет в директории")
except ValueError:
    errors_log_file = open("errors.log", "a", encoding="utf-8")
    errors_log_file.write(f"В строке {count_string} имеется число\n")
finally:
    errors_log_file.close()
    text_file.close()
    print("Программа завершила работу.")
    print(f"Количество возможных слов палиндромов: {len(word_makes_palindrome)}")
