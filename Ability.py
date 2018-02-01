import json

class Ability(object):

    # The class "constructor" - It's actually an initializer
    def __init__(self):
        self.activate = ""
        self.type = ""
        self.modifier = []

    def set_type(self, Card):
        name = Card.name
        colors = ['G', 'B', 'U', 'R', 'W']

        with open("tokenData.json", 'w') as outfile:
            token = json.load("tokenData.json")

            for card in token[name]:
                if 'POS' in card:
                    if 'Power' in card:
                        if 'toughness' in card:
                            self.type = "pandt"
                        self.type = "power"
                        self.activate = "constant"

                if 'T' in card['NN']:
                    self.activate = "tap"
                    if 'Add' in card['VB']:
                        if card['NN'][1] in colors:
                            self.modifier = card['NN'][1]
                            self.type = "mana"
                if 'enters' in card['VBZ'][1]:
                    if 'battlefield' == card['NN'][1]:
                        self.activate = "enters"
                        if 'CD' not in card:
                            if 'draw' in card['VB']:
                                self.type = "draw"
                                self.modifier = "1"
                if 'Land' in Card.types:
                    self.activate = "tap"
                    self.modifier = Card.colors
                    self.type = "land"


