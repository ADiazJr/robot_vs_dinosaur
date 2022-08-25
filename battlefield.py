from robot import Robot
from dinosaur import Dinosaur

class Battlefield():
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()
    
    def run_game(self):
        Battlefield.battle_phase()

    def display_welcome(self):
        pass

    def battle_phase(self):
        Dinosaur.attack(Robot())

    def display_winner(self):
        pass