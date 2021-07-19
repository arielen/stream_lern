class Potato:
    states = {0: "Росток", 1: "Зеленая", 2: "Зеленая", 3: "Зрелая"}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f"Картошка {self.index} сейчас {Potato.states[self.state]}")


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(i_index) for i_index in range(1, count + 1)]

    def grow_all(self):
        print("Картошка прорастает!")
        for i_potato in self.potatoes:
            i_potato.grow()
            i_potato.print_state()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print("Картошка еще не созрела!\n")
        else:
            print("Картошка созрела. Можно собирать!\n")
