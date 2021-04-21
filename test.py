#import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
#import librosa
#import librosa.display
#import scipy
#import sklearn
#import os

# Set up plotting style
# matplotlib inline
sns.set(style='whitegrid', font_scale=1.2)

# read the top n rows of csv file as a dataframe
#df = pd.read_csv("./twoClass/Audio_data_two_class.csv", nrows=0)
#df.to_csv('./data/test.csv')

audio_data = np.genfromtxt('./twoClass/Audio_data_two_class.csv', delimiter=',')

print('done')

librosa.display.waveplot(audio_data[example_time_series_classical[i],:], sr=sampling_rate)