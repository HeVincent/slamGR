import csv
import numpy as np
import librosa
import scipy

class features:
    def __init__(self, source, sr=22050):
        features.src = str(source) # path to parent
        features.sr = sr # sampling rate
        features.tempo = 'Undetermined'
        features.mean = 'Undetermined'
        features.stdev = 'Undetermined'
        features.skew = 'Undetermined'
        features.kurt = 'Undetermined'
        features.plp = 'Undetermined'
        
    def fullFeatures(self, track):

        with open(features.src,'r') as csv_file: # point at csv file
 
            csv_reader = csv.reader(csv_file, delimiter=',') #reader instance


            track_data = next(csv_reader) # numerical track data
            track = np.genfromtxt(track_data,delimiter=',') # numpy array
 
            # Example of time-domain features 
            features.tempo = librosa.beat.tempo(track, features.sr)
            features.mean = np.mean(track)
            features.std = np.std(track)
            features.skew = scipy.stats.skew(track)
            features.kurt = scipy.stats.kurtosis(track)
            features.plp = librosa.beat.plp(track)

    def tempo(self, track):
        features.tempo = librosa.beat.tempo(track, features.sr)

    def mean(self, track):
        features.mean = np.mean(track)

    def std(self, track):
        features.std = np.std(track)

    def skew(self, track):
        features.skew = scipy.stats.skew(track)
    
    def kurt(self, track):
        features.kurt = scipy.stats.kurtosis(track)

    def plp(self, track):
        features.plp = librosa.beat.plp(track)