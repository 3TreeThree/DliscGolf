from dataclasses import dataclass
import random


@dataclass
class Hole:
    par = int
    max_length = int

    def __init__(self, par, max_length):
        self.par = par
        self.max_length = max_length

    def __str__(self):
        return 'Par: ' + str(self.par) + " Length: " + str(self.max_length)

    def __hash__(self):
        return hash((self.par, self.max_length))


def generate_hole():
    length = random.randint(260, 1300)
    # todo determine how foliage will work
    par = _determine_par(length)
    return Hole(par, length)


def _determine_par(length, foliage='light'):
    if foliage == 'light':
        return 3 if length < 700 else 4 if length < 1050 else 5
    else:
        return 3 if length < 535 else 4 if length < 975 else 5 if length < 1150 else 6
