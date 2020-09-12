from dataclasses import dataclass
from StatCard import StatCard


@dataclass
class Player:
    name = str
    stat_card = StatCard

    def __init__(self, name, stat_card):
        self.name = name
        self.stat_card = stat_card

    def __str__(self):
        return str(self.name)

    def throw(self):
        return self.stat_card.power  # windspeed later
