from tsfresh import extract_features
import pandas as pd
import numpy as np

allTracks = np.load("./allTracks.npy")
allTracks = np.transpose(allTracks)
print("Loading done")
df = pd.DataFrame(allTracks)
df.index.name = "time"
# print("coversion done")
# f_features = extract_features(df, column_id="id", column_sort="time")
# print("done")