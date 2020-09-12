from dataclasses import dataclass


@dataclass
class Course:
    par = int
    max_length = int

    def __init__(self, par, max_length):
        self.par = par
        self.max_length = max_length
