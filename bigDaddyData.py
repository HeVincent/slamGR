import csv
import numpy as np
import soundfile as sf

def csv2np(path,fileName, start, end):
    with open(path+fileName+str(start)+'.csv','r') as csv_file: # point at csv file
        print('row: 1/'+str(end+1-start))
        csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

        row_data = next(csv_reader) # numerical track data
        row = np.genfromtxt(row_data,delimiter=',') # numpy array

    array = row

    # for i in np.linspace(1,len(genres)-1,len(genres)-2):
    for i in range(start,end):
        i = str(int(i+1))
        print('row: '+i+'/'+str(end+1-start))

        with open(path+fileName+i+'.csv','r') as csv_file: # point at csv file

            csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

            row_data = next(csv_reader) # numerical track data
            row = np.genfromtxt(row_data,delimiter=',') # numpy array

        array = np.vstack((array,row))
    return array

def csvSplit(sourcePath,sourceName,targetPath,targetName):
    with open(sourcePath+sourceName+'.csv','r') as csv_file: # point at csv file
        csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

        row = 0
        for line in csv_reader: # loads just 1 line into memory
            row+=1
            track_data = line # audio data

            with open(targetPath+targetName+str(row)+'.csv','w') as new_file:
                print('tcTrack'+str(row)+'.csv')

                csv_writer = csv.writer(new_file,delimiter=',')

                csv_writer.writerow(track_data)
    return

def csv2wav(sourcePath,sourceName,targetPath,targetName):
    with open(sourcePath+sourceName+'.csv','r') as csv_file: # point at csv file

        csv_reader = csv.reader(csv_file, delimiter=',') #reader instance

        track_data = next(csv_reader) # numerical track data
        track = np.genfromtxt(track_data,delimiter=',') # numpy array

        sf.write(targetPath+targetName+'.wav', track, 22050) # write to .wav
    return