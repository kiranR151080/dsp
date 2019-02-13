import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('kiran.wav')
print(fs,len(data),data)
plt.subplot(211)
plt.plot(data)
plt.subplot(212)
t=np.arange(0,len(data)/fs,1.0/fs)
plt.plot(t,data)
wav.write('kiran1.wav',2*fs,data)
wav.write('kiran2.wav',0.5*fs,data)
plt.show()

