from robot import Robot
from dinosaur import Dinosaur

class Battlefield():
    def __init__(self):
        self.robot = Robot("Robot")
        self.dinosaur = Dinosaur("Fakezilla", 20)
    
    def run_game(self):
        pass

    def display_welcome(self):
        pass

    def battle_phase(self):
        self.dinosaur.attack(self.robot)

    def display_winner(self):
        pass