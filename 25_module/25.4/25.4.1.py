# Задача 1. Юниты
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты).
# У Юнита есть действие «получить урон» (базовый класс получает 0 урона).
#
# Также есть два дочерних класса:
# Солдат: получает урон, равный переданному значению.
# Обычный гражданин: получает урон, равный двукратному переданному значению.
# Реализуйте родительский и дочерние классы и их методы,
# используя принцип полиморфизма (а также инкапсуляции и наследования, конечно же).

class Unit:

    def __init__(self, hp):
        self.__hp = hp

    def __str__(self):
        return f"У объекта: {self.__hp} hp."

    def take_damage(self, damage=0):
        self.__hp -= damage

    def get_hp(self):
        return self.__hp

    def set_hp(self, hp):
        if isinstance(hp, (int, float)):
            self.__hp = hp
        else:
            raise Exception("Неверный тип данных")


class Soldier(Unit):

    def __init__(self, hp, damage):
        super().__init__(hp)
        self.__damage = damage


class Civil(Unit):

    def __init__(self, hp, damage):
        super().__init__(hp)
        self.__damage = damage * 2


soldiers = Soldier(hp=100, damage=10)
print(soldiers)
soldiers.take_damage(50)
print(soldiers)