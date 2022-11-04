import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

k = np.arange(0,8)
x = np.cos(2*k*np.pi/4)

plt.stem(k,x,use_line_collection=True)
plt.show()