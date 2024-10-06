# Импорт необходимых библиотек
from selenium import webdriver
import re
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt
import time
import csv
# Настройки для запуска браузера

# Создание объекта драйвера

driver = webdriver.Chrome()

# Открытие страницы с предложениями аренды квартир
url = "https://kazan.cian.ru/snyat-kvartiru-studiya-ili-1-komn/"
driver.get(url)

# Задержка, чтобы страница успела загрузиться
time.sleep(10)

# Парсинг цен квартир
try:
    # Используем XPath для нахождения цены
    prices = driver.find_elements(By.XPATH, '//div[@data-name="PriceLayout"]//span[contains(@class, "aee5b7c44e--text--e4SBY")]')

except Exception as e:
    print(f'Произошла ошибка: {e}')
finally:
    pass
    # Закрытие драйвера

#price_list = [price.text for price in prices]
price_list = [re.sub(r'\D', '', price.text) for price in prices]
# Вывод полученных данных

for i, price in enumerate(price_list, start=1):
    print(f"Квартира {i}: {price}")

with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in price_list:
        writer.writerow([price])

# Загрузка данных из CSV-файла
file_path = 'prices.csv'
data = pd.read_csv(file_path)



# Предположим, что столбец с ценами называется 'price'
prices = data['Price']



# Построение гистограммы
plt.hist(prices, bins=20, edgecolor='black')


# Мы можем изменить количество bin-ов по своему усмотрению



# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')



# Показать гистограмму
plt.show()



# Закрытие браузера
driver.quit()



