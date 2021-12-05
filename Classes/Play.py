class Hand:

    def __init__(self,hand,player):
        self.hand = hand
        self.player = player

    def sum(self,hand,i):
        return hand[i].value