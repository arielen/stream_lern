""" Задача 5. Антошка, пора копать картошку
Антона отвезли на дачу и опять заставили копать картошку. А он даже рад, ему она очень нравится.
Правда, бабушка с дедушкой до его приезда уже вскопали N метров, поэтому он начнёт там, где закончили они.
Вся грядка занимает 100 метров и на ней помимо картошки растут другие культуры.
Но Антону нужна только картошка и больше ничего.
Антон знает, что она посажена каждые K метров.
То есть через каждые K метров он останавливается и выкапывает 3 клубня картошки
Напишите программу, которая посчитает сколько клубней картошки соберёт Антон. """

excavate = int(input('Введите колличество выкопанной картошки: '))
distance = int(input('Через сколько посажена картошка? '))
bed = 100
potates = 0

for meter in range(excavate + distance, bed + 1, distance):
    potates += 3

print(f'Антон собрал: {potates} картошек')