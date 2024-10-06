import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import random

x = np.linspace(-10, 10, 100)
y = x*x
plt.plot(x, y)
plt.xlabel('Ось Х')
plt.ylabel('Ось У')
plt.title('График функции y = x*x')
plt.grid(True)
plt.show()