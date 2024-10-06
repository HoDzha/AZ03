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

# Построение гистограммы
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')

# Добавление заголовка и меток осей
plt.title("Гистограмма нормального распределения")
plt.xlabel("Значение")
plt.ylabel("Плотность вероятности")

# Отображение гистограммы
plt.show()

# Количество точек
num_points = 1000

# Генерация двух наборов случайных чисел в диапазоне от 0 до 1
x = np.random.rand(num_points)
y = np.random.rand(num_points)



# Построение диаграммы рассеяния
plt.scatter(x, y, alpha=0.5)

# Добавление заголовка и меток осей
plt.title("Диаграмма рассеяния случайных данных")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

# Отображение диаграммы
plt.show()



# Инициализация драйвера
driver = webdriver.Chrome()
url = "https://www.divan.ru/ufa/category/divany-i-kresla"
driver.get(url)

# Пауза для загрузки страницы
time.sleep(5)

# Собираем данные о светильниках
products = driver.find_elements(By.CLASS_NAME, 'lsooF')  # Элемент карточки товара

data = []
divans_price=[]
print(products)
# driver.quit()

# Цикл по всем элементам на странице
for product in products:
    try:
        # Название светильника
 #       name = product.find_element(By.CLASS_NAME, 'item__title').text
        name = product.find_element(By.CSS_SELECTOR, "span[itemprop='name']").text

        # Цена светильника
        price = product.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU.KIkOH[data-testid='price']").text

        # Ссылка на продукт
        link = product.find_element(By.CSS_SELECTOR, "link[itemprop='url']").get_attribute('href')

        data.append([name, price, link])
        divans_price.append([re.sub(r"\D", "", price)])
    except Exception as e:
        print(f"Ошибка при обработке элемента: {e}")

# Закрываем браузер
driver.quit()

# Запись данных в CSV файл

with open('result.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Название", "Цена", "Ссылка"])  # Заголовки столбцов
    writer.writerows(data)

with open('divans_price.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Цена"])  # Заголовки столбцов
    writer.writerows(divans_price)

df = pd.read_csv('divans_price.csv')
print(df.describe())
print('Средняя цена дивана:', df['Цена'].mean(),' рублей')

plt.hist(df, bins=20, edgecolor='black')
plt.show()

print("Данные успешно выгружены")