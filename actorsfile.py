class Player:
    def __init__(self, hp, name, attack, defense, speed):
        self.hp = hp
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed


def assign_attributes():
    p1 = Player(
        100,
        input("What is your name? "),
        60,
        20,
        25
    )
    print(p1.hp, p1.name, p1.attack, p1.defense, p1.speed)
