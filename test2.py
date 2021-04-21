import csv
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import soundfile as sf

with open('./twoClass/Audio_data_two_class.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    row1 = next(csv_reader)
    print(row1)
    audio_data = np.genfromtxt(row1,delimiter=',')

    sf.write('test.wav', audio_data, 22050)

