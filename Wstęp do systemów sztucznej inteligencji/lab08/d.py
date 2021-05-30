#from sklearn.datasets import load_iris
import pandas as pd
from keras.utils import to_categorical
from sklearn.cluster import KMeans
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
scaler = MinMaxScaler()
df = scaler.fit_transform(df)
xtrain, xtest, ytrain, ytest = train_test_split(df,y, test_size = 0.2,shuffle=False)

kmeans = KMeans(n_clusters=8, init='k-means++', max_iter=100)
pred_y = kmeans.fit(xtrain)
print(pred_y.cluster_centers_)


predictions = pred_y.predict(xtest)

y_test = list(ytest)
for i in range(len(y_test)):
    print(str(y_test[i]) + ' '+ str(predictions[i]))