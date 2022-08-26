from weapon import Weapon
class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.weapons_list = [Weapon("Laser Beam", 25), Weapon("Giant Sword", 20), Weapon("Plasma Chain", 10)]
    def attack(self, dinosaur, choice):
        print(f'{self.name} uses {self.weapons_list[choice].name} to attack')
        dinosaur.health = (dinosaur.health - self.weapons_list[choice].attack_power)
        print(f"{self.name} hits for {self.weapons_list[choice].attack_power} damage. {dinosaur.name} is now at {dinosaur.health}")