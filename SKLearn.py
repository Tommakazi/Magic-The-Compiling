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


data=open('MachineSets.json')
card=json.load(data)

data2=open('AllCards.json')
card2=json.load(data2)

cardNames = []
catagories = []

for key in card['trainingSet']:
    cardName = key
    cardNames.append(cardName)
    catagories.append(card['trainingSet'][key])
print(catagories[0])


trainingSet = []
for name in cardNames:
    trainingSet.append(str(card2[name]))
print(trainingSet[0])

allCards = []
for key in card2:
    allCards.append(str(card2[key]))
print(allCards[0])

#text_clf.fit(allCards)
#document_trans = text_clf.transform(trainingSet)


text_clf.fit(trainingSet, catagories)

newcards = ["Fireball", "Cancel", "Silvercoat Lion", "Serra Angel", "Nissa's Chosen", "Stalwart Shield-Bearers"]
newdoc = []
for name in newcards:
    newdoc.append(str(card2[name]))

#newcards_trans = text_clf.transform(newdoc)

predicted = text_clf.predict(newdoc)
print(predicted)

