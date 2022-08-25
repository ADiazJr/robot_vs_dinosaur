from robot import Robot
from dinosaur import Dinosaur

class Battlefield():
    def __init__(self):
        self.robot = Robot("Robot")
        self.dinosaur = Dinosaur("Fakezilla", 20)
    
    def run_game(self):
        self.display_welcome()
        self.death = False
        while self.death is False:
            self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Hello today you will see a robot fight a dinosaur on Mustafar")

    def battle_phase(self):
        if self.dinosaur.health >= 1:
            self.dinosaur.attack(self.robot)
        elif self.dinosaur.health <= 0:
            self.death = True
            return self.death
        if self.robot.health >= 1:
            self.robot.attack(self.dinosaur)
        elif self.robot.health <= 0:
            self.death = True
            return self.death

    def display_winner(self):
        if self.dinosaur.health >= 1:
            print("Dinosaur Wins!")
        elif self.robot.health >= 1:
            print("Robot Wins!")