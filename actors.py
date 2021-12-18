class Player():
    def __init__(self, name, strength, agility, speed):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.speed = speed


def register():
    p1 = Player(
                input("What strength do you have [0-10]? "),
                input("What agility do you have [0-10]? "),
                input("How fast are you [0-10]? "),
                input("What is your name? ")
    )
    print(p1.name, p1.agility, p1.strength, p1.speed)
