from Player import Player
from StatCard import StatCard
from Course import Course


def build_players():
    players = []
    default_stats = StatCard("player", 100, 100)
    for player_number in range(1, 20):
        players.append(Player("player " + str(player_number), default_stats))

    return players


def play(players, course):
    for player in players:
        pass


def main():
    players = build_players()
    course1 = Course(3, 500)



if __name__ == '__main__':
    main()
