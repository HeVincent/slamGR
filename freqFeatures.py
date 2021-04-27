import csv
import numpy as np
import librosa
import scipy



class freqFeatures:
    def __init__(self):
        self.centroid = 0
        self.rolloff = 0
        self.band = 0
        self.zcr = 0
        self.mel = 0

def getFeatures(path,fileName):

    features = freqFeatures()

    sampling_rate = 22050
    # Parameters of the short-time Fourier transform
    STFT_window = 2048
    STFT_interval = 512

    with open(path+fileName+'.csv','r') as csv_file: # point at csv file

        csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

        track_data = next(csv_reader) # numerical track data
        track = np.genfromtxt(track_data,delimiter=',') # numpy array

        # Example of frequency-domain features 
        features.centroid = librosa.feature.spectral_centroid(track, sr=sampling_rate)
        features.rolloff = librosa.feature.spectral_rolloff(track, sr=sampling_rate)
        features.band = librosa.feature.spectral_bandwidth(track, sr=sampling_rate)
        features.zcr = librosa.feature.zero_crossing_rate(track, frame_length=STFT_window, hop_length=STFT_interval)
        features.mel = librosa.feature.mfcc(y=track, sr=sampling_rate, n_mfcc=20)

    return features