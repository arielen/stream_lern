# Задача 2. Человек
# Реализуйте класс «Человек», который инициализируется именем (имя должно состоять только из букв)
# и возрастом (должен быть в диапазоне от 0 до 100),
# а внутри класса считается общее количество инициализированных объектов.
# Реализуйте сокрытие данных для всех атрибутов (как статических, так и динамических),
# а для изменения и получения данных объекта напишите специальные геттеры и сеттеры.
#
# При тестировании класса измените приватный атрибут (например, возраст) двумя способами:
# сеттером и «крайне не рекомендуемым», который был показан в уроке.

class Person:
    __count = 0

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Person.__count += 1

    def __str__(self):
        return f"Имя: {self.__name}\tВозраст: {self.__age}"

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception("Недопустимое имя!")

    def set_age(self, age):
        if age in range(0, 100):
            self.__age = age
        else:
            Exception("Недопустимый возраст!")


Jhon = Person("Jhon", 20)
print(Jhon)
Jhon.set_age(12)
print(Jhon)
Jhon.set_name("Василий")
print(Jhon)
