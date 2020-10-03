from dataclasses import dataclass
from StatCard import StatCard
import DiscBag
import random
import string


@dataclass
class Player:
    name = str
    stat_card = StatCard
    total_distance = int
    disc_bag = DiscBag

    def __init__(self, name, stat_card):
        self.name = name
        self.stat_card = stat_card

    def __repr__(self):
        return str(self.name) + " "

    def __hash__(self):
        return hash((self.name, self.stat_card))

    # return a number that represents the distance thrown
    def throw(self, disc):
        return self.stat_card.power * ((disc.speed // 14) + 1) * ((disc.glide // 7) + 1) * \
               ((disc.turn // 6) + 1) * ((disc.fade // 5) + 1)


def generate_player():
    alphabet = string.ascii_letters
    name = ''.join((random.choices(alphabet, k=7)))
    return Player(name, StatCard(name, random.randint(125, 130), random.uniform(0.95, 1.00)))
