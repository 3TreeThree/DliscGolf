from Player import Player
from StatCard import StatCard
from random import randint, uniform
import ScoreCard
import Course


def build_players():
    players = []
    for player_number in range(4):
        players.append(Player("player " + str(player_number), StatCard("player", randint(100, 250), uniform(.75, .90))))

    return players


def main():
    players = build_players()
    course = Course.generate_course()
    score_card = ScoreCard.generate_score_card(players, course)

    print(score_card)
    for player in players:
        print(player.stat_card)
    print(course)
    for hole in course.holes:
        for player in players:
            strokes = 0
            player.total_distance = 0
            while player.total_distance < hole.max_length:
                player.total_distance += player.throw()
                strokes += 1
            score_card.scores[(player, hole)] = strokes
    print(score_card)

if __name__ == '__main__':
    main()
