from dataclasses import dataclass
from StatCard import StatCard


@dataclass
class Player:
    name = str
    stat_card = StatCard
    total_distance = int

    def __init__(self, name, stat_card):
        self.name = name
        self.stat_card = stat_card

    def __str__(self):
        return str(self.name) + " "

    def __hash__(self):
        return hash((self.name, self.stat_card))

    def throw(self):
        return self.stat_card.power * self.stat_card.stability  # windspeed later
