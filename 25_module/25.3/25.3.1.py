# Задача 1. Корабли
# Даны два класса кораблей — грузовой и военный.
# У каждого из этих кораблей есть своя модель, и каждый может сделать два действия: сообщить свою модель и идти по воде.
#
# Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю.
# У него есть ещё два действия: погрузить и выгрузить груз с корабля.
#
# У военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью.
# Также, вместо погрузки и выгрузки, у него есть другое действие — атаковать.
#
# Реализуйте классы грузового и военного кораблей.
# Для этого выделите общие атрибуты и методы в отдельный класс «Корабль» и используйте наследование.
# Не забудьте про функцию super в дочерних классах.

class Ship:

    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return f"\nМодель корабля: {self.__model}"

    def sail(self):
        print(f"\nКорабль {self.__model} куда-то плывет")


class WarShip(Ship):

    def __init__(self, model, gun):
        super().__init__(model)
        self.__gun = gun

    def attack(self):
        print(f"\nКорабль атакует с помощью оружия: {self.__gun}")


class CargoShip(Ship):

    def __init__(self, model):
        super().__init__(model)
        self.__tonnage_load = 0

    def load(self):
        print(f"\nЗагружаем корабль:")
        self.__tonnage_load += 1
        print(f"Текущая загруженность: {self.__tonnage_load}")

    def unload(self):
        print(f"\nРазгружаем корабль:")
        if self.__tonnage_load > 0:
            self.__tonnage_load -= 1
        else:
            print(f"Корабль уже разгружен!")
        print(f"Текущая загруженность: {self.__tonnage_load}")


warship = WarShip("zxc2", "Пушки")
warship.attack()
cargoShip = CargoShip("qwe3")
cargoShip.load()
