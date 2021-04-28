# Store frequency features
import csv
import numpy as np
import librosa
import scipy
import matplotlib.pyplot as plt
import librosa.display

# STFT_window = 1949
# STFT_interval = 512
# sampling_rate = 22050

def spect(sourcePath,sourceName,targetPath,targetName,STFT_window,STFT_interval,sampling_rate):

    with open(sourcePath+sourceName+'.csv','r') as csv_file: # point at csv file

        csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

        track_data = next(csv_reader) # numerical track data
        track = np.genfromtxt(track_data,delimiter=',') # numpy array

        # Parameters of the short-time Fourier transform

        windowShape = 'hann' # rect, hann, hamming, bartlett

        # Compute spectrogram using the short-time Fourier transform (STFT)
        short_Fourier_transform = librosa.stft(track, hop_length=STFT_interval, n_fft=STFT_window, window=windowShape)
        spectrogram = np.abs(short_Fourier_transform)

        # Plot spectrogram with a logarithmic frequency scale
        log_spectrogram = librosa.amplitude_to_db(spectrogram)
        plt.figure(figsize=(15,5), dpi=110)
        librosa.display.specshow(log_spectrogram, sr=sampling_rate, hop_length=STFT_interval)
        plt.xlabel('Time')
        plt.ylabel('Frequency')
        plt.colorbar()
        plt.savefig(targetPath+targetName+'.png')
    return


def psd(sourcePath,sourceName,targetPath,targetName):

    with open(sourcePath+sourceName+'.csv','r') as csv_file: # point at csv file

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
    plt.savefig(targetPath+targetName+'.png')
    return

def chrom(sourcePath,sourceName,targetPath,targetName):
    
    with open(sourcePath+sourceName+'.csv','r') as csv_file: # point at csv file

        csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

        track_data = next(csv_reader) # numerical track data
        track = np.genfromtxt(track_data,delimiter=',') # numpy array

    chroma = librosa.feature.chroma_cqt(y=track, sr=sampling_rate)
    plt.figure(figsize=(15,5), dpi=110)
    librosa.display.specshow(chroma, sr=sampling_rate, x_axis='time', y_axis='chroma')
    plt.title('Chromagram')
    plt.colorbar()
    plt.savefig(targetPath,targetName+'.png')
    return

def mfcc(sourcePath,sourceName,targetPath,targetName):
    with open(sourcePath+sourceName+'.csv','r') as csv_file: # point at csv file

        csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

        track_data = next(csv_reader) # numerical track data
        track = np.genfromtxt(track_data,delimiter=',') # numpy array

    MFCC = librosa.feature.mfcc(track, n_fft=STFT_window, hop_length=STFT_interval, n_mfcc=13)
    plt.figure(figsize=(15,5), dpi=110)
    librosa.display.specshow(MFCC, sr=sampling_rate, hop_length=STFT_interval)
    plt.xlabel('Time')
    plt.ylabel('MFCC')
    plt.colorbar()
    plt.savefig(targetPath+targetName+'mfcc.png')
    return