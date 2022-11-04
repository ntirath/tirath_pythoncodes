#sine wave
import numpy as np
import math

import matplotlib.pyplot as nplot
d = int(input("Enter the value of how many cycles in term of degrees = "))
x = (d/180)*math.pi
y = x/100


theta = np.arange(0, x, y);


amp   = np.sin(theta)
nplot.plot(theta, amp)
amp   = np.cos(theta)
nplot.plot(theta, amp)
nplot.show()