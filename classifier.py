import numpy as np
import sklearn
import csv
import pandas as pd
from sklearn import preprocessing
from sklearn import linear_model

# Define training and testing datasets
xTrain = np.load('./xTrain.npy')
xTest = np.load('./xTest.npy')

yTrain = pd.read_csv('./raw/mini/Music_genres_mini.csv', sep=',', header=None).to_numpy()[:400,0]
yTest = pd.read_csv('./raw/mini/Music_genres_mini.csv', sep=',', header=None).to_numpy()[400:,0]


# Standardize features by removing the mean and scaling to unit variance
scaler = preprocessing.StandardScaler(copy=False)
scaler.fit_transform(xTrain)
scaler.transform(xTest)

# Logistic regression model for music genre classification
classifier = linear_model.LogisticRegression(tol=1e-6, C=0.8, max_iter=200, random_state=0).fit(xTrain, yTrain)
y_hat = classifier.predict(xTest)
print('Baseline classifier accuracy: ' + str(round(100*np.mean(y_hat == yTest),2)) + ' %')