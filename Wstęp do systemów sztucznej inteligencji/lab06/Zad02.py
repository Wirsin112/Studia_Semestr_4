#from sklearn.datasets import load_iris
import pandas as pd
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow
from sklearn import metrics

tensorflow.compat.v1.logging.set_verbosity(tensorflow.compat.v1.logging.ERROR)
df = pd.read_csv('weather_madrid_LEMD_1997_2015.csv')


df[" Events"].fillna(value="sun", inplace=True)
for i in df.columns:
    if df[i].isna().any():
        df[i].fillna(method="ffill", inplace=True)


df[" Max Gust SpeedKm/h"].fillna(value=df[" Max Gust SpeedKm/h"].mean(), inplace=True)
del df["CET"]
y = df[" Events"]
del df[" Events"]
encoder = LabelEncoder()
y = encoder.fit_transform(y)
y = pd.get_dummies(y).values
xtrain, xtest, ytrain, ytest = train_test_split(df,y, test_size = 0.2, random_state =24)
scaler = MinMaxScaler()

xtrain = scaler.fit_transform(xtrain)
xtest = scaler.transform(xtest)

model = Sequential()
model.add(Dense(64, input_dim = 21, activation ='tanh'))
model.add(Dense(32, activation ='tanh'))
model.add(Dense(16, activation ='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
model.fit(xtrain, ytrain, epochs = 30, verbose = 1)
predictions = model.predict(xtest)
ytest = ytest.argmax(axis=1)
predictions = predictions.argmax(axis=1)
print(metrics.confusion_matrix(ytest, predictions))
print(metrics.classification_report(ytest, predictions))
print(metrics.accuracy_score(ytest, predictions))
# print('acc',predictions)
