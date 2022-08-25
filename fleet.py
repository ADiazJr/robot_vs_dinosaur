from robot import Robot
class Fleet():
    def __init__(self):
        self.robot_fleet = [Robot("Giant Tin Man"), Robot("Origins Robot"), Robot("Pacific Rim")]
        self.fleet_health = (self.robot_fleet[0].health + self.robot_fleet[1].health + self.robot_fleet[2].health)
        self.fleet_attack_power = (self.robot_fleet[0].weapons_list[0].attack_power + self.robot_fleet[1].weapons_list[1].attack_power + self.robot_fleet[2].weapons_list[2].attack_power)

    def attack(self, herd):
        print(f"{self.robot_fleet[0].name} attacks with {self.robot_fleet[0].weapons_list[0].name}, {self.robot_fleet[1].name} attacks with {self.robot_fleet[1].weapons_list[1].name}, {self.robot_fleet[2].name} attacks with {self.robot_fleet[2].weapons_list[2].name}")
        herd.herd_health = (herd.herd_health - self.fleet_attack_power)
        print(f'The herd is left with {herd.herd_health} health')