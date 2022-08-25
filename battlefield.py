from fleet import Fleet
from herd import Herd

class Battlefield():
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.death = False

    def run_game(self):
        self.display_welcome()
        while self.death is False:
            self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Hello today you will see a Fleet of robots fight a herd of dinosaurs")

    def battle_phase(self):
        if self.herd.herd_health >= 1:
            self.herd.attack(self.fleet)
        elif self.herd.herd_health <= 0:
            self.death = True
            return
        if self.fleet.fleet_health >= 1:
            self.fleet.attack(self.herd)
        elif self.fleet.fleet_health <= 0:
            self.death = True
            return

    def display_winner(self):
        if self.herd.herd_health >= 1:
            print("Herd Wins!")
        elif self.fleet.fleet_health >= 1:
            print("Fleet Wins!")