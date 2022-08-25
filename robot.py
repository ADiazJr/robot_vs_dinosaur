from weapon import Weapon
class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Laser Beam", 25)
    
    def attack(self, dinosaur):
        dinosaur.health -= Weapon.attack_power