import math
import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Initialize fft function from fft.c
#def fourier_transform(f, nn, isign):
#    fun = ctypes.CDLL(fft.so)   
#    fun.fft.argtypes(ctypes.c_arr, ctypes.c_long, ctypes.c_int) # Check if c_arr is a thing

    # Call fft
#    fun.fft(f, nn, 1)

###################################
# Experiment 1.a
f = [2,3,4,4] # Input Signal
nn = 4 # Must be power of 2

# Apply fourier transform to signal
#fourier_transform(f, nn, 1)

###################################
# Experiment 1.b
u = 8
N = 128

###################################
# Experiment 1.c
# Open Rect_128.dat
file = open("Rect_128.dat", "r") 
read_file = file.read()
rect_data = read_file.split("\n")
x = []
y = []
for i in range(len(rect_data)):
    x.append(i)
    y.append(rect_data[i])


plt.plot(x, y, 'ro')
plt.axis([0, 128, 0, 2])

plt.title("Rect_128.dat")
plt.xlabel("Real (X)")
plt.ylabel("Imaginary (Y)")
plt.show()