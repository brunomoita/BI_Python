import numpy as np

x = np.random.random(50)
print (x)

xmax = x[x.argmax()] = 0
xmin = x[x.argmin()] = 100

print xmax
print xmin