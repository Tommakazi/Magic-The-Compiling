from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import numpy as np
import json
import pandas as pd

clf = LinearSVC()
vec = TfidfVectorizer()

data2 = open('AllCards.json')
card2 = json.load(data2)

dataframe = pd.read_csv('trainingSet.csv')


cols = ['targetPow', 'targetLoc', 'targetAttr', 'targetCounter', 'targetCopy', 'targetControl', 'targetDestroy', 'targetExile', 'targetAttach',
        'targetDamage', 'targetTap', 'selfPow', 'selfLoc', 'selfAttr', 'selfCounter', 'selfTap', 'batPow', 'batAttr', 'batCounter', 'batOther', 'batLand',
        'playerLife', 'playerDiscard', 'playerMana', 'playerDraw', 'playerSac', 'playerRet', 'playerMill', 'playerScry']


allCards = []
for key in card2:
    if 'text' not in card2[key]:
        continue
    sent = (card2[key]['text'].splitlines())
    for sentence in sent:
        allCards.append(sentence)
print(allCards[0])
vec.fit(allCards)

temp = ""
X = []
x = dataframe[list(cols)].values
for ls in x:
    for item in ls:
        temp += str(item)
    X.append(temp)
    temp = ""
print(len(X))
y = dataframe['Sentence'].values
Y = vec.transform(y)
print(Y.shape)

clf.fit(Y, X)

df = pd.read_csv('testSet.csv')
test1 = df['Sentence'].values
test2 = vec.transform(test1)

predicted = clf.predict(test2.toarray())

data1 = open('TrainingKey.json')
keySet = json.load(data1)

positions = []
keys = []
allkeys = []
for value in predicted:
    positions.append([pos for pos, char in enumerate(value) if char == '1'])
for i in positions:
    for j in i:
        keys.append(keySet[str(j)])
    allkeys.append(keys)
    keys = []

print(list(zip(test1, allkeys)))
