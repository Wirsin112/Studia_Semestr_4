import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn import metrics


def wynik(y_test, predictions):
    print(metrics.confusion_matrix(y_test, predictions))
    print(metrics.classification_report(y_test, predictions))
    print(metrics.accuracy_score(y_test, predictions))


df = pd.read_csv('train-amazon.tsv', sep='\t')
X = df['review']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=16)
text_clf = Pipeline([('tfidf', TfidfVectorizer(ngram_range=(1, 2))), ('clf', LinearSVC())])
text_clf.fit(X_train, y_train)
predictions = text_clf.predict(X_test)
wynik(y_test, predictions)
