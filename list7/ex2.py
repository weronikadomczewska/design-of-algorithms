import numpy as np


def fft(signal):
    """
    Only use when the number of samples is a power of 2
    """
    n = len(signal)
    if n <= 1:
        return signal
    even = fft(signal[0::2])
    odd = fft(signal[1::2])
    T = [np.exp(-2j * np.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + T[k] for k in range(n // 2)] + [even[k] - T[k] for k in range(n // 2)]


signal = [0, 1, 2, 3]
harmonics = fft(signal)
print(harmonics)



