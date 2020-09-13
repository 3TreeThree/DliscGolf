from dataclasses import dataclass


@dataclass
class Course:
    name: str
    holes: list

    def __init__(self, name):
        self.name = name


