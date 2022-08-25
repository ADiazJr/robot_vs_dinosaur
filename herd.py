from dinosaur import Dinosaur
class Herd():
    def __init__(self):
        self.herd_list = [Dinosaur("Stegosaurus", 10), Dinosaur("Triceratops", 5),Dinosaur("Raptor", 20)]
        self.herd_health = (self.herd_list[0].health + self.herd_list[1].health + self.herd_list[2].health )
        self.herd_attack_power = (self.herd_list[0].attack_power + self.herd_list[1].attack_power + self.herd_list[2].attack_power)

    def attack(self, fleet):
        print(f"The herd attack fleet for {self.herd_attack_power} damage")
        fleet.fleet_health = (fleet.fleet_health - self.herd_attack_power)
        print(f'The fleet is left with {fleet.fleet_health} health')