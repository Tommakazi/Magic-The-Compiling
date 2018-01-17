import json

class Card(object):
    layout = ""
    name = ""
    manaCost = ""
    cmc = ""
    colors = ""
    type = ""
    types = ""
    subtypes = ""
    text = ""
    power = 0
    toughness = 0
    colorIdentity = ""
    isTapped = False
    location = "Deck"

    # The class "constructor" - It's actually an initializer
    def __init__(self, layout, name, manaCost, cmc, colors, type, types, subtypes, text, power, toughness, colorIdentity, isTapped, location):
        self.layout = layout
        self.name = name
        self.manaCost = manaCost
        self.cmc = cmc
        self.colors = colors
        self.type = type
        self.types = types
        self.subtypes = subtypes
        self.text = text
        self.power = power
        self.toughness = toughness
        self.colorIdentity = colorIdentity
        self.isTapped = isTapped
        self.location = location

def make_card(cardname, deck):
    data = open('AllCards.json')
    cards = json.load(data)

    if 'layout' in cards[cardname]:
        layout = cards[cardname]['layout']
    else: layout = ''
    if 'name' in cards[cardname]:
        name = cards[cardname]['name']
    else: name = ''
    if 'manaCost' in cards[cardname]:
        manaCost = cards[cardname]['manaCost']
    else: manaCost = ''
    if 'cmc' in cards[cardname]:
        cmc = cards[cardname]['cmc']
    else: cmc = ''
    if 'colors' in cards[cardname]:
        colors = cards[cardname]['colors']
    else: colors = ''
    if 'type' in cards[cardname]:
        type = cards[cardname]['type']
    else: type = ''
    if 'types' in cards[cardname]:
        types = cards[cardname]['types']
    else: types = ''
    if 'subtypes' in cards[cardname]:
        subtypes = cards[cardname]['subtypes']
    else: subtypes = ''
    if 'text' in cards[cardname]:
        text = cards[cardname]['text']
    else: text = ''
    if 'power' in cards[cardname]:
        power = cards[cardname]['power']
    else: power = 0
    if 'toughness' in cards[cardname]:
        toughness = cards[cardname]['toughness']
    else: toughness = 0
    if 'colorIdentity' in cards[cardname]:
        colorIdentity = cards[cardname]['colorIdentity']
    else: colorIdentity = ''

    isTapped = False
    location = deck

    card = Card(layout, name, manaCost, cmc, colors, type, types, subtypes, text, power, toughness, colorIdentity, isTapped, location)

    return card


def setTap(Card, bool):
    if bool == 1:
        Card.isTapped = True
    else:
        Card.isTapped = False

def getTap(Card):
    return Card.isTapped


def setLocation(Card, str):
    Card.location = str

def getLocation(Card):
    return Card.location


def play_Hand(Card, Player):
    if Player.mana >= Card.manaCost:
        if Card.type != "Land":
            Card.location = "Battlefield"
        else:
            Card.location = "Land"

