from dataclasses import dataclass


@dataclass
class Player:
    name = str

    def __init__(self, name, ):
        self.name = name


def main():
    player1 = Player("man")
    print(player1.name)


if __name__ == '__main__':
    main()
