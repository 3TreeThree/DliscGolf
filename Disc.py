from dataclasses import dataclass


@dataclass
class Disc:
    speed = int     # rate at which the disc travels through the air | 1 - 14
    glide = int     # ability for the disc to maintain loft | 1 - 7
    turn = int      # tendency of disk to bank right at the beginning of a RHBH throw | 1 - -5
    fade = int      # tendency of disk to hook left at the end of a RHBH throw | 0 - 5

    def __init__(self, speed, glide, turn, fade):
        self.speed = speed
        self.glide = glide
        self.turn = turn
        self.fade = fade

    def __repr__(self):
        return "Disc: " + str(self.speed) + " " + str(self.glide) + " " + str(self.turn) + " " + str(self.fade)

    def __hash__(self):
        return hash((self.speed, self.glide, self.turn, self.fade))
