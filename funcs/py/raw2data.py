def convert(sourceFile, targetPath,targetName):

# targetname should be without file extension
# targetPath should en with /

    import csv
    import numpy as np

    # with open('./raw/twoClass/Audio_data_two_class.csv','r') as csv_file: # point at csv file
    with open(sourceFile,'r') as csv_file: # point at csv file

        csv_reader = csv.reader(csv_file, delimiter=',') # reader for source csv
        row = 0

        for line in csv_reader: # every row

            row+=1

            track_data = line # audio data

            with open(targetPath+targetName+str(row)+'.csv','w') as new_file: # writer for target csv
                
                print('tcTrack'+str(row)+'.csv') # log progress

                # write row into separate file
                csv_writer = csv.writer(new_file,delimiter=',')
                csv_writer.writerow(track_data)

