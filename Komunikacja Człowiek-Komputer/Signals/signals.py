from pylab import *
from numpy import *
import math
from ipywidgets import *

A = 1
F = 2.0
T = 1 / F
f = lambda t: A * np.sin(2 * pi * t * F)

LP = 1
w = 40
TW = 1 / w
t = np.arange(0, LP * T, TW)
n = len(t)
signal = f(t)

fig = plt.figure(figsize=(15, 6), dpi=80)

# Plotting the sampled signal
ax = fig.add_subplot(121)
ax.plot(t, signal, 'o', label="Sampled Signal")

# Plotting the continuous signal
base_t = np.arange(0, LP * T, 1 / 200)
base_signal = f(base_t)
ax.plot(base_t, base_signal, linestyle='-', color='red', label="Continuous Signal")

ax.set_ylim([min(base_signal), max(base_signal)])
ax.set_title("Time Domain Signal")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")
ax.legend()

# Fourier Transform
signal1 = fft.fft(signal)
signal1 = abs(signal1)

# Frequency spectrum
ax = fig.add_subplot(122)
freqs = fft.fftfreq(n, d=TW)
stem(freqs[:n // 2], signal1[:n // 2], '-*')
ax.set_title("Frequency Spectrum")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude")

def prosta(a=2 b=0):
    x= np.linspace(-5,5,100, endpoint = False) #punkty
    f = lambda x : a*x + b
    y = f(x)
    
    fig = plt.figure(figsize=(6,3), dpi = 80)
    ax = fig.add_subplot(111)
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.plot(x,y)
interact(prosta, a=(-5,5,0.5), b=(-5,5,0.5))

<function __main__.prosta(a=2, b=0)>
plt.tight_layout()
plt.show()
