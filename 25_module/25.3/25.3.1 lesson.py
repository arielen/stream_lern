class Pet:
    legs = 4
    has_tail = True

    def __str__(self):
        tail = "Да" if self.has_tail else "Нет"
        return f"Всего ног {self.legs}\nХвост присутствует - {tail}"


class Cat(Pet):

    def sounds(self):
        print("Мяу!")


class Dog(Pet):

    def sounds(self):
        print("Гав!")


class Frog(Pet):
    has_tail = False

    def sounds(self):
        print("Ква!")


cat = Cat()
dog = Dog()
frog = Frog()
print(frog)
frog.sounds()
print(cat)
print(dog)
cat.sounds()
dog.sounds()
