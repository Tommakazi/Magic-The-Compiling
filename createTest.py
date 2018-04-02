import json
import random



def Get_Random_Set:
    mtgEvergreenAbilities = ['Deathtouch', 'Defender', 'Double Strike', 'Enchant', 'Equip', 'First Strike', 'Flash',
                             'Flying', 'Haste', 'Hexproof', 'Indestructible', 'Lifelink', 'Menace', 'Prowess',
                             'Reach', 'Trample', 'Vigilance']

    training_set = []
    set_names = []

    with open("tokenData.json", 'w') as token:
        tokens = json.load(token)

    with open("AllCards.json", 'w') as outfile:
        card = json.load(outfile)

        cardnames = []
        for item in card:
            if 'text' not in card[item]:
                continue
            cardnames.append(item['name'])

        for i in range(400):
            random_card = random.choice(cardnames)

            sentences = card[random_card]['text'].splitlines()


            for sentence in sentences:
                if sentence in mtgEvergreenAbilities:
                    continue
                training_set.append(sentence)
                set_names.append(card[random_card]['name'])
