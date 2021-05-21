import dask
import dask.dataframe as dd
import dask.array as da
import numpy as np

allTracks = np.load("allTracks.npy")
da = dd.from_array(allTracks[0,:])
print("\n done")
print(da.head())