from dataclasses import dataclass
from Course import Course


@dataclass
class ScoreCard:
    players = list
    course = Course
    scores = dict()

    def __init__(self, players, course, scores):
        self.players = players
        self.course = course
        self.scores = scores

    def __str__(self):
        player_scores_string = ''
        for player in self.players:
            player_scores_string += str(player) + '\t'
            single_player_total = 0
            for hole in self.course.holes:
                player_scores_string += str(self.scores[(player, hole)]) + '\t'
                single_player_total += self.scores[(player, hole)]
            player_scores_string += str(single_player_total)
            player_scores_string += '\n'

        return 'Course: ' + str(self.course.name) + '\n' \
            '\t\t\t' + ''.join(str(i) + '\t' for i in range(1, 19)) + "Total" + '\n' \
            + player_scores_string


def generate_score_card(players, course):
    score_card = dict()
    for player in players:
        for hole in course.holes:
            score_card[(player, hole)] = 0
    return ScoreCard(players, course, score_card)