import numpy as np


def fft(x):
    n = len(x)
    if n == 1:
        return x
    if n % 2 != 0:
        raise ValueError("size of x must be a power of 2")
    even = fft(x[::2])
    odd = fft(x[1::2])
    factor = np.exp(-2j * np.pi * np.arange(n) / n)
    return np.concatenate([even + factor[:n//2] * odd,
                           even + factor[n//2:] * odd])


if __name__ == "__main__":
    signal = [0, 1, 2, 3]
    harmonics = fft(signal)
    print(harmonics)



