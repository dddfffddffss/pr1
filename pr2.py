import numpy as np
import matplotlib.pyplot as plt

size, p = 1000, 0

y = []
for i in np.random.laplace(0, 0.08, size=size):
	p+=i
	y.append(p)

plt.plot(range(size),y)
plt.show()