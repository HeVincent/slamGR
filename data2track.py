import csv
import numpy as np
import soundfile as sf

with open('./data/mini/miniTrack5.csv','r') as csv_file: # point at csv file

    csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

    track_data = next(csv_reader) # numerical track data
    track = np.genfromtxt(track_data,delimiter=',') # numpy array

    sf.write('./tracks/mini/mini5.wav', track, 22050) # write to .wav