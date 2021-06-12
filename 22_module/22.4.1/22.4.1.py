"""Задача 1. Сумма чисел
Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке.
Напишите программу, которая выводит их сумму в выходной файл answer.txt.

Пример:
Содержимое файла numbers.txt:
1
2
3
4
10
Содержимое файла answer.txt
20"""

numbers_file = open("numbers.txt", "r")
numbers_list = [int(i_elem) for i_elem in numbers_file]
numbers_file.close()

answer_file = open("answer.txt", "w")
answer_file.write(str(sum(numbers_list)))
answer_file.close()
