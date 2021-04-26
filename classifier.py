import sklearn
import pandas as pd
import csv
import numpy as np

genres = pd.read_csv('./raw/mini/Music_genres_mini.csv', sep=',', header=None).to_numpy()[:,0]

with open('./data/mini/miniTrack1.csv','r') as csv_file: # point at csv file

        csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

        track_data = next(csv_reader) # numerical track data
        track = np.genfromtxt(track_data,delimiter=',') # numpy array

tracks = track

# for i in np.linspace(1,len(genres)-1,len(genres)-2):
for i in range(1,3):
    i = str(int(i+1))
    print('track: '+i)

    with open('./data/mini/miniTrack'+i+'.csv','r') as csv_file: # point at csv file

        csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

        track_data = next(csv_reader) # numerical track data
        track = np.genfromtxt(track_data,delimiter=',') # numpy array

    tracks = np.vstack((tracks,track))

np.savetxt("./data/train/saved_numpy_data.csv", tracks, delimiter=",")

# with open('./data/train/miniTrainer.csv','w') as new_file:
#     print('miniTrainer.csv')

#     csv_writer = csv.writer(new_file,delimiter=',')

#     csv_writer.writerows(tracks)




