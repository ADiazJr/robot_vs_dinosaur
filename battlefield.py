from fleet import Fleet
from herd import Herd
import random

class Battlefield():
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.dead_fleet = []
        self.dead_herd = []

    def run_game(self):
        self.display_welcome()
        while len(self.dead_fleet) <= 2 and len(self.dead_fleet) <= 2:
            self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Hello today you will see a Fleet of robots fight a herd of dinosaurs")

    def battle_phase(self):
        if len(self.herd.herd_list) >= 1 and len(self.fleet.robot_fleet) >= 1:
            for index_herd in range(len(self.herd.herd_list)):
                if self.herd.herd_list[index_herd].health >= 1:
                    self.herd.herd_list[index_herd].attack(self.fleet.robot_fleet[random.randrange(len(self.fleet.robot_fleet))])
                else:
                    self.dead_herd.append(self.herd.herd_list[index_herd])
        if len(self.fleet.robot_fleet) >= 1 and len(self.herd.herd_list) >= 1:    
            for index_fleet in range(len(self.fleet.robot_fleet)):
                if self.fleet.robot_fleet[index_fleet].health >= 1:
                    self.fleet.robot_fleet[index_fleet].attack(self.herd.herd_list[random.randrange(len(self.herd.herd_list))], index_fleet)
                else:
                    self.dead_fleet.append(self.fleet.robot_fleet[index_fleet])
    def display_winner(self):
        if len(self.herd.herd_list) >= 1:
            print("Herd Wins!")
        elif len(self.fleet.robot_fleet) >= 1:
            print("Fleet Wins!")