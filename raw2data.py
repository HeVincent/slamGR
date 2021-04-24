import csv
import numpy as np
import soundfile as sf

with open('./raw/mini/Audio_data_mini.csv','r') as csv_file: # point at csv file

    csv_reader = csv.reader(csv_file, delimiter=',') #reader instance
    row = 0

    for line in csv_reader:

        row+=1

        track_data = line # audio data

        with open('./data/mini/miniTrack'+str(row)+'.csv','w') as new_file:
            print('tcTrack'+str(row)+'.csv')

            csv_writer = csv.writer(new_file,delimiter=',')

            csv_writer.writerow(track_data)

