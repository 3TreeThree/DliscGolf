from dataclasses import dataclass


@dataclass
class StatCard:
    player = str
    power = int
    stability = float

    def __init__(self, player, power, stability):
        self.player = player
        self.power = power
        self.stability = stability

    def __repr__(self):
        return str(self.player) + "\npower: " + str(self.power) + "\nstability: " + str(round(self.stability, 4))

    def __hash__(self):
        return hash((self.player, self.power, self.stability))
