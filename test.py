#import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
#import librosa
#import librosa.display
#import scipy
#import sklearn
#import os

audio_data = np.genfromtxt('./twoClass/Audio_data_two_class.csv', delimiter=',', usecols = (1,2,3,4,5))

# read the top n rows of csv file as a dataframe
#df = pd.read_csv("./twoClass/Audio_data_two_class.csv", nrows=5, usecols = [0,1,2,3,4,5], low_memory = True, header=None)
#df = pd.read_csv("./twoClass/Music_genres_two_class.csv", nrows=10, low_memory=True, header=None)
#df.to_csv('./data/test.csv')
print(df.head())


#audio_data = np.genfromtxt('./twoClass/Audio_data_two_class.csv', delimiter=',')

print('done')

#librosa.display.waveplot(audio_data[example_time_series_classical[i],:], sr=sampling_rate)