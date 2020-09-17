from dataclasses import dataclass
from StatCard import StatCard
import random
import string


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

    # return a number that represents the distance thrown
    def throw(self):
        return self.stat_card.power * self.stat_card.stability


def generate_player():
    alphabet = string.ascii_letters
    return Player(''.join((random.choices(alphabet, k=10))),
                  StatCard("player", random.randint(100, 250), random.uniform(.75, .90)))
