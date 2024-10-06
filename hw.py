from selenium import webdriver
import re
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt
import time
import csv
import numpy as np

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)