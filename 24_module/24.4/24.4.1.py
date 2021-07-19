# Задача 1. Машина 3
# Вам предстоит снова немного видоизменить класс Toyota из прошлого урока. На всякий случай вот описание класса.
# Четыре атрибута:
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Два метода:
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса (то есть передаваться в init).
# Реализуйте такое изменение класса.

class Toyota:
    def __init__(self, color, price, max_speed=200, current_speed=0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def car_info(self):
        print(f"Цвет машины: {self.color}\n"
              f"Цена: {self.price}\n"
              f"Максимальная скорость: {self.max_speed}\n"
              f"Текущая скорость: {self.current_speed}\n")

    def change_speed(self, speed):
        if speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = speed
        print(f"Текущая скорость автомобиля: {self.current_speed}\n")


SUPRA = Toyota("Black", 5000000, 380)
SUPRA.car_info()
SUPRA.change_speed(240)
SUPRA.car_info()
SUPRA.change_speed(800)
SUPRA.car_info()