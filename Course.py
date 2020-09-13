from dataclasses import dataclass


@dataclass
class Course:
    name: str
    holes: int

    def __init__(self, name, holes):
        self.name = name
        self.holes = holes

