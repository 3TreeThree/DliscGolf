from dataclasses import dataclass
import Disc


@dataclass
class DiscBag:
    discs = list

    def __init__(self, discs):
        self.discs = discs

    def __repr__(self):
        return str('Disc bag: '.join(disc for disc in self.discs))


def generate_balanced_disc_bag():
    return [Disc.Disc(13, 5, 0, 4), ]
