from dataclasses import dataclass


@dataclass
class DiscBag:
    discs = list

    def __init__(self, discs):
        self.discs = discs

    def __repr__(self):
        return str('Disc bag: '.join(disc for disc in self.discs))
