import numpy as np

# Create a sample sinusoidal signal with a phase offset
sampling_rate = 1000  # Hz
duration = 1  # seconds
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
frequency = 50  # Hz
phase_offset_true = np.pi / 4  # True phase offset
signal = np.sin(2 * np.pi * frequency * t + phase_offset_true)

# Perform FFT
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), 1 / sampling_rate)

# Find the index of the dominant frequency (e.g., 50 Hz)
dominant_frequency_index = np.argmax(np.abs(frequencies - frequency) < 0.1)

# Get the phase angle of that frequency component
phase_fft = np.angle(fft_result[dominant_frequency_index])
print(f"Phase from FFT: {phase_fft} radians")
