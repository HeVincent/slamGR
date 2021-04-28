import ffStore as ffs

winShort = 216
winLong = 3898
stepShort = int(winShort/2)
stepLong = int(winLong/2)
sampling_rate = 22050

STFT_window = winLong
STFT_interval = stepLong

ffs.spect('./data/mini/','miniTrack1','./graphics/winLengthDemo/','longWindow',winLong,stepLong,sampling_rate)

STFT_window = winShort
STFT_interval = stepShort

ffs.spect('./data/mini/','miniTrack1','./graphics/winLengthDemo/','shortWindow',winShort,stepShort,sampling_rate)