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

    # Example of frequency-domain features 
    spectral_centroid = librosa.feature.spectral_centroid(track, sr=sampling_rate)
    spectral_rolloff = librosa.feature.spectral_rolloff(track, sr=sampling_rate)
    spectral_bandwidth = librosa.feature.spectral_bandwidth(track, sr=sampling_rate)
    zero_crossing_rate = librosa.feature.zero_crossing_rate(track, frame_length=STFT_window, hop_length=STFT_interval)
    mel_frequency_cepstral_coefficients = librosa.feature.mfcc(y=track, sr=sampling_rate, n_mfcc=20)

    