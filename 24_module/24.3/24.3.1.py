# Задача 1. Машина 2
# Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
#
# Добавьте два метода класса:
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Проверьте работу этих методов.
import random


class Toyota:
    color = "red"
    price = 1000000
    max_speed = 200
    current_speed = 0

    def print_info(self):
        print(f"Car: \n"
              f"Color: {self.color}\n"
              f"Price: {self.price}\n"
              f"Max Speed: {self.max_speed}\n"
              f"Current Speed: {self.current_speed}\n")

    def new_speed(self, speed):
        self.current_speed += speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed


tundra = Toyota()
celica = Toyota()
supra = Toyota()

tundra.print_info()
celica.print_info()
supra.print_info()

tundra.new_speed(random.randint(0, 250))
celica.new_speed(random.randint(0, 250))
supra.new_speed(random.randint(0, 250))

tundra.print_info()
celica.print_info()
supra.print_info()
