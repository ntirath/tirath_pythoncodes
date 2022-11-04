import sounddevice as sd
import numpy as np   # We use this one to do numerical operations
import matplotlib.pyplot as plt  # We use this one to plot things
from scipy.io.wavfile import write


fs = 44100  # Sample rate
seconds = 5  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output_a.wav', fs, myrecording)  # Save as WAV file
p_wav = myrecording
# We'll use the numpy function "linspace" to create a time axis for plotting
p_timeaxis = np.linspace(0,0.6,len(p_wav))
# And plot them
f1=plt.figure(1,figsize=(14,4))
plt.subplot(211)
plt.plot(p_timeaxis,p_wav)