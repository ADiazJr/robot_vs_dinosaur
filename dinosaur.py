class Dinosaur():
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 50

    def attack(self, robot):
        robot.health = (robot.health - self.attack_power)
        print(f"{self.name} hits for {self.attack_power} damage. {robot.name} is now at {robot.health}")