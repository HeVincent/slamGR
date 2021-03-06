from tsfresh import extract_features
import pandas as pd
import numpy as np

allTracks = np.load("./allTracks.npy")
allTracks = np.transpose(allTracks)


mod = np.zeros([2,allTracks.shape[0]])


time = np.linspace(0,allTracks.shape[0]-1,allTracks.shape[0])
time = time.astype('int')
idt = np.ones(allTracks.shape[0])

mod[0,:] = time
mod[1,:] = idt
mod = mod.astype('int')
mod = np.transpose(mod)
a = allTracks[:,1:2]
npPre = np.append(mod,a,axis=1)
print("Loading done")
df = pd.DataFrame(npPre)
df = df.rename(columns={0:"time"})
df = df.rename(columns={1:"id"})


df.set_index("time")
print("coversion done")
df_features = extract_features(df, column_id="id", column_sort="time")
print("done")