from Player import Player
from StatCard import StatCard
from Hole import Hole
import ScoreCard
import Course


def build_players():
    players = []
    default_stats = StatCard("player", 100, .80)
    for player_number in range(4):
        players.append(Player("player " + str(player_number), default_stats))

    return players


def main():
    players = build_players()
    course = Course.generate_course()
    score_card = ScoreCard.generate_score_card(players, course)
    print(score_card)

    print(course)


if __name__ == '__main__':
    main()
