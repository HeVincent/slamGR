import numpy as np
import bigDaddyData as bdd

path = "./data/mini/"
array = bdd.csv2np(path,"miniTrack",1,800)
np.save("allTracks.npy", array)