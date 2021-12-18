class Monster():
    def __init__(self, hp, attack, defense, speed, agility, fear_resist, fear):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.agility = agility
        self.fear_resist = fear_resist
        self.fear = fear


class Gargoyle(Monster):
    """def __init__(self, attack, defense, speed, agility, fear_resist, fear):
        super().__init__(attack, defense, speed, agility, fear_resist, fear)"""
    pass


def params():
    m1 = Gargoyle(10, 5, 6, 12, 120, 5, 1)

    print(f"Monster 1 has attributes {m1.hp} health, {m1.attack} "
          f"attack, {m1.defense} defense, {m1.speed} "
          f"speed, {m1.agility} agility, resists {m1.fear_resist} "
          f"fear, and is {m1.fear} scary. ")
