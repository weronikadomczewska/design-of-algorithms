import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos
from scipy.fft import fft, ifft

def generate_samples():
    i = 64
    j = 64
    As = np.random.rand(i)
    small_as = np.random.rand(i)
    Bs = np.random.rand(j)
    small_bs = np.random.rand(j)

    first_sum = []
    second_sum = []

    ts = range(i)

    for first_cnt in range(i):
        first_sum.append(As[first_cnt] * sin(small_as[first_cnt] * ts[first_cnt]))

    for second_cnt in range(j):
        second_sum.append(Bs[second_cnt] * cos(small_bs[second_cnt] * ts[second_cnt]))

    total_sum = []
    for cnt in range(i):
        total_sum.append(first_sum[cnt] + second_sum[cnt])
    return ts, total_sum


times, signal = generate_samples()
fft_signal = fft(signal)
freqs = np.fft.fftfreq(len(signal), times[1]-times[0])
print(freqs)

fig, ax = plt.subplots(2, 1)
ax[0].plot(times, signal)
ax[0].set_title("Signal in time domain")
ax[1].plot(freqs, fft_signal)
ax[1].set_title("Signal after Fourier transform in frequency domain")
plt.tight_layout()
plt.show()


frequencies_to_remove = np.linspace(0, 0.25)
for freq in frequencies_to_remove:
    fft_signal[np.where(freqs == freq)] = 0
    fft_signal[np.where(freqs == -freq)] = 0

filtered_signal = ifft(fft_signal)
fft_filtered_signal = fft(filtered_signal)

fig, ax = plt.subplots(2, 1)
ax[0].plot(freqs, fft_signal, color="orange")
ax[0].set_title("Original signal\'s Fourier transform in frequency domain")
ax[1].plot(freqs, fft_filtered_signal)
ax[1].set_title("Filtered signal\'s Fourier transform in frequency domain")
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(2, 1)
ax[0].plot(times, fft_signal, color="orange")
ax[0].set_title("Original signal\'s Fourier transform in time domain")
ax[1].plot(times, fft_filtered_signal)
ax[1].set_title("Filtered signal\'s Fourier transform in time domain")
plt.tight_layout()
plt.show()







