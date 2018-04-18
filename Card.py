import json
import Ability

class Card(object):

    # The class "constructor" - It's actually an initializer
    def __init__(self):
        self.layout = ""
        self.name = ""
        self.manaCost = ""
        self.cmc = ""
        self.colors = ""
        self.type = ""
        self.types = ""
        self.subtypes = ""
        self.text = ""
        self.power = 1
        self.toughness = 1
        self.colorIdentity = ""
        self.isTapped = False
        self.location = ""
        self.abilities = []
        self.controller = ""
        self.attributes = []
        self.counters = []

    def make_card(cardname, deck):
        data = open('AllCards.json')
        cards = json.load(data)

        card = Card()

        if 'layout' in cards[cardname]:
            card.layout = cards[cardname]['layout']
        else: card.layout = ''
        if 'name' in cards[cardname]:
            card.name = cards[cardname]['name']
        else: card.name = ''
        if 'manaCost' in cards[cardname]:
            card.manaCost = cards[cardname]['manaCost']
        else: card.manaCost = ''
        if 'cmc' in cards[cardname]:
            card.cmc = cards[cardname]['cmc']
        else: card.cmc = ''
        if 'colors' in cards[cardname]:
            card.colors = cards[cardname]['colors']
        else: card.colors = ''
        if 'type' in cards[cardname]:
            card.type = cards[cardname]['type']
        else: card.type = ''
        if 'types' in cards[cardname]:
            card.types = cards[cardname]['types']
        else: card.types = ''
        if 'subtypes' in cards[cardname]:
            card.subtypes = cards[cardname]['subtypes']
        else: card.subtypes = ''
        if 'text' in cards[cardname]:
            card.text = cards[cardname]['text']
        else: card.text = ''
        if 'power' in cards[cardname]:
            card.power = cards[cardname]['power']
        else: card.power = 0
        if 'toughness' in cards[cardname]:
            card.toughness = cards[cardname]['toughness']
        else: card.toughness = 0
        if 'colorIdentity' in cards[cardname]:
            card.colorIdentity = cards[cardname]['colorIdentity']
        else: card.colorIdentity = ''

        card.isTapped = False
        card.location = deck



        return card


    def setTap(Card, bool):
        if bool == 1:
            Card.isTapped = True
        else:
            Card.isTapped = False

    def getTap(Card):
        return Card.isTapped


    def play_Hand(Card, Player):
        if Player.mana >= Card.manaCost:
            if Card.type != "Land":
                Card.location = "Battlefield"
            else:
                Card.location = "Land"

