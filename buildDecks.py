import json
import Card
import Deck

names=open('Decks')
cardname=json.load(names)

green = Deck.Deck("greenDeck")
red = Deck.Deck("redDeck")

for key in cardname["greenDeck"]:
    for i in range(int(cardname["greenDeck"][key])):
        cardObj = Card.make_card(key,"Green")
        Deck.addcard(green, cardObj)

for key in cardname["redDeck"]:
    for j in range(int(cardname["redDeck"][key])):
        cardObj = Card.make_card(key,"Red")
        Deck.addcard(green, cardObj)


print(green)
print(red)


