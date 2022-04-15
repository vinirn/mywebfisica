#import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

filepath = './double_senoid/'

#p = pyaudio.PyAudio()

volume = 0.5
fs = 44100
duration = 2

for n in range(25,37):
	f1 = n*10;
	f2 = n*15;
	#if f1<100:
	#	f1 = f1 + 100;
	#if f2<100:
	#	f2 = f2 + 100;

	f1 = f1**1.2
	f2 = f2**1.2


	print(n)
	print(str(f1) + ' Hz')
	print(str(f2) + ' Hz')

	samples = 2*np.sin(2*np.pi*np.arange(fs*duration) * f1/fs) +\
			  1*np.sin(2*np.pi*np.arange(fs*duration) * f2/fs)
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
