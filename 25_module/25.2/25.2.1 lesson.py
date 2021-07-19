class Person:
    __count = 0

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        Person.__count += 1

    def __str__(self):
        return f"Имя: {self.__name}\tВозраст: {self.__age}"

    def get_count(self):
        return self.__count

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception("Недопустимый возраст")


misha = Person("Misha", 20)
tom = Person("Tom", 22)
print(tom)
print(misha.get_count())
new_age = 80
misha.set_age(new_age)
print(misha.get_age())
