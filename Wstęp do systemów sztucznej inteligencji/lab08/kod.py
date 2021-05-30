import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.cluster import KMeans

df = pd.read_csv('iris-2.csv')


X = df[['sepal_length','sepal_width','petal_length','petal_width']]
y = df['species']


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state=42)


kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=100)
pred_y = kmeans.fit(X_train)
print(pred_y.cluster_centers_)


predictions = pred_y.predict(X_test)

y_test = list(y_test)
for i in range(len(y_test)):
    print(str(y_test[i]) + ' '+ str(predictions[i]))