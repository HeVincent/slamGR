from tsfresh import extract_features
import pandas as pd
import numpy as np
import time as timer
import dask
import dask.dataframe as dd
import dask.array as da

start_time = timer.time()

allTracks = np.load("./allTracks.npy")
allTracks = np.transpose(allTracks)
n = allTracks.shape[0]

mod = np.zeros([2,n])


time = np.linspace(0,n-1,n)
time = time.astype('int')
idt = np.ones(n)

mod[0,:] = time
mod[1,:] = idt
mod = mod.astype('int')
mod = np.transpose(mod)
a = allTracks[0:n,0:1]
npPre = np.append(mod,a,axis=1)
print("Loading done")


df = dd.from_array(npPre)



df = df.rename(columns={0:"time"})
df = df.rename(columns={1:"id"})
df = df.rename(columns={2:"track"})



df.set_index("time")
print("coversion done")
df_features = extract_features(df, column_id="id", column_sort="time")
print("\ndone")
print("--- %s seconds ---" % (timer.time() - start_time))