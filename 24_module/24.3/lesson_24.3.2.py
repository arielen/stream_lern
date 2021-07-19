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
