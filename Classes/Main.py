

from Classes.Player import *
from Classes.Deck import *
from Classes.Play import *
import random





p = Player("Javier","Martin",23)
d = Deck()
c = Card("Ace","Spades",1)

deck1 = d.deck
random.shuffle(deck1)

message = ""
i = 0
hand = []
while(message != "No"):
    message = input("Do you want a card?")

    if(message == "Yes"):
        hand.append(deck1[i])
    i += 1
    v = 0
    for j in hand:
        v += j.value

        print(j.description())
    print(v)




