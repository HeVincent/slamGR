import csv
import numpy as np
import soundfile as sf

with open('./data/train/miniTrainer.csv','r') as csv_file: # point at csv file

    csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

    track_data = next(csv_reader) # numerical track data
    track = np.genfromtxt(track_data,delimiter=',') # numpy array

    sf.write('./data/train/test.wav', track, 22050) # write to .wav