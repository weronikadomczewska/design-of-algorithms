import numpy as np


def fft(x):
    n = len(x)
    if n == 1:
        return x
    even = fft(x[::2])
    odd = fft(x[1::2])
    factor = np.exp(-2j * np.pi * np.arange(n) / n)
    return np.concatenate([even + factor[:n//2] * odd,
                           even + factor[n//2:] * odd])


if __name__ == "__main__":
    signal = [0, 1, 2, 3]
    harmonics = fft(signal)
    print(harmonics)



