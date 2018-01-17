import json

data=open('AllCards.json')
card=json.load(data)

names=open('Decks')
cardname=json.load(names)

print(cardname)
