# Задача 2. Семья
# Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и «Наличие дома» и
# объекты которого могут выполнять следующие действия:
# Отобразить информацию о себе.
# Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»).
# Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
# Создайте как минимум один экземпляр класса и проверьте работу методов.
#
# Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):
#
# Family name: Common family
# Family funds: 100000
# Having a house: False
#
# Try to buy a house
# Not enough money!
#
# Earned 800000 money! Current value: 900000
# Try to buy a house again
# House purchased! Current money: 0.0
#
# Family name: Common family
# Family funds: 0.0
# Having a house: True

class Family:
    surname = "Common family"
    money = 100000
    have_a_house = False

    def info(self):
        print(
            f"Family name: {self.surname}\n"
            f"Family funds: {self.money}\n"
            f"Having a house: {self.have_a_house}\n"
        )

    def earn_money(self, amount):
        self.money += amount
        print(f"Earned {amount} money! Current value: {self.money}")

    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print(f"House purchased! Current money: {self.money}\n")
        else:
            print("Not enough money!\n")


my_family = Family()
my_family.info()

print("Try to buy a house")
my_family.buy_house(10 ** 6)

if not my_family.have_a_house:
    my_family.earn_money(800000)
    print("Try to buy a house again")
    my_family.buy_house(10 ** 6, 10)

my_family.info()
