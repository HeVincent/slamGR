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

    # Compute spectrogram using the short-time Fourier transform (STFT)
    short_Fourier_transform = librosa.stft(track, hop_length=STFT_interval, n_fft=STFT_window, window='hann')
    spectrogram = np.abs(short_Fourier_transform)

    # Plot spectrogram with a logarithmic frequency scale
    log_spectrogram = librosa.amplitude_to_db(spectrogram)
    plt.figure(figsize=(15,5), dpi=110)
    librosa.display.specshow(log_spectrogram, sr=sampling_rate, hop_length=STFT_interval)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.colorbar()
    plt.savefig('./graphics/twoClass/spect/'+trackName+"Spect.png")


