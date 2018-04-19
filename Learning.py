import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
#Pandas DataFrame object created using the CSV file
df = pd.read_csv('trainingSet.csv')
print(df.head())
input("Press Enter to continue...")

#Open the trainingg key
data = open('TrainingKey.json')
keySet = json.load(data)

#Open the card data store
data2 = open('AllCards.json')
card2 = json.load(data2)

Sentence = list(df['Sentence'])

#Term Frequency - Inverse Document Frequency
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=3, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')

#Create Bag-of-Words using only the words appearing in Magic cards
allCards = []
for key in card2:
    if 'text' not in card2[key]:
        continue
    sent = (card2[key]['text'].splitlines())
    for sentence in sent:
        allCards.append(sentence)
tfidf.fit(allCards)

#Convert DataFrame to NumPy Array for use with SKLearn
sentences = df['Sentence'].values
sentences = tfidf.transform(sentences).toarray()
labels = df['Feature'].values
print(sentences)
print(labels)
input("Press Enter to continue...")

#Split the training set into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['Sentence'], df['Feature'], random_state = 0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = LinearSVC().fit(X_train_tfidf, y_train)

models = [
    KNeighborsClassifier(n_neighbors=5),
    LinearSVC(),
    MultinomialNB(),
    LogisticRegression(random_state=0),
    RandomForestClassifier()
]
CV = 25
cv_df = pd.DataFrame(index=range(CV * len(models)))
entries = []
for model in models:
    model_name = model.__class__.__name__
    accuracies = cross_val_score(model, sentences, labels, scoring='accuracy', cv=CV)
    for fold_idx, accuracy in enumerate(accuracies):
        entries.append((model_name, fold_idx, accuracy))
cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])

sns.boxplot(x='model_name', y='accuracy', data=cv_df)
sns.stripplot(x='model_name', y='accuracy', data=cv_df,
              size=12, jitter=True, edgecolor="gray", linewidth=2)
plt.show()
input("Press Enter to continue...")

print(cv_df.groupby('model_name').accuracy.mean())
input("Press Enter to continue...")

fig = plt.figure(figsize=(8, 6))
df.groupby('Feature').Sentence.count().plot.bar(ylim=0)
plt.show()
