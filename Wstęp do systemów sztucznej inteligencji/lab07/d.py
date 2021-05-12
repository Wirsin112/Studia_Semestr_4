#from sklearn.datasets import load_iris
import pandas as pd
from keras.utils import to_categorical
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.svm import SVC
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow
from sklearn import metrics


def wynik(y_test, predictions):
    print(metrics.confusion_matrix(y_test,predictions))
    print(metrics.classification_report(y_test, predictions))
    print(metrics.accuracy_score(y_test, predictions))


tensorflow.compat.v1.logging.set_verbosity(tensorflow.compat .v1.logging.ERROR)
df = pd.read_csv('weather_madrid_LEMD_1997_2015.csv')
df["CET"] = pd.to_datetime(df["CET"])
df["y"] = [x.year for x in df["CET"]]
df["m"] = [x.month for x in df["CET"]]
df["d"] = [x.day for x in df["CET"]]

df[" Events"].fillna(value="sun", inplace=True)
df = df.fillna(df.mean())

del df["CET"]
y = df[" Events"]
del df[" Events"]
encoder = LabelEncoder()
y = encoder.fit_transform(y)
scaler = MinMaxScaler()
df = scaler.fit_transform(df)
xtrain, xtest, ytrain, ytest = train_test_split(df,y, test_size = 0.2,shuffle=False)


# xtrain = scaler.fit_transform(xtrain)
# xtest = scaler.transform(xtest)

print('random forest')
rf_model = RandomForestClassifier(n_estimators =7, criterion='gini')
rf_model.fit(xtrain, ytrain)
predictions = rf_model.score(xtest,ytest)
# wynik(ytest, predictions)
print(predictions)

print('multinomial bayes')
nb_model = MultinomialNB()
nb_model.fit(xtrain, ytrain)
predictions = nb_model.score(xtest,ytest)
print(predictions)

# wynik(ytest, predictions)

print('SVC')
model = SVC(kernel="linear",C=0.9)
model.fit(xtrain, ytrain)
predictions = model.score(xtest,ytest)
print(predictions)
predictions = model.predict(xtest)
wynik(ytest, predictions)