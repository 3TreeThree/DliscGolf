from dataclasses import dataclass


@dataclass
class StatCard:
    player = str
    power = int
    mental = float

    def __init__(self, player, power, mental):
        self.player = player
        self.power = power
        self.mental = mental

    def __repr__(self):
        return str(self.player) + "\npower: " + str(self.power) + "\nmental: " + str(round(self.mental, 4))

    def __hash__(self):
        return hash((self.player, self.power, self.mental))
