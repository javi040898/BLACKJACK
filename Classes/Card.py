class Card:


    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    def description(self):
        return self.name + " of " + self.suit
