import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos
from scipy.fft import fft, ifft

def generate_samples(sampling_rate):
    As = [10, 20, 30]
    small_as = [40, 50, 60]
    Bs = [20, 40, 60]
    small_bs = [10, 30, 50]

    first_sum = []
    second_sum = []

    time_interval = 1.0 / sampling_rate
    ts = np.arange(0, 1, time_interval)

    for first_cnt in range(sampling_rate):
        first_sum.append(As[first_cnt % len(As)] * sin(small_as[first_cnt % len(small_as)] * ts[first_cnt]))

    for second_cnt in range(sampling_rate):
        second_sum.append(Bs[second_cnt % len(Bs)] * cos(small_bs[second_cnt % len(small_bs)] * ts[second_cnt]))

    total_sum = np.add(first_sum, second_sum)
    return ts, total_sum

sampling_rate = 256
times, signal = generate_samples(sampling_rate)
fft_signal = fft(signal)
N = len(fft_signal)
n = np.arange(N)
T = N/sampling_rate
freqs = n/T


fig, ax = plt.subplots(2, 1)
ax[0].plot(times, signal)
ax[0].set_title("Signal in time domain")
ax[1].plot(freqs, fft_signal)
ax[1].set_title("Signal after Fourier transform in frequency domain")
plt.tight_layout()
plt.show()

frequencies_to_remove = [int(input("Enter frequency to remove: "))]

fig, ax = plt.subplots(2, 1)
ax[0].plot(freqs, fft_signal, color="orange")
ax[0].set_title("Original signal\'s Fourier transform in frequency domain")

for freq in frequencies_to_remove:
    fft_signal[np.where(freqs >= freq)] = 0

filtered_signal = ifft(fft_signal)
fft_filtered_signal = fft(filtered_signal)


ax[1].plot(freqs, fft_filtered_signal)
ax[1].set_title("Filtered signal\'s Fourier transform in frequency domain")
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(2, 1)
ax[0].plot(times, signal, color="orange")
ax[0].set_title("Original signal\'s Fourier transform in time domain")
ax[1].plot(times, filtered_signal)
ax[1].set_title("Filtered signal\'s Fourier transform in time domain")
plt.tight_layout()
plt.show()
