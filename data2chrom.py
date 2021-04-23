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

    chroma = librosa.feature.chroma_cqt(y=track, sr=sampling_rate)
    plt.figure(figsize=(15,5), dpi=110)
    librosa.display.specshow(chroma, sr=sampling_rate, x_axis='time', y_axis='chroma')
    plt.title('Chromagram')
    plt.colorbar()
    plt.savefig('./graphics/twoClass/chrom/'+trackName+"chrom.png")