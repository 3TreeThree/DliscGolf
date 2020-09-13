from Player import Player
from StatCard import StatCard
from Hole import Hole


def build_players():
    players = []
    default_stats = StatCard("player", 100, .80)
    for player_number in range(1, 4):
        players.append(Player("player " + str(player_number), default_stats))

    return players


def play(players, hole):
    for player in players:
        pass


def main():
    score_card = dict()
    players = build_players()
    for player in players:
        score_card[player] = 0
    hole1 = Hole(3, 500)
    


if __name__ == '__main__':
    main()
