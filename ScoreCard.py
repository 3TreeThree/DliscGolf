from dataclasses import dataclass
from Course import Course


@dataclass
class ScoreCard:
    players = list
    course = Course

    def __init__(self, players, course):
        self.players = players
        self.course = course


def generate_score_card(players, course):
    score_card = dict()
    for player in players:
        for hole in course.holes:
            score_card[(player, hole)] = 0
    return score_card
