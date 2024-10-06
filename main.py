import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import random

x = [1,2,3,4,5,6]
y = [1,4,9,16,25,36]
plt.style.use('ggplot')
plt.plot(x,y)
plt.title("Мой первый график")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.show()
