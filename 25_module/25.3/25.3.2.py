# Задача 2. Роботы
# На военную базу завезли несколько интересных моделей роботов, которые похожи между собой,
# но имеют немного разные функции.
# У каждого робота есть номер модели и действие operate, которое означает, что делает робот.
# Особенности роботов следующие:
#
# У робота-пылесоса есть мешок для мусора, изначально он пустой (0).
# При команде operate робот сообщает, что он пылесосит пол, и выводит текущую заполняемость мешка.
# У военного робота есть оружие, и при команде operate он выводит
# сообщение о защите военного объекта с помощью этого оружия.
# Ещё есть робот — подводная лодка, который также является военным.
# У этого робота есть значение глубины, и при команде operate он делает то же,
# что и военный робот, плюс сообщает, что охрана ведётся под водой.
#
# Напишите программу, которая реализует все необходимые классы роботов.

class Robot:

    def __init__(self, model):
        self.__model = model


class CleanRobot(Robot):

    def __init__(self, model, bag=0):
        super().__init__(model)
        self.__bag = bag

    def operate(self):
        if self.__bag < 10:
            print(f"\nРобот пылесосит пол:")
            self.__bag += 1
            print(f"Текущий уровень мусора в мешке: {self.__bag}")
        else:
            print("\nУ робота закончилось место в мешке!")


class WarRobot(Robot):

    def __init__(self, model, gun):
        super().__init__(model)
        self.__gun = gun

    def operate(self):
        print(f"\nРобот защищает территорию с помощью: {self.__gun}")


class WatterRobot(Robot):

    def __init__(self, model, depth):
        super().__init__(model)
        self.__depth = depth

    def operate(self):
        print(f"\nРобот защищает территорию под водой, глубина: {self.__depth} метров")


watter_robot = WatterRobot("watter_robot", 25)
watter_robot.operate()
war_robot = WarRobot("war_robot", "UZI-25")
war_robot.operate()
clean_robot = CleanRobot("clean_robot", 3)
clean_robot.operate()
