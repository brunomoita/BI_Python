import matplotlib.pyplot as plt
import numpy as np
from pylab import *
n = 256
X = np.linspace(-np.pi,np.pi,n,endpoint=True)
Y = np.sin(2*X)
plot (X, Y+1, color='blue', alpha=1.00)
plot (X, Y-1, color='blue', alpha=1.00)

plt.fill_between(X,Y, color='Blue')

show()
