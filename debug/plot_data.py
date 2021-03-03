import matplotlib.pyplot as plt
import numpy as np

time_step = []
amplitude1 = []
amplitude2 = []

file1 = open('./dataset/observation/4000hz/200hz4000.txt','r') 
contents = file1.read()
contents = contents.split('\n')
for i, content in enumerate(contents):
    time_step.append(i*0.00025)
    data = content.split(',')
    amplitude1.append(int(data[0]))
    amplitude2.append(int(data[1]))
file1.close()
time_step = np.array(time_step)
amplitude1 = np.array(amplitude1)
amplitude2 = np.array(amplitude2)

plt.plot(time_step, amplitude1, label='source signal')
plt.plot(time_step, amplitude2, label='error signal')

plt.xlabel('Time (hr)')
plt.ylabel('amplitude (digital)')
plt.legend()
plt.grid()
plt.show()