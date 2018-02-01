

class Hand(list):

    def __init__(self, name):
        super().__init__()
        self.cards = []
        self.name = name

    def addcard(self, card):
        card.Location = "Hand"
        self.append(card)