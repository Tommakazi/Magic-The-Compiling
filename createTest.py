import json
import random


mtgEvergreenAbilities = ['Deathtouch', 'Defender', 'Double Strike', 'Enchant', 'Equip', 'First Strike', 'Flash',
                         'Flying', 'Haste', 'Hexproof', 'Indestructible', 'Lifelink', 'Menace', 'Prowess',
                         'Reach', 'Trample', 'Vigilance']

training_set = []
set_names = []

data = open('tokenData.json')
tokens = json.load(data)

data2 = open('AllCards.json')
card = json.load(data2)

with open("sentences.txt", 'w') as outfile2:

    card_names = []
    for item in card:
        if 'text' not in card[item]:
                        continue
        card_names.append(card[item]['name'])

    for i in range(200):
        random_number = random.randint(0, 17000)
        current_card = card_names[random_number]
        sentences = card[current_card]['text'].splitlines()

        for sentence in sentences:
            if sentence in mtgEvergreenAbilities:
                continue
            outfile2.write(sentence + "\n")
            set_names.append(card[current_card]['name'])

