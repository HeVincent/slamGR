import csv
import numpy as np
import librosa
import scipy

sampling_rate = 22050

with open('./data/twoClass/tcTrack1.csv','r') as csv_file: # point at csv file

    csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

    track_data = next(csv_reader) # numerical track data
    track = np.genfromtxt(track_data,delimiter=',') # numpy array

    # Parameters of the short-time Fourier transform
    STFT_window = 2048
    STFT_interval = 512

    # Example of time-domain features 
    track_tempo = librosa.beat.tempo(track, sr=sampling_rate)
    track_mean = np.mean(track)
    track_standard_deviation = np.std(track)
    track_skew = scipy.stats.skew(track)
    track_kurtosis = scipy.stats.kurtosis(track)

    