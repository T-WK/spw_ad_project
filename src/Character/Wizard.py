from Player import Player
from Monster import Monster


class Wizard(Player):
    monster = Monster()

    def __init__(self):
        pass

    def heal(self, atk, mana):
        pass

    def fireball(self, atk, mana):
        pass

    def curse(self, monster):
        pass