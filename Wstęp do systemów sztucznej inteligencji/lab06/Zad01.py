#from sklearn.datasets import load_iris
import pandas as pd
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn import metrics

df = pd.read_csv('iris-2.csv')

def wynik(y_test, predictions):
    print(metrics.confusion_matrix(y_test,predictions))
    print(metrics.classification_report(y_test, predictions))
    print(metrics.accuracy_score(y_test, predictions))
X = df[['sepal_length','sepal_width','petal_length','petal_width']]
z = df['species']

y=[]
for i in z:
    if i=='Setosa':
        k=0
    elif i=='Versicolor':
        k=1
    else:
        k=2
    y.append(k)

y = to_categorical(y)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.33, random_state =42)
skaler = MinMaxScaler()
skaler.fit(X_train)
X_train_scal = skaler.transform(X_train)
X_test_scal = skaler.transform(X_test)
model = Sequential()
model.add(Dense(8, input_dim = 4, activation ='tanh'))
model.add(Dense(3, activation ='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
model.fit(X_train_scal, y_train, epochs = 500, verbose = 1)
predictions = model.predict_classes(X_test_scal)

wynik(y_test.argmax(axis=1),predictions)
#model.save('pierwszy-model.h5')
x=[[2.5,3.2,1.0,2.3]]
x=skaler.transform(x)
pred=model.predict_classes(x)
print('przyklad: ' + str(pred))
