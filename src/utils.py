# ...existing code...
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq


def load_observation_file(path, sr=8000, offset=2048, max_lines=None):
    """
    Load an observation text file with lines "value,err".
    Returns: (time, source, err, sr)
    - time: 1D numpy array of time samples (seconds)
    - source: 1D numpy array (offset removed)
    - err: 1D numpy array (offset removed)
    """
    lines = []
    with open(path, "r") as fh:
        for i, ln in enumerate(fh):
            ln = ln.strip()
            if not ln:
                continue
            lines.append(ln)
            if max_lines and len(lines) >= max_lines:
                break

    src = []
    er = []
    for ln in lines:
        parts = ln.split(",")
        if len(parts) < 2:
            continue
        try:
            src.append(int(parts[0]) - offset)
            er.append(int(parts[1]) - offset)
        except ValueError:
            # skip malformed lines
            continue

    source = np.array(src, dtype=float)
    err = np.array(er, dtype=float)
    N = len(source)
    T = 1.0 / sr
    time = np.arange(N) * T
    return time, source, err, sr


# ...existing code...
def plot_time_and_frequency(time, source, err, sr=8000, show=True, save_prefix=None):
    """
    Plot time-domain, frequency-domain magnitude, and phase.
    - time, source, err: arrays returned by load_observation_file
    - sr: sample rate (Hz)
    - show: if True, calls plt.show()
    - save_prefix: if provided, saves figures to '{save_prefix}_<fig>.png'
    """
    N = len(source)
    if N == 0:
        raise ValueError("Empty source array")

    T = 1.0 / sr

    # Time domain
    plt.figure("time domain")
    plt.clf()
    plt.plot(time, source, label="source")
    plt.plot(time, err, label="error")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (digital)")
    plt.legend()
    plt.grid(True)

    # Frequency domain (magnitude)
    f_xaxis = fftfreq(N, T)[: N // 2]
    f_source = fft(source)[: N // 2]
    f_err = fft(err)[: N // 2]

    plt.figure("frequency domain")
    plt.clf()
    plt.plot(f_xaxis, np.abs(f_source), label="source")
    plt.plot(f_xaxis, np.abs(f_err), label="err")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (digital)")
    plt.legend()
    plt.grid(True)

    # Phase plot
    phase_source = np.angle(f_source)
    plt.figure("phase spectrum", figsize=(10, 5))
    plt.clf()
    plt.plot(f_xaxis, phase_source)
    plt.title("Phase Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (radians)")
    plt.grid(True)

    if save_prefix:
        for fig_num in plt.get_fignums():
            fig = plt.figure(fig_num)
            fig_name = f"{save_prefix}_{fig_num}.png"
            fig.savefig(fig_name, dpi=200)

    if show:
        plt.show()


# ...existing code...

if __name__ == "__main__":
    from src.utils import load_observation_file, plot_time_and_frequency

time, source, err, sr = load_observation_file(
    "./dataset/observation/4000hz/100hz4000.txt", sr=4000
)
plot_time_and_frequency(time, source, err, sr)
