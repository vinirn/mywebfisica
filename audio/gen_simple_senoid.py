#import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

filepath = './simple_senoid/'

#p = pyaudio.PyAudio()

volume = 0.5
fs = 44100
duration = 2

for n in range(11,49):
	f = 500*np.sqrt(np.cos(2*n)**2 + np.cos(n)**2)

	print(n)
	print(f)

	samples = np.sin(2*np.pi*np.arange(fs*duration) * f/fs)
	samples = samples.astype(np.float32)

	scaled = np.int16(samples/np.max(np.abs(samples)) * 32767)

	outfile = filepath + 'a' + str(n) + '.wav'
	write(outfile, 44100, scaled)

#for n1 in range(1,4):
#	f1 = 500*np.sqrt(np.cos(2*n1)**2 + np.cos(n1)**2)		
#	for n2 in range(1,4):
#		f2 = 500*np.sqrt(np.cos(2*n2)**2 + np.cos(n2)**2)

#		print(n1,' ',n2)
#		print(f1,' ',f2)

#		samples = (np.sin(2*np.pi*np.arange(fs*duration) * f1/fs)+np.sin(2*np.pi*np.arange(fs*duration) * f2/fs))/2
#		samples = samples.astype(np.float32)

#		scaled = np.int16(samples/np.max(np.abs(samples)) * 32767)

#		outfile = 'a' + str(n1) + 'a' + str(n2) + '.wav'
#		write(outfile, 44100, scaled)
