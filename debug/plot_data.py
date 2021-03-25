import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq

time_step = []
source = []
err = []

SR = 4000
DURATION = 2
N = SR * DURATION 
T = 1/SR

file1 = open('./dataset/observation/4000hz/200hz4000.txt','r') 
contents = file1.read()
contents = contents.split('\n')
for i, content in enumerate(contents):
    time_step.append(i*T)
    data = content.split(',')
    source.append(int(data[0])-2048)
    err.append(int(data[1])-2048)
file1.close()

time_step = np.array(time_step)
source = np.array(source)
err = np.array(err)

plt.figure("time domain")
plt.plot(time_step, source, label='source')
plt.plot(time_step, err, label='error')

plt.xlabel('Time (hr)')
plt.ylabel('amplitude (digital)')
plt.legend()
plt.grid()

f_xaxis = fftfreq(N, T)[:N//2]

f_source = fft(source)[:N//2]
f_err = fft(err)[:N//2]

plt.figure("frequency domain")
plt.plot(f_xaxis, np.abs(f_source), label='source')
plt.plot(f_xaxis, np.abs(f_err), label='err')

plt.xlabel('frequency (hz)')
plt.ylabel('amplitude (digital)')
plt.legend()
plt.grid()

plt.show()