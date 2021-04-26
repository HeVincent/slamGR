import csv
import numpy as np
import sklearn
from sklearn import preprocessing as pp

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