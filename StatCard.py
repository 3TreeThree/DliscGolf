from dataclasses import dataclass


@dataclass
class StatCard:
    player = str
    power = int
    control = int

    def __init__(self, player, power, control):
        self.player = player
        self.power = power
        self.control = control

