import csv
import numpy as np
import librosa
import scipy

sampling_rate = 22050

class timeFeatures:
    def __init__(self):
        self.tempo = 0
        self.mean = 0
        self.std = 0
        self.skew = 0
        self.kurt = 0
        self.plp = 0

def getFeatures(path,fileName):

    features = timeFeatures()

    with open(path+fileName+'.csv','r') as csv_file: # point at csv file

        csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

        track_data = next(csv_reader) # numerical track data
        track = np.genfromtxt(track_data,delimiter=',') # numpy array

        # Example of time-domain features 
        features.tempo = librosa.beat.tempo(track, sr=sampling_rate)
        features.mean = np.mean(track)
        features.std = np.std(track)
        features.skew = scipy.stats.skew(track)
        features.kurt = scipy.stats.kurtosis(track)
        features.plp = librosa.beat.plp(track)

    return features

    