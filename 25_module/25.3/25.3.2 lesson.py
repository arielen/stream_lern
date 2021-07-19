class Ship:

    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return f"\nМодель корабля: {self.__model}"

    def sail(self):
        print("\nКорабль куда-то поплыл")


class WarShip(Ship):

    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print(f"\nКорабль атакует с помощью оружия: {self.gun}")


class CargoShip(Ship):

    def __init__(self, model):
        super().__init__(model)
        self.tonnage_load = 0

    def load(self):
        print(f"\nЗагружаем корабль:")
        self.tonnage_load += 1
        print(f"Текущая загруженность: {self.tonnage_load}")

    def unload(self):
        print("\nРазгружаем корабль")
        if self.tonnage_load > 0:
            self.tonnage_load -= 1
        else:
            print("Корабль уже разгружен!")
        print(f"Текущая загруженность: {self.tonnage_load}")


warship = WarShip("zxc2", "Пушки")
warship.attack()
cargoShip = CargoShip("qwe3")
cargoShip.load()