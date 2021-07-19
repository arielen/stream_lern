# Задача 2. Полёт
# Иногда для реализации дочерних классов используется так называемый класс-роль,
# где также описываются общие атрибуты и методы,
# но в программе инициализируются объекты только дочерних классов,
# а базовый класс-роль не трогается.
# К примеру, что общего у бабочки и ракеты?
# Они обе могут летать и приземляться.
#
# Реализуйте класс «Может летать».
# Атрибуты:
#     Высота = 0.
#     Скорость = 0.
# Методы:
#     Взлететь (в теле прописать pass).
#     Лететь (в теле прописать pass).
#     Приземлиться (установить высоту и скорость в значение 0).
#     Вывести высоту и скорость на экран.
# Затем реализуйте два дочерних класса:
#     «Бабочка», который может:
#         Взлететь (высота = 1).
#         Лететь (скорость = 0.5).
#     «Ракета», которая может:
#         Взлететь (высота = 500, скорость = 1000).
#         Приземлиться (высота = 0, взрыв).
#         Взорваться (тут уже что угодно).

class CanFly:

    def __init__(self, height=0, speed=0):
        self.__height = height
        self.__speed = speed

    def __str__(self):
        return f"Высота: {self.__height}\tСкорость: {self.__speed}"

    def get_height(self):
        return self.__height

    def get_speed(self):
        return self.__speed

    def take_off(self):
        pass

    def fly(self):
        pass

    def land(self):
        self.__height = 0
        self.__speed = 0


class Butterfly(CanFly):

    def __init__(self, height, speed):
        super().__init__(height, speed)

    def take_off(self):
        super().__init__(height=1)

    def fly(self):
        super().__init__(speed=0.5)


class Rocket(CanFly):

    def __init__(self, height=0, speed=0):
        super().__init__(height, speed)

    def take_off(self):
        super().__init__(height=500, speed=1000)

    def destroy(self):
        del self

    def land(self):
        super().land()
        print("Ракета приземлилась. Но взорвалась!")
        return self.__str__()

    def close(self):
        pass


racket = Rocket()
print(racket)
racket.take_off()
print(racket)
print(racket)
print(racket.land())
racket.destroy()
print(racket)
