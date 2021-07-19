class Person:
    """
    Базовый класс, описывающий человека

    __count: общее количество человек

    Args:
        name (str): передается имя человека
        age (int): передается возраст человека

    Attributes:
        max_count (int): максимальное количество инстансов
    """
    __count = 0
    max_count = 5

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        self.__location = "Moscow"
        if Person.__count > self.max_count:
            raise Exception("Слишком много людей")
        Person.__count += 1

    def __str__(self):
        return f"Имя: {self.__name}\tВозраст: {self.__age}"

    def get_name(self):
        return self.__name

    def get_age(self):
        """
        Геттер для получения возраста

        :return: __age
        :rtype: int
        """
        return self.__age

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception("Недопустимое имя!")

    def set_age(self, age):
        """
        Сеттер для установления возраста

        :param age: возраст
        :type age: int
        :raise Exception: если возраст не в границах от 0 до 100, то вызывается исключение
        """
        if age in range(0, 100):
            self.__age = age
        else:
            Exception("Недопустимый возраст!")


class Student(Person):

    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.__university = university

    def __str__(self):
        info = super().__str__()
        info = "\n".join(
            (
                info,
                f"Студент учится в университете: {self.get_university()}"
            )
        )
        return info

    def get_university(self):
        return self.__university


class Employee(Person):
    """
    Класс Работник. Родитель: Person

    Args:
        name (str): передается имя человека
        age (int): передается возраст человека

    Attributes:
        max_count (int): максимальное количество инстансов
        job (str): должность работника
    """

    def __init__(self, name, age, company, salary):
        super().__init__(name, age)
        self.__company = company
        self.__salary = salary

    def __str__(self):
        info = super().__str__()
        info = "\n".join(
            (
                info,
                f"Компания: {self.get_company()}\tЗарплата: {self.get_salary()}"
            )
        )
        return info

    def get_company(self):
        return self.__company

    def get_salary(self):
        return self.__salary


my_student = Student(name="Tom", age=24, university="MGU")
print(my_student)
my_employee = Employee(name="Bob", age=25, salary=10000, company="Google")
print(my_employee)
