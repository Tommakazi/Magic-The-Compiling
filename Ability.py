from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
import numpy as np
import json


text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, random_state=42,
                                           max_iter=5, tol=None)),
])


class Ability(object):

    # The class "constructor" - It's actually an initializer
    def __init__(self):
        self.activate = ""
        self.type = ""
        self.modifier = []
        self.keywords = []

    def set_type(self, Card):
        name = Card.name
        colors = ['G', 'B', 'U', 'R', 'W']
        mtgEvergreenAbilities = ['Deathtouch', 'Defender', 'Double Strike', 'Enchant', 'Equip', 'First Strike', 'Flash',
                                 'Flying', 'Haste', 'Hexproof', 'Indestructible', 'Lifelink', 'Menace', 'Prowess',
                                 'Reach', 'Trample', 'Vigilance']
        ability = []

        with open("tokenData.json", 'w') as outfile:
            token = json.load(outfile)

            if 'Creature' or 'Planeswalker' or 'Enchantment' in Card['types']:
                ability.append("Summon Battlefield")

            if 'Land' in Card['types']:
                ability.append("Summon Land")

            if 'text' not in Card:
                return ability


            sentences = Card['text'].splitlines()

            for sentence in sentences:
                if sentence in mtgEvergreenAbilities:
                    ability.append(sentence)

                ability.append(text_clf.predict(sentence))










