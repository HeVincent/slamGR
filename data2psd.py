import csv
import numpy as np
import librosa
import scipy
import matplotlib.pyplot as plt

sampling_rate = 22050
trackNR = 1
trackName = 'tcTrack'+str(trackNR)

with open('./data/twoClass/'+trackName+'.csv','r') as csv_file: # point at csv file

    csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

    track_data = next(csv_reader) # numerical track data
    track = np.genfromtxt(track_data,delimiter=',') # numpy array

    # Compute the discrete Fourier transform (DFT) using the fast Fourier transform (FFT) algorithm
    fast_Fourier_transform = np.fft.fft(track)

    # Plot the power spectrum
    magnitude = np.abs(fast_Fourier_transform)
    power_spectrum = magnitude**2
    frequency = np.fft.fftfreq(n=track.size, d=1/sampling_rate)
    fig = plt.figure(figsize=(10,5), dpi=110)
    plt.plot(frequency, power_spectrum)
    plt.xlabel('Frequency')
    plt.ylabel('Power')
    plt.show()
    plt.savefig('./graphics/twoClass/psd/'+trackName+"PSD.png")

