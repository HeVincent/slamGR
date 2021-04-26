import pandas as pd
import bigDaddyData as bdd # self written
import sklearn
from sklearn import preprocessing as pp
import numpy as np

genres = pd.read_csv('./raw/mini/Music_genres_mini.csv', sep=',', header=None).to_numpy()[:,0]
yTrain = genres[0:400]
yTest =  genres[400:]

xTrain = bdd.csv2np('./data/mini/','miniTrack',1,400)
xTest = bdd.csv2np('./data/mini/','miniTrack',401,800)

# Standardize features by removing the mean and scaling to unit variance
scaler = pp.StandardScaler(copy=False)
scaler.fit_transform(xTrain)
scaler.transform(xTest)

# Logistic regression model for music genre classification
classifier = sklearn.linear_model.LogisticRegression(tol=1e-6, C=0.8, max_iter=200, random_state=0).fit(X_train, y_train)
y_hat = classifier.predict(xTest)
print('Baseline classifier accuracy: ' + str(round(100*np.mean(y_hat == yTest),2)) + ' %')