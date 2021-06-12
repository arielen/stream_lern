nums_sum = 0
nums_count = 0

try:
    numbers_file = open("numbers.txt", "r")
    for i_line in numbers_file:
        nums_count += 1
        nums_sum += int(i_line)
    numbers_file.close()
    print(f"Среднее арифметическое: {nums_sum / nums_count}")
except FileNotFoundError:
    print("Такого файла не существует")
except ValueError:
    print("Нельзя преобразовать данные в целое число!")
