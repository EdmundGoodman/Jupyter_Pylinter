# ==============================================================================
a = 10

# ==============================================================================
print(a)

# ==============================================================================
import time
time.sleep(10)

# ==============================================================================
import sys
from ctypes import CDLL
# This will crash a Linux or Mac system
# equivalent calls can be made on Windows

# Uncomment these lines if you would like to see the segfault

# dll = 'dylib' if sys.platform == 'darwin' else 'so.6'
# libc = CDLL("libc.%s" % dll) 
# libc.time(-1)  # BOOM!!

# ==============================================================================
print("hi, stdout")

# ==============================================================================
from __future__ import print_function
print('hi, stderr', file=sys.stderr)

# ==============================================================================
import time, sys
for i in range(8):
    print(i)
    time.sleep(0.5)

# ==============================================================================
for i in range(50):
    print(i)

# ==============================================================================
for i in range(500):
    print(2**i - 1)
