import csv
import numpy as np
import librosa
import librosa.display
import scipy
import matplotlib.pyplot as plt

sampling_rate = 22050
trackNR = 1
trackName = 'tcTrack'+str(trackNR)

with open('./data/twoClass/'+trackName+'.csv','r') as csv_file: # point at csv file

    csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

    track_data = next(csv_reader) # numerical track data
    track = np.genfromtxt(track_data,delimiter=',') # numpy array

    # Parameters of the short-time Fourier transform
    STFT_window = 2048
    STFT_interval = 512

    MFCC = librosa.feature.mfcc(track, n_fft=STFT_window, hop_length=STFT_interval, n_mfcc=13)
    plt.figure(figsize=(15,5), dpi=110)
    librosa.display.specshow(MFCC, sr=sampling_rate, hop_length=STFT_interval)
    plt.xlabel('Time')
    plt.ylabel('MFCC')
    plt.colorbar()
    plt.savefig('./graphics/twoClass/mfcc/'+trackName+"mfcc.png")