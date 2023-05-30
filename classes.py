class Card:
    def __init__(self, name: str, value: int, lore: str = '', effect: list = None):
        if effect is None:
            effect = ['effect_num', 'effect_param']
        self.name = name
        self.value = value
        self.lore = lore
        self.effect = effect

        deck[self.name] = self.value

    def write_lore(self, lore: str):
        self.lore = lore


class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.hp = 100  # For a future project
        self.cards = []


# ANSI escape codes for text colors
# Redundant because I will use colorama package
class Colors:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    reset = '\033[0m'  # reset the color to default


# Needed to make the CARD_VALUES
deck = {}
