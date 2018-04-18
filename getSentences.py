import json

data = open('AllCards.json')
card = json.load(data)

data2 = open('Decks.json')
deck = json.load(data2)

mtgEvergreenAbilities = ['Deathtouch', 'Defender', 'Double Strike', 'Enchant', 'Equip', 'First Strike', 'Flash',
                                 'Flying', 'Haste', 'Hexproof', 'Indestructible', 'Lifelink', 'Menace', 'Prowess',
                                 'Reach', 'Trample', 'Vigilance']

names = []
for key in deck:
    for item in deck[key]:
        names.append(item)
print(names)
with open('sentences.txt', 'w') as outfile:
    for name in names:
        if 'text' not in card[name]:
            continue
        sentence = card[name]['text'].splitlines()

        for sent in sentence:
            outfile.write(sent + "\n")
