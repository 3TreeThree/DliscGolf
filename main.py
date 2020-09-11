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


@dataclass
class Player:
    name = str
    stat_card = StatCard

    def __init__(self, name, stat_card):
        self.name = name
        self.stat_card = stat_card


def main():
    player1 = Player("man", StatCard("man", 100, 100))
    print(player1.name)
    player2 = Player


if __name__ == '__main__':
    main()
