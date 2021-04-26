import numpy as np
import sklearn
import csv

# Define training and testing datasets
with open('./data/train/miniTrain.csv','r') as csv_file: # point at csv file

        csv_reader = csv.reader(csv_file, delimiter=',') #reader instance
        print('a')
        X_train = np.genfromtxt(csv_file,delimiter=',') # numpy array

        print(X_train[0,0])

# X_test = audio_data[400:, :]
# y_train = audio_label[:400]
# y_test = audio_label[400:]

# Standardize features by removing the mean and scaling to unit variance
scaler = sklearn.preprocessing.StandardScaler(copy=False)
scaler.fit_transform(X_train)
scaler.transform(X_test)

# Logistic regression model for music genre classification
classifier = sklearn.linear_model.LogisticRegression(tol=1e-6, C=0.8, max_iter=200, random_state=0).fit(X_train, y_train)
y_hat = classifier.predict(X_test)
print('Baseline classifier accuracy: ' + str(round(100*np.mean(y_hat == y_test),2)) + ' %')