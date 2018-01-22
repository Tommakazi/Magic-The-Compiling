import random
import Card


class Deck(list):

    def __init__(self, name):
        super().__init__()
        self.cards = []
        self.name = name


    def addcard(self, card):
        card.Location = "Deck"
        self.append(card)


    def draw(self):
        card = self.pop()
        card.setLocation("Hand")
        return card


    def shuffle(self):
        random.shuffle(self)


    def removecard(self, card):
        card.setLocation("Graveyard")
        self.remove(card)


    def findcard(self, card):
        if card in self:
         return next(item for item in self if card == self.card)
        else:
            return "Card not Found."


