from dataclasses import dataclass
import Hole
import string
import random

@dataclass
class Course:
    name = str
    holes = list

    def __init__(self, name, holes):
        self.name = name
        self.holes = holes

    def __str__(self):
        return 'Course: ' + str(self.name) + \
               ''.join('\nHole ' + str(i+1) + ': ' + str(self.holes[i]) for i in range(18))


def generate_course():
    holes = []
    alphabet = string.ascii_letters

    for i in range(18):
        holes.append(Hole.generate_hole())
    return Course(''.join((random.choices(alphabet, k=10))), holes)


def main():
    print(generate_course())


if __name__ == "__main__":
    main()