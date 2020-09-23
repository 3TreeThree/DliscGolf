import Player
import ScoreCard
import Course
import Disc


def main():
    players = [Player.generate_player(), Player.generate_player(), Player.generate_player(), Player.generate_player()]
    course = Course.generate_course()
    score_card = ScoreCard.generate_score_card(players, course)

    for player in players:
        print(player.stat_card)
        player.disc_bag = [Disc.Disc(10, 10, 10, 10)]
        print(player.disc_bag)
        print('\n')

    print(course)
    # the part where they play the game
    for hole in course.holes:
        for player in players:
            strokes = 0
            player.total_distance = 0
            while player.total_distance < hole.max_length and strokes < hole.par + 3:
                player.total_distance += player.throw()
                strokes += 1
            score_card.scores[(player, hole)] = strokes - hole.par
    # results
    print(score_card)


if __name__ == '__main__':
    main()
