from Player import Player
from StatCard import StatCard
from Hole import Hole
import ScoreCard
from Course import Course


def build_players():
    players = []
    default_stats = StatCard("player", 100, .80)
    for player_number in range(4):
        players.append(Player("player " + str(player_number), default_stats))

    return players


def play(players, hole):
    for player in players:
        pass


def main():

    players = build_players()
    course = Course("frig")
    score_card = ScoreCard.generate_score_card(players, course)
    for player in players:
        pass

    print(score_card)
    hole1 = Hole(3, 500)


if __name__ == '__main__':
    main()
