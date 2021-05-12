import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('iris-2.csv')

def wynik(y_test, predictions):
    print(metrics.confusion_matrix(y_test,predictions))
    print(metrics.classification_report(y_test, predictions))
    print(metrics.accuracy_score(y_test, predictions))
X = df[['sepal_length','sepal_width','petal_length','petal_width']]
y = df['species']


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state=42)

print('random forest')
rf_model = RandomForestClassifier(n_estimators =2, criterion='gini')
rf_model.fit(X_train, y_train)
predictions = rf_model.predict(X_test)
wynik(y_test, predictions)

print('multinomial bayes')
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
predictions = nb_model.predict(X_test)
wynik(y_test, predictions)


predictionrf = rf_model.predict([[5,4,2,0.1]])
predictionnb = nb_model.predict([[5,4,2,0.1]])
print(predictionrf)
print(predictionnb)
