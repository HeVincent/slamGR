import sklearn
import pandas as pd
import csv
import numpy as np

start = 401
end = 800

genres = pd.read_csv('./raw/mini/Music_genres_mini.csv', sep=',', header=None).to_numpy()[:,0]

with open('./data/mini/miniTrack'+str(start)+'.csv','r') as csv_file: # point at csv file
    print('track: '+str(start))

    csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

    track_data = next(csv_reader) # numerical track data
    track = np.genfromtxt(track_data,delimiter=',') # numpy array

tracks = track

for i in range(start,end):
    i = str(int(i+1))
    print('track: '+i)

    with open('./data/mini/miniTrack'+i+'.csv','r') as csv_file: # point at csv file

        csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

        track_data = next(csv_reader) # numerical track data
        track = np.genfromtxt(track_data,delimiter=',') # numpy array

    tracks = np.vstack((tracks,track))

np.savetxt("./data/train/miniTest.csv", tracks, delimiter=",")




