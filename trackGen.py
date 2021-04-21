import csv
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import soundfile as sf

with open('./raw/twoClass/Audio_data_two_class.csv','r') as csv_file: # point at csv file
    csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

    track_data = next(csv_reader) # numerical track data
    print(track_data)
    track = np.genfromtxt(track_data,delimiter=',') # numpy array

    sf.write('test.wav', track, 22050) # write to .wav

