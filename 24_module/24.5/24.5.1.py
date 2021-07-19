from garden import PotatoGarden

potato_garden1 = PotatoGarden(5)
potato_garden1.are_all_ripe()

for _ in range(3):
    potato_garden1.grow_all()
    potato_garden1.are_all_ripe()
