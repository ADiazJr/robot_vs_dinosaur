from robot import Robot
from dinosaur import Dinosaur

class Battlefield():
    def __init__(self):
        self.robot = Robot("Robot")
        self.dinosaur = Dinosaur("Fakezilla", 20)
    
    def run_game(self):
        self.display_welcome()
        while (self.dinosaur.health >= 1) or (self.robot.health >= 1):
            self.battle_phase()
        self.display_winner

    def display_welcome(self):
        print("Hello today you will see a robot fight a dinosaur on Mustafar")

    def battle_phase(self):
        self.dinosaur.attack(self.robot)
        self.robot.attack(self.dinosaur)

    def display_winner(self):
        if self.dinosaur.health >= 1:
            print("Dinosaur Wins!")
        elif self.robot.health >= 1:
            print("Robot Wins!")