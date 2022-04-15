#import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

filepath = './'

#p = pyaudio.PyAudio()

volume = 0.5
fs = 44100
duration = 2

for n in range(11,12):
	f = 30000

	print(n)
	print(f)

	samples = np.sin(2*np.pi*np.arange(fs*duration) * f/fs)
	samples = samples.astype(np.float32)

	scaled = np.int16(samples/np.max(np.abs(samples)) * 32767)

	outfile = filepath + 'a' + str(n) + '.wav'
	write(outfile, 44100, scaled)

