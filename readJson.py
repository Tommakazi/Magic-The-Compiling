from pycorenlp import StanfordCoreNLP
import json

data=open('AllCards.json')
card=json.load(data)

cardNames = []
for key in card:
    cardName = card[key]['name']
    cardNames.append(cardName)




nlp = StanfordCoreNLP('http://localhost:9000')
nlpOutputs = []
pairs = []
finalOutputs = []
with open('depData.txt', 'w') as outfile:
    for name in cardNames:
        #print(name)
        if 'text' not in card[name]:
            continue
        output = nlp.annotate(card[name]['text'],
                           properties={
                               'annotators': 'depparse',
                               'outputFormat': 'json',
                           })
        for i in range(len(output['sentences'])):
            for j in range(len(output['sentences'][i]['basicDependencies'])):
                key = output['sentences'][i]['basicDependencies'][j]['dep']
                value = output['sentences'][i]['basicDependencies'][j]['dependentGloss']
                pair = {key: value}
                pairs.append(pair)

        nlpOutputs.append(output)
        pair2 = {name: pairs}
        pairs = []
        print(pair2)
        finalOutputs.append(pair2)
    json.dump(finalOutputs, outfile)




mtgEvergreenActions = ['Activate', 'Attach', 'Cast', 'Counter', 'Create', 'Destroy', 'Discard', 'Exchange', 'Exile', 'Fight', 'Play', 'Reveal', 'Sacrifice', 'Scry', 'Search', 'Shuffle', 'Tap', 'Untap']
mtgEvergreenAbilities = ['Deathtouch', 'Defender', 'Double Strike', 'Enchant', 'Equip', 'First Strike', 'Flash', 'Flying', 'Haste', 'Hexproof', 'Indestructible', 'Lifelink', 'Menace', 'Prowess', 'Reach', 'Trample', 'Vigilance']
mtgOtherActions = ['damage', 'gain', 'lose', 'target', 'graveyard', 'deck', 'library', 'hand', 'opponent', 'player', 'creature', 'spell', 'instant', 'sorcery', ]



