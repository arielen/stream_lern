# Задача 1. Машина
# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.
import random


class Toyota:
    color = "red"
    price = 1000000
    max_speed = 200
    current_speed = 0


tundra = Toyota()
celica = Toyota()
supra = Toyota()
tundra.current_speed = random.randint(0, 200)
celica.current_speed = random.randint(0, 200)
supra.current_speed = random.randint(0, 200)

print(tundra.current_speed, celica.current_speed, supra.current_speed)
