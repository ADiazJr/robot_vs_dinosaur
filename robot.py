from weapon import Weapon
class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.laser_weapon = Weapon("Laser Beam", 25)
        self.sword_weapon = Weapon("Giant Sword", 20)
        self.plasma_weapon = Weapon("Plasma Chain", 10)
        self.weapons_list = [self.laser_weapon, self.sword_weapon, self.plasma_weapon]
    def attack(self, dinosaur, choice):
        print(f'Robot uses {self.weapons_list[choice].name} to attack')
        dinosaur.health = (dinosaur.health - self.weapons_list[choice].attack_power)
        print(f"Robot hits for {self.weapons_list[choice].attack_power} damage. Dinosaur is now at {dinosaur.health}")